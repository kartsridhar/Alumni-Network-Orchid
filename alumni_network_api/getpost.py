from flask import Blueprint
from flask import Flask,request,jsonify
import mongoconfig
from bson import json_util
import json


get_post_route=Blueprint('get_post_route',__name__)
@get_post_route.route('/getpost',methods=['POST'])
def getpost():
    payload=request.json
    user=payload['user']
    db_mongo=mongoconfig.createMongoConnection()
    interests=db_mongo['interests'].find_one({"user": user})['interest']
    post_collection=db_mongo['posts']
    allposts=[]
    for i in interests:
        for j in post_collection.find({"tags": i}).sort("timestamp",-1):
            if json.loads(json_util.dumps(j)) not in allposts:
                allposts.append(json.loads(json_util.dumps(j)))
    return jsonify(allposts)

@get_post_route.route('/getpostcount',methods=['POST'])
def getpostcount():
    payload=request.json
    user=payload['user']
    db_mongo=mongoconfig.createMongoConnection()
    interests=db_mongo['interests'].find_one({"user": user})['interest']
    post_collection=db_mongo['posts']
    allposts=[]
    count=0
    for i in interests:
        for j in post_collection.find({"tags": i}).sort("timestamp",-1):
            if json.loads(json_util.dumps(j)) not in allposts:
                allposts.append(json.loads(json_util.dumps(j)))
                count+=1
    return jsonify(count)