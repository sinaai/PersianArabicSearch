import hazm
from elasticsearch import Elasticsearch
from langDetection import language_detector


def separate_languages(string, library='voting'):
    sentences = hazm.sent_tokenize(string)
    arabic, farsi = '', ''
    for sentence in sentences:
        language = language_detector(sentence, library)
        if language == 'fa':
            farsi = farsi + sentence
        else:
            arabic = arabic + sentence
    return farsi, arabic


def rebuild_index(index_name, text_field, language_detection_library='voting'):
    es = Elasticsearch()
    lastID = es.count(index=index_name)['count']
    for i in range(1, lastID + 1):
        txt = es.get(index=index_name, id=i)['_source'][text_field]
        farsi, arabic = separate_languages(txt, language_detection_library)
        doc = {
            text_field: txt,
            "farsi_field": farsi,
            "arabic_field": arabic
        }
        es.index(index=index_name, id=i, body=doc)



