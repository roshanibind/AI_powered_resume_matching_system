from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_match_score(resume, job):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume, job])
    score = cosine_similarity(vectors[0:1], vectors[1:2])
    return round(score[0][0]*100 , 2)