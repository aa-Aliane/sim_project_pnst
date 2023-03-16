from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from collections import Counter
import unicodedata as ud

import os, sys, json
from tqdm import tqdm

ENV_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
load_dotenv(ENV_PATH)

DOCS_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "src")
BASE_DIR = os.path.dirname(__file__)

sys.path.append(DOCS_PATH)


import models as docs_models

engine = create_engine(os.environ["DATABASE_URL"])
session = sessionmaker(bind=engine)()


db_docs = [str(doc.domain).lower() for doc in session.query(docs_models.Document).all()]
domains = Counter(db_docs)


with open(os.path.join(BASE_DIR, "pnst_domains.json"), "w", encoding="utf8") as f:
    json.dump(domains, f, ensure_ascii=False)
