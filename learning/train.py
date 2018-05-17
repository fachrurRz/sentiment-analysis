from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.externals import joblib

train_features = None
vect = None
vocab = None

def vectorize(review_matrix):
    global train_features
    global vect
    global vocab
    vector = CountVectorizer()
    if train_features is not None:
        return train_features
    train = vector.fit_transform(review_matrix.text_matrix)
    vect = vector
    vocab = list(vect.vocabulary_.keys())
    train_features = train
    return train_features

def get_vocabulary():
    return vocab

def get_vectorizer():
    return vect

def train_food_reviews(review_matrix):
    try:
        nb = joblib.load('food.pkl')
        
        if nb:
            return nb
    except:
        nb = MultinomialNB(alpha=1)
        features = vectorize(review_matrix)
        # features = review_matrix.text_matrix
        nb.fit(features, review_matrix.food_matrix)
        # print(review_matrix.food_matrix)
        joblib.dump(nb, 'food.pkl')
        return nb

def train_price_reviews(review_matrix):
    try:
        nb = joblib.load('price.pkl')
        
        if nb:
            return nb
    except:
        nb = MultinomialNB(alpha=1)
        features = vectorize(review_matrix)
        # features = review_matrix.text_matrix
        nb.fit(features, review_matrix.price_matrix)
        joblib.dump(nb, 'price.pkl')
        return nb

def train_service_reviews(review_matrix):
    try:
        nb = joblib.load('service.pkl')
        
        if nb:
            return nb
    except:
        nb = MultinomialNB(alpha=1)
        features = vectorize(review_matrix)
        # features = review_matrix.text_matrix
        nb.fit(features, review_matrix.service_matrix)
        joblib.dump(nb, 'service.pkl')
        return nb

def train_ambience_reviews(review_matrix):
    try:
        nb = joblib.load('ambience.pkl')
        
        if nb:
            return nb
    except:
        nb = MultinomialNB(alpha=1)
        features = vectorize(review_matrix)
        # features = review_matrix.text_matrix
        nb.fit(features, review_matrix.ambience_matrix)
        joblib.dump(nb, 'ambience.pkl')
        return nb
