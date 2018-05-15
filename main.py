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
df = pd.read_csv('train.csv')
reviews = df.as_matrix()
matrix = build_review_matrix(reviews[:,2:-4], reviews[:,-4], reviews[:,-3], reviews[:,-2], reviews[:,-1])

print("--- Starting to train ---")
train_food_reviews(matrix)
train_price_reviews(matrix)
train_ambience_reviews(matrix)
train_service_reviews(matrix)

print("--- Finish training, moving to testing ---")

df = pd.read_csv('test.csv')
pred = df.as_matrix()
pred_matrix = build_review_matrix(pred[:,2:-4], pred[:,-4], pred[:,-3], pred[:,-2], pred[:,-1], True)

print("--- Finish loading testing data, predicting... ---")

prediction = predict_reviews(pred_matrix)
predicted_df = pd.DataFrame()
predicted_df['rid'] = pred[:,0]
predicted_df['FOOD'] = prediction.food_matrix
predicted_df['SERVICE'] = prediction.service_matrix
predicted_df['AMBIENCE'] = prediction.ambience_matrix
predicted_df['PRICE'] = prediction.price_matrix
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
