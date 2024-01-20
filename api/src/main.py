from fastapi import FastAPI, UploadFile, File
from fastapi_sqlalchemy import DBSessionMiddleware, db
from fastapi.middleware.cors import CORSMiddleware

from .docs import models as docs_models
from .core import query_index
from .schemas import SimpleQuery, FileQuery, CompareRequest
from .utils import clean_text, extract_from_pdf

import os
import re
import tempfile
from dotenv import load_dotenv
import textract
import unicodedata as ud
import langdetect as ld

from elasticsearch import Elasticsearch

# Connect to your Elasticsearch instance
es = Elasticsearch([{'host': 'es01', 'port': 9200}])

# Index name in Elasticsearch
index_name = 'es_db'




# Create a FastAPI instance
app = FastAPI()

# Load environment variables
ENV_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "backend.env")
load_dotenv(ENV_PATH)

# Define allowed origins for CORS
origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://127.0.0.1",
    "http://127.0.0.1:5173",
]

# Add middleware for database sessions
app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])

# Add middleware for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Root endpoint to check if the API is running
@app.get("/api/")
async def hello_world():
    return {"message": "Welcome to plagiarism detection in scientific writings"}


# Endpoint to handle text queries
@app.post("/api/most_similar_standard/")
async def most_similar_standard(query: SimpleQuery):
    content = query.content
    k = query.k

    # Clean the input text
    cleaned_text = clean_text(content)


    query = {
    "query": {
        "match": {
            "content": {
                "query": cleaned_text,
                "operator": "or"
            }
        }
    }
}

    # Perform the search
    result = es.search(index=index_name, body=query)

    max_score = max(hit['_score'] for hit in result['hits']['hits'])

    # Display the results
    res = []
    for hit in result['hits']['hits']:
        rate = (hit['_score'] / max_score) * 100
        res.append({"id": hit["_source"]["filename"], "rate":rate})

   

    # Retrieve results from the database
    results = (
        db.session.query(docs_models.Document)
        .filter(docs_models.Document.doc_id.in_([r["id"] for r in res]))
        .all()
    )

    # Format the response
    response = [
        {   "doc_id" : doc.doc_id,
            "title": re.sub(r"\[.*", "", doc.title),
            "rate": rate * 100 // 100,
            "url": doc.url,
            "authors": doc.authors,
            "lang": ld.detect(doc.title),
        }
        for doc, rate in zip(results, [r["rate"] for r in res])
    ]

    return {"response": response}


# Endpoint to handle text queries
@app.post("/api/most_similar/")
async def most_similar(query: SimpleQuery):
    content = query.content
    k = query.k

    # Clean the input text
    cleaned_text = clean_text(content)

    
    # Perform the search
    res = query_index.search(cleaned_text, k)

    # Retrieve results from the database
    results = (
        db.session.query(docs_models.Document)
        .filter(docs_models.Document.doc_id.in_([r["id"] for r in res]))
        .all()
    )

    # Format the response
    response = [
        {   "doc_id" : doc.doc_id,
            "title": re.sub(r"\[.*", "", doc.title),
            "rate": rate,
            "url": doc.url,
            "authors": doc.authors,
            "lang": ld.detect(doc.title),
        }
        for doc, rate in zip(results, [r["rate"] for r in res])
    ]

    return {"response": response}


# Endpoint to handle file uploads
@app.post("/api/most_similar_file/")
async def most_similar_file(file: UploadFile = File(...), k: int = 5):
    content = file

    if content.filename.endswith(".txt"):
        contents = await content.read()
        cleaned_text = clean_text(contents.decode("utf-8"))

    else:
        contents = await content.read()
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(contents)
            tmp_file_path = tmp_file.name

        if content.filename.endswith(".pdf"):
            text = extract_from_pdf(tmp_file_path)
        elif content.filename.endswith(".docx"):
            text = textract.process(tmp_file_path, method="python-docx").decode("utf-8")

        os.unlink(tmp_file_path)

        text = ud.normalize("NFKD", text)
        cleaned_text = clean_text(text)

    # Perform the search
    res = query_index.search(cleaned_text, k)

    # Retrieve results from the database
    results = (
        db.session.query(docs_models.Document)
        .filter(docs_models.Document.repo_id.in_([r["id"] for r in res]))
        .all()
    )

    # Format the response
    response = [
        {
            "title": re.sub(r"\[.*", "", doc.title),
            "rate": rate,
            "url": doc.url,
            "authors": doc.authors,
            "lang": ld.detect(doc.title),
        }
        for doc, rate in zip(results, [r["rate"] for r in res])
    ]

    return {"response": response}


# Endpoint to compare a list of source texts against a target text
@app.post("/api/compare/")
async def compare_texts(request: CompareRequest):

    target_text = request.target
    source = request.source



    # Calculate similarity rates using SequenceMatcher
    similarity_rates = query_index.compare_vectors(source, target_text)
  
    print(similarity_rates)

    return {"similarity_rates": similarity_rates}
