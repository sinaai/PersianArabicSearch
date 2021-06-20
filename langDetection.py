import spacy
from spacy_cld import LanguageDetector
from langdetect import detect, LangDetectException
import pycld2 as cld2

nlp = spacy.load('xx_ent_wiki_sm')
language_detector = LanguageDetector()
nlp.add_pipe(language_detector)


def spacy_language_detector(string):
    doc = nlp(string)
    lang = doc._.languages
    return lang[0]


def lang_detect(string):
    try:
        lang = detect(string)
    except LangDetectException:
        lang = 'fa'
    return lang


def cld2_language_detector(string):
    is_reliable, text_bytes_found, details = cld2.detect(string)
    if is_reliable:
        return details[0][1]
    else:
        return 'fa'


def language_detector(string, library='pycld2'):
    libraries = {'pycld2', 'langdetect', 'spacy'}
    language = ''

    if library == 'pycld2':
        language = cld2_language_detector(string)
    elif library == 'langdetect':
        language = lang_detect(string)
    elif library == 'spacy':
        language = spacy_language_detector(string)
    else:
        assert (library in libraries)

    if language not in {'fa', 'ar'}:
        return 'fa'
    else:
        return language
