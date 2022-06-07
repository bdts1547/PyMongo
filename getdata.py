import pymongo
from pymongo import MongoClient
import argparse


def getConfig():
    parser = argparse.ArgumentParser()
    # parser.add_argument('--folder', type=str, default="", help='Link download')
    parser.add_argument('--key', default="", type=str, help='Key object need search')
    parser.add_argument('--value', type=int, default=0, help='Value object need search')
    # parser.add_argument('--condition', type=dict, default='')

    args = parser.parse_args()
    return args

# Configuration
args = getConfig()



cluster = MongoClient("mongodb+srv://bdts1547:bdts1547@cluster0.b4zod.mongodb.net/?retryWrites=true&w=majority")
db = cluster["Test"]    # Database
collection = db["test1"] # Collection


objects = collection.find({args.key: args.value})
for obj in objects:
    print(obj)


