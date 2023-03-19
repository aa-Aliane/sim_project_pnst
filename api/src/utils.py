import re
from langdetect import detect


def clean_text(text):
    lang = detect(text)

    # Remove non-alphabetic characters and convert to lowercase
    if lang == "ar":
        cleaned_text = re.sub("[^؀-ۿ]+", " ", text)
        cleaned_text = re.sub("\s+", " ", cleaned_text)
        cleaned_text = cleaned_text.strip()
    elif lang == "fr":
        cleaned_text = re.sub("[^a-zA-ZàâçéèêëîïôûùüÿñæœÀÂÇÉÈÊËÎÏÔÛÙÜŸÑÆŒ]+", " ", text)
        cleaned_text = re.sub("\s+", " ", cleaned_text)
        cleaned_text = cleaned_text.strip().lower()
    else:  # default to English
        cleaned_text = re.sub("[^a-zA-Z]+", " ", text)
        cleaned_text = re.sub("\s+", " ", cleaned_text)
        cleaned_text = cleaned_text.strip().lower()
    return cleaned_text
