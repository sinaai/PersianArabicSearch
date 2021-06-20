import spacy
from spacy_cld import LanguageDetector
from langdetect import detect, LangDetectException

nlp = spacy.load("xx_ent_wiki_sm")
language_detector = LanguageDetector()
nlp.add_pipe(language_detector)


def spacy_language_detector(string):
    doc = nlp(string)
    lang = doc._.languages
    if lang in [['fa'], ['ar']]:
        pass
    else:
        lang = ['fa']
    return lang[0]


def lang_detect(string):
    try:
        lang = detect(string)
    except LangDetectException:
        lang = 'fa'
    if lang in {'fa', 'ar'}:
        pass
    else:
        lang = 'fa'
    return lang


def language_detector(string, library="langdetect"):
    if library == "langdetect":
        lang_detect(string)
    elif library == "spacy":
        spacy_language_detector(string)
