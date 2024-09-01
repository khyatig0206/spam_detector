import string
from django.conf import settings

from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from joblib import load

VECTORIZER = settings.BASE_DIR /'training'/'tfidf.joblib'
MODEL_FILE = settings.BASE_DIR/'training'/'spam_model.joblib'


knn=load(MODEL_FILE)
tfidf=load(VECTORIZER)

def preprocess(text):
    # Remove punctuation and convert text to lowercase
    text = "".join([t.lower() for t in text if t not in string.punctuation])
    
    # Split the text into tokens (words)
    tokens = text.split()
    
    # Remove stop words and rejoin tokens into a string with spaces between words
    return " ".join(t for t in tokens if t not in ENGLISH_STOP_WORDS)


def predict_spam(comments):
    processed=[preprocess(comment) for comment in comments]

    vectors = tfidf.transform(processed)

    return knn.predict(vectors)
