from elasticsearch import Elasticsearch
import os

es = Elasticsearch()
directory = "sampleIndex/txt files"


def buildindex(field="body", name="sample-index"):
    for txt_idx, txt_file_name in enumerate(os.listdir(directory)):
        doc = {
            field: open(directory + os.sep + txt_file_name, 'r').read().replace("\u200c", " ")
        }
        es.index(index=name, id=txt_idx + 1, body=doc)
