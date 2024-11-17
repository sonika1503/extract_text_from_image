import os

MONGODB_URL = os.getenv("MONGODB_URL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

LABEL_READER_PROMPT = None

def load_label_reader_prompt():
    global LABEL_READER_PROMPT
    if LABEL_READER_PROMPT is None:
        with open('../label_prompt.txt', 'r') as file:
            LABEL_READER_PROMPT = file.read()
