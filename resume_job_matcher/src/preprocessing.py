import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
STOPWORDS = set(stopwords.words('english'))

def clean_text(text):
# 🚨 THIS WILL EXPOSE THE BUG CLEARLY
    if callable(text):
        raise TypeError(
            "clean_text received a FUNCTION/METHOD instead of text. "
            "You forgot parentheses () somewhere."
        )
    
    if not isinstance(text, str):
        text = str(text)
        
    text = text.lower()
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    tokens = text.split()
    tokens = [w for w in tokens if w not in STOPWORDS]
    return " ".join(tokens)


