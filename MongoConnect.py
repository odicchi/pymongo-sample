from pymongo import MongoClient

client1 = MongoClient()
client2 = MongoClient('localhost', 27017)
client3 = MongoClient('mongodb://localhost:27017')