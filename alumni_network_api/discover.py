from flask import Blueprint
from flask import Flask,request,jsonify
import mongoconfig
from bson.objectid import ObjectId
from bson import json_util
import json

get_category_route=Blueprint('get_category_route',__name__)
@get_category_route.route('/getcategories',methods=['GET'])
def getcategories():
    db_mongo=mongoconfig.createMongoConnection()
    categories=db_mongo['categories']
    results=[]
    for x in json.loads(json_util.dumps(categories.find())):
        results.append(x)
    return jsonify(results)

@get_category_route.route('/getchildcategories',methods=['POST'])
def getchildcategories():
    payload=request.json
    db_mongo=mongoconfig.createMongoConnection()
    categories=db_mongo['childcategories']
    results=[]
    for x in json.loads(json_util.dumps(categories.find(payload))):
        results.append(x)
    return jsonify(results)

@get_category_route.route('/getgrandchildcategories',methods=['POST'])
def getgrandchildcategories():
    payload=request.json
    db_mongo=mongoconfig.createMongoConnection()
    categories=db_mongo['grandchildcategories']
    results=[]
    for x in json.loads(json_util.dumps(categories.find(payload))):
        results.append(x)
    return jsonify(results)

@get_category_route.route('/getcategorypost',methods=['POST'])
def getcategorypost():
    payload=request.json
    print(payload)
    category=payload['cat']
    db_mongo=mongoconfig.createMongoConnection()
    post_collection=db_mongo['posts']
    allposts=[]
    for j in post_collection.find({"tags": category}).sort("timestamp",-1):
        if json.loads(json_util.dumps(j)) not in allposts:
            allposts.append(json.loads(json_util.dumps(j)))
    return jsonify(allposts)

@get_category_route.route('/getinterest',methods=['POST'])
def getinterest():
    payload=request.json
    db_mongo=mongoconfig.createMongoConnection()
    interests=db_mongo['interests']
    x=interests.find_one(payload)['interest']
    return jsonify(x)

@get_category_route.route('/addinterest',methods=['POST'])
def addinterest():
    payload=request.json
    db_mongo=mongoconfig.createMongoConnection()
    interests=db_mongo['interests']
    query={"user":payload['user']}
    try:
        interests.update(query,{"$push":{"interest":payload['interest']}})
        result="200"
    except:
        result="500"
    return jsonify(result)

@get_category_route.route('/removeinterest',methods=['POST'])
def removeinterest():
    payload=request.json
    db_mongo=mongoconfig.createMongoConnection()
    interests=db_mongo['interests']
    query={"user":payload['user']}
    try:
        interests.update(query,{"$pull":{"interest":payload['interest']}})
        result="200"
    except:
        result="500"
    return jsonify(result)