from pymongo import MongoClient

class MongoDeleteSample(object):
    
    def __init__(self, dbName, collectionName):
        self.client = MongoClient()
        self.db = self.client[dbName]
        self.collection = self.db.get_collection(collectionName)

    def find(self, projection=None,filter=None, sort=None):
        return self.collection.find(projection=projection,filter=filter,sort=sort)

    def delete_one(self, filter):
        return self.collection.delete_one(filter)

    def delete_many(self, filter):
        return self.collection.delete_many(filter)

    def find_one_and_delete(self, filter):
        return self.collection.find_one_delete(filter)

mongo = MongoDeleteSample('test', 'salary')
print('--------------------削除前--------------------')
find = mongo.find()
for doc in find:
    print(doc)

print('-------------------削除情報-------------------')
result = mongo.delete_many({'name':'山田'})
print(type(result))
print(result)
print(result.deleted_count)

print('--------------------削除後--------------------')
find = mongo.find()
for doc in find:
    print(doc)
