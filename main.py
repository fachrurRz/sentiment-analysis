from preprocess.parsing import *
from preprocess.utils import *
import time
import os
import sys
import json


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
start_time = time.time()

# put your program
train_features = get_review_text()
print(len(train_features))
with open('tests_final.json', 'w') as f:
    f.write(json.dumps(train_features))
# write_to_csv()

print("--- %s seconds ---" % (time.time() - start_time))
