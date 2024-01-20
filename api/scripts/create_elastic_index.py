from elasticsearch import Elasticsearch
import os
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from tqdm import tqdm

# Connect to your Elasticsearch instance
es = Elasticsearch([{'host': 'es01', 'port': 9200}])

# Path to the folder containing your text files
folder_path = '../src/core/files'

# Index name in Elasticsearch
index_name = 'es_db'


mapping = {
    "properties": {
        "content": {
            "type": "text",
            "analyzer": "standard"
        },
        "filename": {
            "type": "text"
        }
        # Add other fields as needed
    }
}

# Delete the index
es.indices.delete(index=index_name, ignore=400)

# Create the index
es.indices.create(index=index_name, body={"mappings": mapping}, ignore=400)

# Iterate through each file in the folder
for filename in tqdm(os.listdir(folder_path)):
    if filename.endswith(".txt"):
        file_path = os.path.join(folder_path, filename)

        # Read the content of the text file
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()


        # Index the document
        document = {
            'filename': filename[:-4],
            'content': file_content
        }

        # Index the document in Elasticsearch
        es.index(index=index_name, body=document)

print("Indexing completed.")