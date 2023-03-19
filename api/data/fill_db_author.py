from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv


import os, sys, json, re
from tqdm import tqdm

ENV_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
load_dotenv(ENV_PATH)

DOCS_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "src")
BASE_DIR = os.path.dirname(__file__)

sys.path.append(DOCS_PATH)


import models as docs_models


with open(os.path.join(BASE_DIR, "enhanced.pnst_meta.json"), "r", encoding="utf8") as f:
    meta = json.load(f)


engine = create_engine(os.environ["DATABASE_URL"])

session = sessionmaker(bind=engine)()


docs_to_add = []
all_auteurs = []
author_role = []
for doc in tqdm(meta):
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

        document_id = (
            session.query(docs_models.Document)
            .filter(docs_models.Document.title == doc.get("Titre"))
            .first()
            .id
        )

        for auteur in auteurs:
            db_author = docs_models.Author()
            db_author.full_name = auteur.get("fullname")
            all_auteurs.append(db_author)
            author_role_item = auteur | {"document_id": document_id}
            author_role.append(author_role_item)


session.bulk_save_objects(all_auteurs)


roles = []
for role in tqdm(author_role):
    author_id = (
        session.query(docs_models.Author)
        .filter(docs_models.Author.full_name == role.get("fullname"))
        .first()
        .id
    )

    db_role = docs_models.Doc_Author()
    db_role.author_id = author_id
    db_role.document_id = role.get("document_id")
    db_role.role = role.get("role")
    roles.append(db_role)

session.bulk_save_objects(roles)


session.commit()
