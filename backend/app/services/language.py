
from langdetect import detect

def detect_language(text):

    lang = detect(text)

    if lang == "hi":
        return "Hindi"

    if lang == "ta":
        return "Tamil"

    return "English"
