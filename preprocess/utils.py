from nltk.corpus import wordnet
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from preprocess.parsing import get_reviews
from langdetect import detect
import json


def get_bad_words(reviews):
    json_data = open('english_id.json').read()

    data = json.loads(json_data)
    indonesian_words = set()
    with open('indonesian-wordlist.txt', 'r') as f:
        for word in f:
            indonesian_words.add(word.strip('\n'))
    # reviews = get_reviews()
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    non_formal_words = set()
    count = 0
    print(len(reviews))
    for review in reviews:
        count += 1
        print(count)
        if review.id not in data:
            continue
        stemmed = stemmer.stem(review.text)
        words = stemmed.split(' ')

        for word in words:
            if word not in indonesian_words:
                non_formal_words.add(word)

    return non_formal_words


def get_english_review_id(reviews):
    english_review_ids = []

    # reviews = get_reviews()
    for review in reviews:
        try:
            lang = detect(review.text)
        except Exception:
            print(review.text)
            lang = 'en'
        if lang == 'en':
            english_review_ids.append(review.id)

    return english_review_ids


def get_indo_bad_words():
    json_data = open('bad_words.json').read()

    bad_words = json.loads(json_data)
    print(len(bad_words))
    indo_bad_words = []
    for bad_word in bad_words:
        if wordnet.synsets(bad_word):
            continue
        indo_bad_words.append(bad_word)

    print(len(indo_bad_words))
    return indo_bad_words
