import hazm
from nltk.tokenize import WhitespaceTokenizer as wt
from elasticsearch import Elasticsearch
from langDetection import language_detector


def sent_tokenizer(string):
    sentences = hazm.sent_tokenize(string)
    indices = list(wt().span_tokenize_sents(sentences))
    idx = 1
    for s in range(len(indices)):
        for w in range(len(indices[s])):
            indices[s][w] = idx
            idx += 1
    return sentences, indices


def separate_languages(string, library='voting'):
    sentences, indices = sent_tokenizer(string)
    arabic, farsi = '', ''
    arabic_idx, farsi_idx = [], []
    for i, sentence in enumerate(sentences):
        language = language_detector(sentence, library)
        if language == 'fa':
            farsi = farsi + sentence
            farsi_idx += indices[i]
        else:
            arabic = arabic + sentence
            arabic_idx += indices[i]
    return farsi, arabic, farsi_idx, arabic_idx


def rebuild_index(input_index, output_index, text_field, language_detection_library='voting'):
    es = Elasticsearch()
    lastID = es.count(index=input_index)['count']
    mapping = {
        "mappings": {
            "properties": {
                "body": {
                    "type": "text"
                },
                "farsi_field": {
                    "type": "text",
                    "analyzer": "persian"
                },
                "arabic_field": {
                    "type": "text",
                    "analyzer": "arabic"
                }
            }
        }
    }
    es.indices.create(index=output_index, body=mapping)
    for i in range(1, lastID + 1):
        txt = es.get(index=input_index, id=i)['_source'][text_field]
        farsi, arabic, farsi_idx, arabic_idx = separate_languages(txt, language_detection_library)
        doc = {
            text_field: txt,
            "farsi_field": farsi,
            "arabic_field": arabic,
            "farsi_indices": farsi_idx,
            "arabic_indices": arabic_idx
        }
        es.index(index=output_index, id=i, body=doc)
