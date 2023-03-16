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
        ]

        db_author = docs_models.Author()
        document_id = (
            session.query(docs_models.Document)
            .filter(docs_models.Document.title == doc.get("Titre"))
            .first()
            .id
        )

        for auteur in auteurs:
            db_author.full_name = auteur.get("fullname")
            all_auteurs.append(db_author)
            author_role.append({"document_id": document_id})

try:
    session.bulk_save_objects(all_auteurs)
except:
    pass

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
    db_role.book_id = role.get("document_id")
    db_role.role = role.get("role")
    roles.append(role)

session.bulk_save_objects(roles)


# document_id = session.query(docs_models.Document).filter(docs_models.Document.title == doc.get('Titre')).first().id


#     if doc.get("Titre"):
#         db_doc = docs_models.Document()
#         db_doc.repo_id = doc.get("id")
#         db_doc.source = doc.get("source")

#         db_doc.title = doc.get("Titre")
#         db_doc.type = doc.get("Type de document")
#         db_doc.lang = doc.get("Langue")
#         db_doc.abstract = doc.get("Résumé")

#         if "Theme" in doc.keys():
#             db_doc.domain = doc.get("Theme")
#         if "url" in doc.keys():
#             db_doc.url = doc.get("url")

#         docs_to_add.append(db_doc)
# session.bulk_save_objects(docs_to_add)
# session.commit()
