from pymongo import MongoClient
from pymongo import DESCENDING
from pymongo import ASCENDING
from matplotlib import pyplot

class MongoFindSample(object):

    def __init__(self, dbName, collectionName):
        self.client = MongoClient()
        self.db = self.client[dbName]
        self.collection = self.db.get_collection(collectionName)

    def find_one(self, projection=None,filter=None, sort=None):
        return self.collection.find_one(projection=projection,filter=filter,sort=sort)

    def find(self, projection=None,filter=None, sort=None):
        return self.collection.find(projection=projection,filter=filter,sort=sort)

    def count_documents(self, filter=None):
        return self.collection.count_documents(filter)


mongo = MongoFindSample('test', 'salary')
findOne = mongo.find_one()
print('-----------------find_One-----------------')
print(type(findOne))
print(findOne)

find = mongo.find()
print('-------------------find-------------------')
# print(type(find))
# for i in range(find.count()):
#     print(find[i])                                                                                                                                                                                                                                                                                                           
try:
    doc = find.next()
    while doc != None:
        print(doc)
        doc = find.next()
except StopIteration:
    pass

print('-------------------前方一致-------------------')
result1 = mongo.find(filter={'depId':{'$regex':'^A'}})
print(type(result1))
for doc in result1:
    print(doc)

print('-------------------後方一致-------------------')
result1 = mongo.find(filter={'depId':{'$regex':'2$'}})
print(type(result1))
for doc in result1:
    print(doc)

print('-------------------含む-------------------')
result1 = mongo.find(filter={'name':{'$regex':'田'}})
print(type(result1))
for doc in result1:
    print(doc)

print('-------------------以上-------------------')
result1 = mongo.find(filter={'salary':{'$gte':300000,'$lte':400000}})
print(type(result1))
for doc in result1:
    print(doc)

print('-------------------かつ-------------------')
result1 = mongo.find(filter={'$and':[{'name':'山田'},{'depId':'C0002'}]})
print(type(result1))
for doc in result1:
    print(doc)

print('-------------------または-------------------')
result1 = mongo.find(filter={'$or':[{'name':'山田'},{'depId':'B0001'}]})
print(type(result1))
for doc in result1:
    print(doc)

result1 = mongo.find(filter={'$and':[{'salary':{'$gte':300000}},{'salary':{'$lte':400000}}]})
print(type(result1))
for doc in result1:
    print(doc)
# print('-------------------find-------------------')
# #find = mongo.find(filter={'name':'山田','salary':{'$gte':400000}})
# #find = mongo.find(projection={'_id':0, 'name':1, 'salary':1},sort=[('salary',DESCENDING),('name',ASCENDING)])
# find = mongo.find()
# y = []
# data = []
# for doc in find.sort([('salary',DESCENDING),('name',ASCENDING)]):
#     print(doc)
#     y += [doc['salary']]
#     data += [doc['name']]

# x = range(len(y))
# print(y)
# print(data)
# pyplot.bar(x, y, tick_label=data)
# pyplot.show()
