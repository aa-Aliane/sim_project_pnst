from fastapi import FastAPI, UploadFile, File
from fastapi_sqlalchemy import DBSessionMiddleware, db
from fastapi.middleware.cors import CORSMiddleware

from .docs import models as docs_models
from .core import query_index


from .schemas import SimpleQuery, FileQuery
from .utils import clean_text

import os, re
import tempfile
from dotenv import load_dotenv
import textract
import unicodedata as ud
import langdetect as ld

app = FastAPI()

ENV_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "backend.env")
load_dotenv(ENV_PATH)

origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://127.0.0.1",
    "http://127.0.0.1:5173",
]

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])
# add allowed origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/api/")
async def hello_world():
    return {"message": "welcome to plagiarism detection in scientific writings"}


@app.post("/api/most_similar/")
async def most_similar(query: SimpleQuery):

    content = query.content
    k = query.k

    cleaned_text = clean_text(content)

    res = query_index.search(cleaned_text, k)

    results = (
        db.session.query(docs_models.Document)
        .filter(docs_models.Document.repo_id.in_([r["id"] for r in res]))
        .all()
    )

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


@app.post("/api/most_similar_file/")
async def most_similar_file(file: UploadFile = File(...), k: int = 5):

    content = file

    if content.filename.endswith(".txt"):
        contents = await content.read()
        # text = contents.decode("utf-8")
        cleaned_text = clean_text(text)

    else:
        contents = await content.read()
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(contents)
            tmp_file_path = tmp_file.name

        if content.filename.endswith(".pdf"):
            text = textract.process(tmp_file_path).decode("utf-8")
        elif content.filename.endswith(".docx"):
            text = textract.process(tmp_file_path, method="python-docx").decode("utf-8")

        os.unlink(tmp_file_path)

        text = ud.normalize("NFKD", text)
        cleaned_text = clean_text(text)
        print(cleaned_text)

    res = query_index.search(cleaned_text, k)

    results = (
        db.session.query(docs_models.Document)
        .filter(docs_models.Document.repo_id.in_([r["id"] for r in res]))
        .all()
    )

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
