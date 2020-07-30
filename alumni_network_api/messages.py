from flask import Blueprint
from flask import Flask,request,jsonify
import mongoconfig
from bson.objectid import ObjectId
from bson import json_util
import json

messages_route=Blueprint('messages_route',__name__)
@messages_route.route('/getconvo',methods=['POST'])
def getconvo():
    payload=request.json
    q1={}
    q2={}
    q1["user1"]=payload["user"]
    q2["user2"]=payload["user"]
    db_mongo=mongoconfig.createMongoConnection()
    convos=db_mongo['conversations']
    results=[]
    for x in json.loads(json_util.dumps(convos.find({'$or':[q1,q2]}))):
        results.append(x)
    return jsonify(results)

@messages_route.route('/startconvo',methods=['POST'])
def startconvo():
    payload=request.json
    db_mongo=mongoconfig.createMongoConnection()
    convos=db_mongo['conversations']
    q={}
    q['user1']=payload['user1']
    q['user2']=payload['user2']
    q1={}
    q1['user2']=payload['user1']
    q1['user1']=payload['user2']
    c=convos.count({"$or":[q1,q]})
    if(c<1):
        convos.insert_one(payload)
        result="200"
    else:
        result="500"
    return result

@messages_route.route('/sendmessage',methods=['POST'])
def sendmessage():
    payload=request.json
    db_mongo=mongoconfig.createMongoConnection()
    msg=db_mongo['messages']
    msg.insert_one(payload)
    return "200"

@messages_route.route('/getmessages',methods=['POST'])
def getmessages():
    payload=request.json
    q1={}
    q1['from']=payload["user1"]
    q1['to']=payload["user2"]
    q2={}
    q2['from']=payload["user2"]
    q2['to']=payload["user1"]
    db_mongo=mongoconfig.createMongoConnection()
    msg=db_mongo['messages']
    results=[]
    r=msg.find({'$or':[q1,q2]}).sort('timestamp',-1).limit(15)
    r=json.loads(json_util.dumps(r))
    r.reverse()
    for x in r:
        results.append(x)
    return jsonify(results)