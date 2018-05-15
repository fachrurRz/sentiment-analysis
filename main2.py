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

input_file = open ('reviews.json')
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
train_price_reviews(reviews)
train_ambience_reviews(reviews)
train_service_reviews(reviews)


print("--- Finish training, loading testing data ---")

input_file = open ('tests.json')
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
files = open('prediction.txt','w')
files.write(res)
files.close()

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
