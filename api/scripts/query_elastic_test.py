from elasticsearch import Elasticsearch

# Connect to your Elasticsearch instance
es = Elasticsearch([{'host': 'es01', 'port': 9200}])

# Index name in Elasticsearch
index_name = 'es_db'


# Define your query for the provided sentence
sentence_to_search = """however , notice that alice s reduced density matrix does not depend on what happens in the optical channel , nor on any of bob s measurement results .
her expectation values can be completely determined from the initial state @xmath10 .
indeed , alice s measurement results can be thought of as classical registers which merely record which mode state was sent through the device .
this observation allows us to move from an entanglement - based ( eb ) picture to an equivalent ` prepare and measure ' ( pm ) scenario @xcite , in which alice s measurements are absorbed into the initial state preparation .    in a pm scenario ,
we retain full knowledge of @xmath9 , in particular the off - diagonal coherence term"""

query = {
    "query": {
        "match": {
            "content": {
                "query": sentence_to_search,
                "operator": "or"
            }
        }
    }
}

# Perform the search
result = es.search(index=index_name, body=query)

max_score = max(hit['_score'] for hit in result['hits']['hits'])

# Display the results
for hit in result['hits']['hits']:
    percentage_score = (hit['_score'] / max_score) * 100
    print(f"Document Name: {percentage_score}")
