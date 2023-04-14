from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv


import os, sys, json, re
from tqdm import tqdm

ENV_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "backend.env")
load_dotenv(ENV_PATH)

DOCS_PATH = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(__file__)

sys.path.append(DOCS_PATH)


import src.models as docs_models


with open(os.path.join(BASE_DIR, "enhanced.pnst_meta.json"), "r", encoding="utf8") as f:
    meta = json.load(f)


engine = create_engine(os.environ["DATABASE_URL"])

session = sessionmaker(bind=engine)()


docs_to_add = []
authors_to_add = []
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

        authors = []
        if "Auteur(s)" in doc.keys():
            auteurs = doc.get("Auteur(s)").split(";")
            auteurs = [
                {
                    "fullname": re.sub(r"[،,\s]", " ", re.sub(r"\(.*", "", all_)),
                    "role": re.sub(r"\)", "", re.sub(r".*\(", "", all_)),
                }
                for all_ in auteurs
                if all_
            ]
            for author in auteurs:
                db_author = docs_models.Author()
                db_author.full_name = author.get("fullname")
                authors_to_add.append(db_author)
                authors.append(db_author)

        db_doc.authors = authors

        docs_to_add.append(db_doc)
        
session.add_all(docs_to_add + authors_to_add)
# session.bulk_save_objects(authors_to_add)
session.commit()



# build a function that calc the sum
