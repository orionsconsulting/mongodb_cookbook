import pymongo


def showResults(cursor):
    if cursor.count() != 0:
        for e in cursor:
            print e
    else:
        print 'No documents found'


client = pymongo.MongoClient('localhost', 27017)
db = client.test
postCodes = db.postalCodes.find().limit(10)
showResults(db.pymongoTest.find())

print "Update"
db.pymongoTest.update({'i': {'$gt': 10}}, {'$set': {'gtTen': True}})
{u'updatedExisting': True, u'connectionId': 8, u'ok': 1.0, u'err': None, u'n': 1}
showResults(db.pymongoTest.find())

print "More updates"
print db.pymongoTest.update({'i': {'$gt': 10}}, {'$set': {'gtTen': True}}, multi=True)

print "Update 21"
print db.pymongoTest.update({'i': 21}, {'$set': {'gtTen': True}})

print "Upserting"
print db.pymongoTest.update({'i': 21}, {'$set': {'gtTen': True}}, upsert=True)

print "Deleting"
print db.pymongoTest.remove({'i': 23})
print db.pymongoTest.insert({'i': 23, '_id': 23})

print db.pymongoTest.remove(23)

print "Find and Modify"
print db.pymongoTest.find_and_modify({'i': 20}, {'$set': {'inWords': 'Twenty'}})

print "Find"
print db.pymongoTest.find_one({'i':20})

print "Find and Modify"
print db.pymongoTest.find_and_modify({'i': 19}, {'$set': {'inWords': 'Nineteen'}}, new=True)


cursor = db.postalCodes.find({'state': 'Gujarat'}, {'_id': 0, 'city': 1, 'state': 1, 'pincode': 1}, limit=10,
                             sort=[('city', pymongo.ASCENDING)])
showResults(cursor)

showResults(db.postalCodes.find({'state':'Andhra Pradesh'}, max_scan=50))

print db.pymongoTest.update(spec={'i':{'$gt':10}},document= {'$set':{'gtTen':True}})

print db.pymongoTest.find_and_modify(query={'_id':31}, remove=True)

