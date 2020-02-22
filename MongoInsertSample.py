from pymongo import MongoClient

class MongoInsertSample(object):

    def __init__(self, dbName, collectionName):
        self.client = MongoClient()
        self.db = self.client[dbName]
        self.collection = self.db.get_collection(collectionName)

    def find(self, projection=None,filter=None, sort=None):
        return self.collection.find(projection=projection,filter=filter,sort=sort)

    def insert_one(self, document):
        return self.collection.insert_one(document)

    def insert_many(self, documents):
        return self.collection.insert_many(documents)

mongo = MongoInsertSample('test', 'salary')
find = mongo.find()
print('--------------------登録前--------------------')
for doc in find:
    print(doc)

info = [{'name':'山田','salary':300000,'depId':'C0002'}]
print('-------------------登録情報-------------------')
result = mongo.insert_many(info)
print(type(result))
print(result)
print(result.inserted_ids)
find = mongo.find()
print('--------------------登録後--------------------')
for doc in find:
    print(doc)
