from preprocess.parsing import *
from preprocess.utils import *
from learning.prepare import *
from learning.train import *
from learning.test import *
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
pred = df.asmatrix()
pred_matrix = build_review_matrix(pred[:,2:-4], pred[:,-4], pred[:,-3], pred[:,-2], pred[:,-1])

print("--- Finish loading testing data, predicting... ---")

prediction = predict_reviews(pred_matrix)
predicted_df = pd.Dataframe()
predicted_df['rid'] = reviews[:,0]
predicted_df['FOOD'] = prediction.food_matrix
predicted_df['SERVICE'] = prediction.service_matrix
predicted_df['AMBIENCE'] = prediction.ambience_matrix
predicted_df['PRICE'] = prediction.price_matrix
predicted_df.to_csv('prediction.csv')

print("--- %s seconds ---" % (time.time() - start_time))
