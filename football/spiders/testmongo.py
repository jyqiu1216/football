#!/usr/bin/python3

import pymongo

client = pymongo.MongoClient("mongodb://47.110.134.68:27017", username="admin", password="admin")
db = client['football']
db.authenticate('jyqiu', 'QJY6095956')
collection = db['test']

x = collection.find_one({'name': '2', 'value': 2})
print(type(x))
print(x)
