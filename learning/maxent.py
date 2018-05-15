import nltk
from sklearn.externals import joblib


def prepare_documents(reviews, idx):
    documents = [(review['words'], review['aspects'][idx]) for review in reviews]
    return documents

def get_word_features(reviews):
    ws = []
    for r in reviews:
        for w in r['words']:
            ws.append(w)
    all_words = nltk.FreqDist(ws) 
    word_features = list(all_words.keys())[:2000]
    return word_features

def document_features(document, word_features):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

def train_food_maxent(reviews):
    try:
        me = joblib.load('me_food.pkl')
        if me:
            return me
    except:
        documents = prepare_documents(reviews, 0)

        word_features = get_word_features(reviews)

        featuresets = [(document_features(d, word_features), c) for (d, c) in documents]

        maxent_classifier = nltk.MaxentClassifier.train(featuresets, max_iter=25)

        return maxent_classifier

def train_price_maxent(reviews):
    try:
        me = joblib.load('me_price.pkl')
        if me:
            return me
    except:
        documents = prepare_documents(reviews, 1)

        word_features = get_word_features(reviews)

        featuresets = [(document_features(d, word_features), c) for (d, c) in documents]

        maxent_classifier = nltk.MaxentClassifier.train(featuresets, max_iter=25)

        return maxent_classifier

def train_service_maxent(reviews):
    try:
        me = joblib.load('me_service.pkl')
        if me:
            return me
    except:
        documents = prepare_documents(reviews, 2)

        word_features = get_word_features(reviews)

        featuresets = [(document_features(d, word_features), c) for (d, c) in documents]

        maxent_classifier = nltk.MaxentClassifier.train(featuresets, max_iter=25)

        return maxent_classifier

def train_ambience_maxent(reviews):
    try:
        me = joblib.load('me_ambience.pkl')
        if me:
            return me
    except:
        documents = prepare_documents(reviews, 3)

        word_features = get_word_features(reviews)

        featuresets = [(document_features(d, word_features), c) for (d, c) in documents]

        maxent_classifier = nltk.MaxentClassifier.train(featuresets, max_iter=25)

        return maxent_classifier


def test_maxent(reviews):
    res = []
    for a in ['food', 'price', 'service', 'ambience']:
        res.append(test_aspect(reviews, a))
    return res

def test_aspect(reviews, aspect):
    model = None
    if aspect == 'food':
        model = train_food_maxent(reviews)
    elif aspect == 'price':
        model = train_price_maxent(reviews)
    elif aspect == 'service':
        model = train_service_maxent(reviews)
    else:
        model = train_ambience_maxent(reviews)

    documents = prepare_documents(reviews, d[aspect])

    word_features = get_word_features(reviews)

    featuresets = [(document_features(d, word_features), c) for (d, c) in documents]
    pred = model.classify(featuresets)
    return pred

def count_accuracy_maxent(aspect, reviews):
    d = {
        'food': 0,
        'price': 1,
        'service': 2,
        'ambience': 3
    }
    model = joblib.load('me_{}.pkl'.format(aspect))

    documents = prepare_documents(reviews, d[aspect])

    word_features = get_word_features(reviews)

    featuresets = [(document_features(d, word_features), c) for (d, c) in documents]

    fa = nltk.classify.accuracy(model, featuresets)
    return fa
