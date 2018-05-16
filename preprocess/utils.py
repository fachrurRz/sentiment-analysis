from nltk.corpus import wordnet
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from preprocess.parsing import get_reviews
from langdetect import detect
import json
from preprocess.abbreviation import (
    abbrevIndo,
    abbrevEng
)
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import csv


def get_bad_words():
    json_data = open('english_id.json').read()

    data = json.loads(json_data)
    indonesian_words = set()
    with open('indonesian-wordlist.txt', 'r') as f:
        for word in f:
            indonesian_words.add(word.strip('\n'))
    reviews = get_reviews("test.xml")
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


def get_english_review_id():
    english_review_ids = []

    reviews = get_reviews("test.xml")
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


def get_all_distinct_words():
    reviews_train = get_reviews("train.xml")
    reviews = reviews_train
    json_data = open('english_id.json').read()

    english_id = json.loads(json_data)

    fix_words = set()
    counter = 0
    total = len(reviews)
    for review in reviews:
        print(str(counter) + '/' + str(total))
        counter += 1
        id = review.id
        if id in english_id:
            ps = PorterStemmer()
            sentence = review.text
            words = word_tokenize(sentence)
            for word in words:
                word = ps.stem(word)
                if word in abbrevEng:
                    t_word = abbrevEng[word]
                    fix_words.add(t_word)
                else:
                    fix_words.add(word)

        else:
            factory = StemmerFactory()
            stemmer = factory.create_stemmer()

            kalimat = review.text
            katadasar = stemmer.stem(kalimat)
            katadasar = katadasar.split(' ')

            for kata in katadasar:
                if kata in abbrevIndo:
                    t_kata = abbrevIndo[kata]
                    fix_words.add(t_kata)
                else:
                    fix_words.add(kata)

    return list(fix_words)


def get_review_text():
    reviews = get_reviews("dataset_test.xml")
    json_data = open('english_id.json').read()

    english_id = json.loads(json_data)

    counter = 0
    total = len(reviews)
    data = {}
    for review in reviews:
        aspects = review.get_aspects()
        print(str(counter) + '/' + str(total))
        counter += 1
        id = review.id
        data[id] = {}
        data[id]['aspects'] = aspects
        if id in english_id:
            ps = PorterStemmer()
            sentence = review.text
            words = word_tokenize(sentence)
            fix_words = set()
            for word in words:
                word = ps.stem(word)
                if word in abbrevEng:
                    t_word = abbrevEng[word]
                    fix_words.add(t_word)
                else:
                    fix_words.add(word)
            data[id]['words'] = list(fix_words)

        else:
            factory = StemmerFactory()
            stemmer = factory.create_stemmer()

            kalimat = review.text
            katadasar = stemmer.stem(kalimat)
            katadasar = katadasar.split(' ')

            fix_words_id = set()
            for kata in katadasar:
                if kata in abbrevIndo:
                    t_kata = abbrevIndo[kata]
                    fix_words_id.add(t_kata)
                else:
                    fix_words_id.add(kata)
            data[id]['words'] = list(fix_words_id)

    return data


def remove_stop_words():
    json_data = open('reviews.json').read()

    reviews = json.loads(json_data)

    indonesian_stopwords = set()
    with open('indonesia_stopwords.txt', 'r') as f:
        for word in f:
            indonesian_stopwords.add(word.strip('\n'))

    stop_words = set(stopwords.words('english'))

    data = []
    for review in reviews:
        words = review['words']
        w = []
        for word in words:
            if (word not in stop_words) and (word not in indonesian_stopwords):
                w.append(word)

        r = {'rid': review['rid'], 'words': w, 'aspects': review['aspects']}
        data.append(r)
    return data

def write_to_csv():
    train_reviews_json = open('test_reviews.json').read()
    train_features_json = open('train_features.json').read()

    train_reviews = json.loads(train_reviews_json)
    train_features = json.loads(train_features_json)

    train_aspects = ['food_aspect', 'price_aspect', 'service_aspect', 'ambience_aspect']
    with open('test.csv', 'w') as csvfile:
        fieldnames = ['rid'] + train_features + train_aspects
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        train_features = set(train_features)

        counter = 0
        total = len(train_reviews)
        for rid in train_reviews:
            print(str(counter) + '/' + str(total))
            counter += 1
            row = {'rid': -1}
            for feature in train_features:
                row[feature] = 0

            for aspect in train_aspects:
                row[aspect] = 0
            review = train_reviews[rid]
            words = review['words']
            aspects = review['aspects']
            row['rid'] = rid
            for word in words:
                if word in train_features:
                    count = words.count(word)
                    row[word] = count
            row['food_aspect'] = aspects[0]
            row['price_aspect'] = aspects[1]
            row['service_aspect'] = aspects[2]
            row['ambience_aspect'] = aspects[3]
            writer.writerow(row)


def parse_review_to_list():
    json_data = open('test_reviews.json').read()

    train_reviews = json.loads(json_data)

    reviews = []
    for rid in train_reviews:
        review = train_reviews[rid]
        review['rid'] = rid
        reviews.append(review)

    return reviews
