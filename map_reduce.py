import bson
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017')
db = client.test
map = bson.Code("function() {emit(this.state, 1)}")
reduce = bson.Code("function(key,values) {return Array.sum(values)}")

db.postalCodes.map_reduce(map=map, reduce=reduce, out="pymr_out")

print "Map Reduce"
c = db.pymr_out.find(sort=[('value', pymongo.DESCENDING)], limit=5)
for elem in c:
    print elem

print "Check on Map Reduce"
c = db.pymr_out.find(sort=[('value', pymongo.DESCENDING)], limit=5)
for elem in c:
    print elem


print "How many states are in Maharashtra"
print db.postalCodes.count({'state': 'Maharashtra'})