from pymongo import MongoClient
from pymongo import DESCENDING
from pymongo import ASCENDING
from bson.son import SON

class MongoAggregateSample(object):

    def __init__(self, dbName, collectionName):
        self.client = MongoClient()
        self.db = self.client[dbName]
        self.collection = self.db.get_collection(collectionName)

    def find(self, projection=None,filter=None, sort=None):
        return self.collection.find(projection=projection,filter=filter,sort=sort)

    def aggregate(self, pipeline):
        return self.collection.aggregate(pipeline)

mongo = MongoAggregateSample('test','salary')
result1 = mongo.find(filter={'depId':{'$regex':'1$'}})
print(type(result1))
for doc in result1:
    print(doc)

print('sum:')
result = mongo.aggregate([ \
    {'$match':{'depId':{'$regex':'^A'}}}, \
    {'$group':{'_id':"$depId", 'salary_total':{'$sum': "$salary"}}}, \
    {'$sort': SON([('salary_total',DESCENDING)])}])
print(type(result))
for doc in result:
    print(doc)

print('max:')
result = mongo.aggregate([ \
        {'$match':{'depId':{'$regex':'^A'}}}, \
        {'$group':{'_id':"$depId", 'salary_total':{'$max': "$salary"}}}, \
        {'$sort': SON([('salary_total',DESCENDING)])}])
print(type(result))
for doc in result:
    print(doc)

print('min:')
result = mongo.aggregate([ \
        {'$match':{'depId':{'$regex':'^A'}}}, \
        {'$group':{'_id':"$depId", 'salary_total':{'$min': "$salary"}}}, \
        {'$sort': SON([('salary_total',DESCENDING)])}])
print(type(result))
for doc in result:
    print(doc)

print('avg:')
result = mongo.aggregate([ \
        {'$match':{'depId':{'$regex':'^A'}}}, \
        {'$group':{'_id':"$depId", 'salary_total':{'$avg': "$salary"}}}, \
        {'$sort': SON([('salary_total',DESCENDING)])}])
print(type(result))
for doc in result:
    print(doc)

print('複数:')
result = mongo.aggregate([ \
        {'$group':{'_id':"$depId", 'salary_total':{'$sum': "$salary"},'salary_max':{'$max':'$salary'},'salary_avg':{'$avg':'$salary'}}}, \
        {'$sort': SON([('salary_total',DESCENDING)])}])
print(type(result))
for doc in result:
    print(doc)

print('結合:')
result = mongo.aggregate([ \
        {'$lookup':{'from':"department", 'localField':'depId','foreignField':'depId','as':'departmentId'}} \
        ])
print(type(result))
for doc in result:
    print(doc)