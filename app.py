from pymongo import MongoClient



url = 'mongodb://localhost:27017/test'

client = MongoClient(url)
db=client.test
collection = db.testData

# tempD = collection.find_One({"Rajat" : "Music Right Here"})
print(collection.find())

# x = collection.find({"Song": "1"})
# print(x)
# temp = db.findOne({'Rajat' : 'Music Right Here'})


# print(temp)
# print('hi')




print('Helllo World')