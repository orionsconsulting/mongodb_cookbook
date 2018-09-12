import pymongo

client =  pymongo.MongoClient('localhost', 27017)
db = client.test
postCodes = db.postalCodes.find().limit(10)

print "10 Post Codes"
for postCode in postCodes:
    print 'City: ', postCode['city'], ', State: ', postCode['state'], ', Pin Code: ', postCode['pincode']

print "One Postal Code"
postCode = db.postalCodes.find_one()
print 'City: ', postCode['city'], ', State: ', postCode['state'], ', Pin Code: ', postCode['pincode']

print "Ascending CityTop 10 Cities in Gujarat"
cursor = db.postalCodes.find({'state': 'Gujarat'}, {'_id': 0, 'city': 1, 'state': 1, 'pincode':1}).sort('city',
        pymongo.ASCENDING).limit(10)
for postCode in cursor:
    print 'City: ', postCode['city'], ', State: ', postCode['state'], ', Pin Code: ', postCode['pincode']

print "Sorted Data"
city = db.postalCodes.find().sort([('state', pymongo.DESCENDING), ('city', pymongo.ASCENDING)]).limit(5)
for postCode in city:
    print 'City: ', postCode['city'], ', State: ', postCode['state'], ', Pin Code: ', postCode['pincode']


for i in range(1, 21):
    db.pymongoTest.insert({'i': i})

db.pythonTest.insert([{'name': 'John'}, {'name': 'Mark'}])
db.pymongoTest.insert({'name': 'Jones'}, w=1, j=True)
