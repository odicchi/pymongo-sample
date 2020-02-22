from pymongo import MongoClient

class MongoUpdateSample(object):

    def __init__(self, dbName, collectionName):
        self.client = MongoClient()
        self.db = self.client[dbName]
        self.collection = self.db.get_collection(collectionName)

    def find(self, projection=None,filter=None, sort=None):
        return self.collection.find(projection=projection,filter=filter,sort=sort)

    def update_one(self, filter, update):
        return self.collection.update_one(filter,update)

    def find_one_and_update(self, filter, update):
        return self.collection.find_one_and_update(filter,update)

    def update_many(self, filter, update):
        return self.collection.update_many(filter,update)

    def replace_one(self, filter, replacement):
        return self.collection.replace_one(filter, replacement)

    def find_one_and_replace(self, filter, replacement):
        return self.collection.find_one_and_replace(filter, replacement)

mongo = MongoUpdateSample('test', 'salary')
find = mongo.find()
print('--------------------更新前--------------------')
for doc in find:
    print(doc)

#update = mongo.find_one_and_replace({'fullname':'山田　太郎'},{'name':'山田','salary':500000,'depId':'A0002'})
update = mongo.update_one({'name':'佐藤'},{'$set':{'salary':450000}})
print(type(update))
print(update)
find = mongo.find()
print('--------------------更新後--------------------')
for doc in find:
    print(doc)
