from elasticsearch import Elasticsearch
import os


def buildindex(name="sample-index", field="body", directory="sampleIndex/txt files"):
    es = Elasticsearch()
    for txt_idx, txt_file_name in enumerate(os.listdir(directory)):
        doc = {
            field: open(directory + os.sep + txt_file_name, 'r').read().replace("\u200c", " ")
        }
        es.index(index=name, id=txt_idx + 1, body=doc)
