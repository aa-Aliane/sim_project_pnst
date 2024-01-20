import unicodedata as ud
import re


def tokenize(text: str):

    tokens = []
    token = ""
    for i, ch in enumerate(text):
        category = ud.category(ch)
        match category:
            case "Pf" | "Po":
                if 100 < len(token):
                    tokens.append(token)
                    token = ""
                elif i + 100 >= len(text):
                    break
                token += ch
            case _:
                token += ch
    if i + 100 >= len(text):
        tokens.append(text[i:])

    return tokens




def regex_tokenize(text: str):
    return re.split(r"[.?!:.؟!]", text)




def divide_into_chunks(text, chunk_size=512):
    """
    Divide the input text into chunks of the specified size while ensuring words are not split.

    Parameters:
    - text (str): The input text to be divided.
    - chunk_size (int): The desired size of each chunk.

    Returns:
    - List of strings: Chunks of the input text.
    """
    # words = re.findall(r'\S+\s*', text)
    # chunks = []
    # current_chunk = ""
    # for word in words:
    #     if len(current_chunk) + len(word) <= chunk_size:
    #         current_chunk += word
    #     else:
    #         chunks.append(current_chunk.strip())
    #         current_chunk = word
    # if current_chunk:
    #     chunks.append(current_chunk.strip())
    return text.split("\n")



def load_file(doc_id):
    chunk_size = 512
    with open("src/core/files/"+doc_id+".txt", 'r', encoding="utf8") as f:
        doc = f.read()

    return divide_into_chunks(doc)
