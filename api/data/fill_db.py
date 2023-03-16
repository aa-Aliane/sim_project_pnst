from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv


import os,sys, json
from tqdm import tqdm

ENV_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
load_dotenv(ENV_PATH)

DOCS_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src')
BASE_DIR = os.path.dirname(__file__)

sys.path.append(DOCS_PATH)


import models as docs_models



with open(os.path.join(BASE_DIR, "enhanced.pnst_meta.json"), "r", encoding="utf8") as f:
    meta = json.load(f)




engine = create_engine(os.environ["DATABASE_URL"])

session = sessionmaker(bind=engine)()


docs_to_add = []
for doc in tqdm(meta):
    if doc.get("Titre"):
        db_doc = docs_models.Document()
        db_doc.repo_id = doc.get("id")
        db_doc.source = doc.get("source")

        db_doc.title = doc.get("Titre")
        db_doc.type = doc.get("Type de document")
        db_doc.lang = doc.get("Langue")
        db_doc.abstract = doc.get("Résumé")

        if "Theme" in doc.keys():
            db_doc.domain = doc.get("Theme")
        if "url" in doc.keys():
            db_doc.url = doc.get("url")
            
        docs_to_add.append(db_doc)
session.bulk_save_objects(docs_to_add)
session.commit()


