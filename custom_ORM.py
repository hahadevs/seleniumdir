import pymongo

import pandas as pd

dataframe = pd.read_csv('csvdir/indus.csv')

config_url = open('mongo.conf','r').read()
conn = pymongo.MongoClient(config_url)
db = conn['SCRAP_DB']
collection = db['homes_collection']

for i in range(len(dataframe)):
    print("Inserting : ",dataframe['url'][i])
    collection.insert_one({
        "url":dataframe['url'][i],
        "price":dataframe['price'][i],
        "location":dataframe['location'][i],
        "amenities":dataframe['amenities'][i]
    })



