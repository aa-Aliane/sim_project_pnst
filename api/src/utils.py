import re
from langdetect import detect
import fitz

def extract_from_pdf(file_path):
    text = ""

    try:
        

        with fitz.open(file_path) as pdf_document:
            # Iterate through each page
            for page_num in range(pdf_document.page_count):
                # Get the page
                page = pdf_document[page_num]

                # Extract text from the page
                text += page.get_text()

        return text
    except Exception as e:
        print(f"Error extracting text from PDF: {str(e)}")
        return None
    
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
