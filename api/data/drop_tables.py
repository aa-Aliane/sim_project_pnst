from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv


import os, sys, json
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


docs_models.Base.metadata.drop_all(bind=engine)
