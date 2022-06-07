import pymongo
from pymongo import MongoClient
import urllib.request
import requests
import argparse
import os
import json

# Config Args
def getConfig():
    parser = argparse.ArgumentParser()
    parser.add_argument('--folder', type=str, default="", help='Link download')
    parser.add_argument('--key', default=0, type=str, help='Key object')
    parser.add_argument('--value', type=str, default="", help='Value object')
    parser.add_argument('--condition', type=dict, default='')

    args = parser.parse_args()
    return args

# Configuration
args = getConfig()



list_files = os.listdir(args.folder)
list_objects = []
for filename in list_files:
    if filename.split('.')[-1] == 'json':
        with open(os.path.join(args.folder, filename)) as f:
            file_data = json.load(f)
            list_objects.append(file_data)
            print(file_data)

cluster = MongoClient("mongodb+srv://bdts1547:bdts1547@cluster0.b4zod.mongodb.net/?retryWrites=true&w=majority")
db = cluster["Test"]  # Name database
collection = db["test1"] # Name collection

for item in list_objects:
    collection.insert_one(item)




