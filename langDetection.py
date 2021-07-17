from spacy_cld import LanguageDetector
from langdetect import detect, LangDetectException
import pycld2 as cld2
import xx_ent_wiki_sm

nlp = xx_ent_wiki_sm.load()
detector = LanguageDetector()
nlp.add_pipe(detector)


def spacy_language_detector(string):
    doc = nlp(string)
    try:
        lang = doc._.languages
    except:
        lang = ''
    if len(lang):
        return lang[0]
    else:
        return ''


def lang_detect(string):
    try:
        lang = detect(string)
    except:
        lang = ''
    return lang


def cld2_language_detector(string):
    try:
        is_reliable, text_bytes_found, details = cld2.detect(string)
    except:
        is_reliable = False
    if is_reliable:
        return details[0][1]
    else:
        return ''


def voting_language_detector(string):
    votes = [cld2_language_detector(string), lang_detect(string), spacy_language_detector(string)]
    if votes.count('fa') == 0 and votes.count('ar') == 0:
        return ''
    else:
        if votes.count('fa') > votes.count('ar'):
            return 'fa'
        else:
            return 'ar'


def language_detector(string, library='voting'):
    libraries = {'voting', 'pycld2', 'langdetect', 'spacy'}
    language = ''

    if library == 'voting':
        language = voting_language_detector(string)
    elif library == 'pycld2':
        language = cld2_language_detector(string)
    elif library == 'langdetect':
        language = lang_detect(string)
    elif library == 'spacy':
        language = spacy_language_detector(string)
    else:
        assert (library in libraries)

    if language not in {'fa', 'ar'}:
        return 'ar'
    else:
        return language
