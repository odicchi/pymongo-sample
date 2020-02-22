from pymongo import MongoClient
from datetime import datetime

class MongoSample(object):

    def __init__(self, name):
        self.client = MongoClient()
        self.db = self.client[name] #DB名を設定

    def find_one(self):
        return self.db.emploey.find_one()

    def get_collection(self, name):
        return self.db.get_collection(name)

    def collection_names(self):
        return self.db.collection_names()

    def create_collection(self, name):
        return self.db.create_collection(name)

    def list_collection_names(self):
        return self.db.list_collection_names()

mongo = MongoSample('test')
emp = mongo.get_collection('salary')

print(mongo.list_collection_names())

