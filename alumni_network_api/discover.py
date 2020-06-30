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