from preprocess.parsing import *
from preprocess.utils import *
from learning.prepare import *
from learning.train import *
from learning.test import *
from learning.evaluation import *
from learning.maxent import *
import pandas as pd
import time
import os
import sys
import json


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
start_time = time.time()

print("--- Loading training data ---")

input_file = open ('reviews_final.json')
json_array = json.load(input_file)
reviews = []

for item in json_array:
    r = {"rid":None, "words":None, "aspects":None}
    r['rid'] = item['rid']
    r['words'] = item['words']
    r['aspects'] = item['aspects']
    reviews.append(r)

print("--- Starting to train ---")
train_food_maxent(reviews)
train_price_maxent(reviews)
train_ambience_maxent(reviews)
train_service_maxent(reviews)


print("--- Finish training, loading testing data ---")

input_file = open ('tests_final.json')
json_array = json.load(input_file)
test_reviews = []

for item in json_array:
    r = {"rid":None, "words":None, "aspects":None}
    r['rid'] = item['rid']
    r['words'] = item['words']
    r['aspects'] = item['aspects']
    test_reviews.append(r)

print("Test data len:", len(test_reviews))

print("--- Finish loading testing data, predicting ---")
res = test_maxent(test_reviews)

predicted_df = pd.DataFrame()
predicted_df['rid'] = [t['rid'] for t in test_reviews]
predicted_df['FOOD'] = res[0]
predicted_df['PRICE'] = res[1]
predicted_df['SERVICE'] = res[2]
predicted_df['AMBIENCE'] = res[3]
predicted_df.to_csv('me_prediction.csv')

print("--- Finish predicting, loading accuracy ---")

facc = count_accuracy_maxent('food', test_reviews)
pacc = count_accuracy_maxent('price', test_reviews)
sacc = count_accuracy_maxent('service', test_reviews)
aacc = count_accuracy_maxent('ambience', test_reviews)
print('Food accuracy is:\n ', facc)
print('Price accuracy is:\n ', pacc)
print('Service accuracy is:\n ', sacc)
print('Ambience accuracy is:\n ', aacc)

print("--- %s seconds ---" % (time.time() - start_time))

# put your program here
