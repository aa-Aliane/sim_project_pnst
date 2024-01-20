import json
from tqdm import tqdm

with open("ids_to_articles.json", "r", encoding="utf8") as f:
    meta = json.load(f)

for doc in tqdm(meta):
    with open(doc['article_id']+".txt", "w", encoding="utf8") as f:
        f.write(doc["article_text"])