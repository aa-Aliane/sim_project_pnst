from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db
from fastapi.middleware.cors import CORSMiddleware
import os
from .docs import models as docs_models
from .core import query_index
from pydantic import BaseModel
from dotenv import load_dotenv


class Query(BaseModel):
    content: str
    k: int | None = 5


app = FastAPI()

BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
load_dotenv(BASE_DIR)

origins = [
    "http://localhosts",
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
async def most_similar(query: Query):
    import unicodedata as ud

    q = ud.normalize("NFKD", query.content)

    res = query_index.search(q, query.k)
    print(type(res))
    results = (
        db.session.query(docs_models.Document)
        .filter(docs_models.Document.repo_id.in_(res))
        .all()
    )
    titles = [{"title": doc.title} for doc in results]
    return {"most similar docs": titles}
