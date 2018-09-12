import pymongo


def showResults(cursor):
    if cursor.count() != 0:
        for e in cursor:
            print e
    else:
        print 'No documents found'


client = pymongo.MongoClient('mongodb://localhost:27017')
db = client.test


result = db.postCodes.aggregate([
    {'$project': {'state': 1, '_id': 0}},
    {'$group': {'_id': '$state', 'count': {'$sum': 1}}},
    {'$sort': {'count': -1}},
    {'$limit': 5}
  ]
)

