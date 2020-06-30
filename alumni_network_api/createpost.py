from flask import Blueprint
from flask import Flask,request,jsonify
import mongoconfig
from bson.objectid import ObjectId


create_post_route=Blueprint('create_post_route',__name__)
@create_post_route.route('/createpost',methods=['post'])
def createpost():
    payload=request.json
    try:
        db_mongo=mongoconfig.createMongoConnection()
        posts=db_mongo["posts"]
        posts.insert_one(payload)
        result="200"
    except:
        result="500"
    return result

@create_post_route.route('/addcomment',methods=['post'])
def addcomment():
    payload=request.json
    query={}
    query["_id"]=ObjectId(payload["post"])
    comment={}
    comment["comment"]=payload["comment"]
    comment["user"]=payload["user"]
    comment["timestamp"]=payload["timestamp"]
    try:
        db_mongo=mongoconfig.createMongoConnection()
        posts=db_mongo["posts"]
        posts.update(query,{'$push':{'comment': comment}})
        result="200"
    except:
        result="500"
    return result