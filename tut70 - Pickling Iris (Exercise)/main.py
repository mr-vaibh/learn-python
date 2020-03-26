
# pickle
# Use requests module to download the iris dataset

import requests
import pickle

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
response = requests.get(url)

data = response.text

List =[item.split(",") for item in data.split("\n") if len(item)!=0]

with open('irisData.pkl', 'wt+') as file:
    pickle.dump(List, file)