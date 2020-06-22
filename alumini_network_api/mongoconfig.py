import pymongo
def createMongoConnection():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    return myclient["user_data"]