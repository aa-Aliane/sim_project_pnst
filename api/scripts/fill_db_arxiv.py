from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv


import os, sys, json
from tqdm import tqdm

ENV_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "backend.env")
load_dotenv(ENV_PATH)

DOCS_PATH = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(__file__)

sys.path.append(DOCS_PATH)


import src.models as docs_models




engine = create_engine(os.environ["DATABASE_URL"])

session = sessionmaker(bind=engine)()


with open("../data/arxiv_articles_db.json", "r", encoding="utf8") as f:
    meta = json.load(f)

for doc in meta:
    print(doc.keys())



docs_to_add = []
authors_to_add = []
for doc in tqdm(meta):
    db_doc = docs_models.Document()
    db_doc.doc_id = doc["article_id"]
    
    db_doc.title = doc["title"]
    db_doc.lang = "en"
    db_doc.abstract = doc["abstract_text"]
    db_doc.authors = doc["authors"]


    docs_to_add.append(db_doc)



session.add_all(docs_to_add)
session.commit()