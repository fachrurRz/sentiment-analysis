from preprocess.parsing import *
from preprocess.utils import *
from learning.prepare import *
from learning.train import *
from learning.test import *
from learning.evaluation import *
import pandas as pd
import time
import os
import sys
import json


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
start_time = time.time()

# put your program here
print("--- Loading training data ---")
input_file = open ('reviews_final.json')
json_array = json.load(input_file)
reviews = []

for item in json_array:
    r = Review(item['rid'], item['words'])
    a = item['aspects']
    print(a, type(a[0]))
    r.set_food(a[0])
    r.set_price(a[1])
    r.set_service(a[2])
    r.set_ambiance(a[3])
    print(r.food, r.price, r.service, r.ambiance, '\n')
    reviews.append(r)

matrix = build_from_objects(reviews)

print("--- Starting to train ---")
train_food_reviews(matrix)
train_price_reviews(matrix)
train_ambience_reviews(matrix)
train_service_reviews(matrix)

print("--- Finish training, moving to testing ---")

input_file = open ('tests_final.json')
json_array = json.load(input_file)
testreviews = []

for item in json_array:
    r = Review(item['rid'], item['words'])
    a = item['aspects']
    r.set_food(a[0])
    r.set_price(a[1])
    r.set_service(a[2])
    r.set_ambiance(a[3])
    testreviews.append(r)

pred_matrix = build_from_objects(testreviews, True)

print("--- Finish loading testing data, predicting... ---")

prediction = predict_reviews(pred_matrix)
predicted_df = pd.DataFrame()
predicted_df['rid'] = [r.id for r in testreviews]
predicted_df['FOOD'] = prediction.food_matrix[-2000:]
predicted_df['PRICE'] = prediction.price_matrix[-2000:]
predicted_df['SERVICE'] = prediction.service_matrix[-2000:]
predicted_df['AMBIENCE'] = prediction.ambience_matrix[-2000:]

predicted_df.to_csv('prediction.csv')

print("--- Finish predicting, loading accuracy ---")
f, p, s, a = count_accuracy(prediction, pred_matrix)
print("Food confusion matrix:\n", f)
print("Price confusion matrix:\n", p)
print("Service confusion matrix:\n", s)
print("Ambience confusion matrix:\n", a)

f, p, s, a = count_accuracy_score(prediction, pred_matrix)
print("Food accuracy:\n", f)
print("Price accuracy:\n", p)
print("Service accuracy:\n", s)
print("Ambience accuracy:\n", a)

print("--- %s seconds ---" % (time.time() - start_time))
