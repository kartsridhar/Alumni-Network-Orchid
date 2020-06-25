from flask import Blueprint
from flask import Flask,request,jsonify
import mongoconfig

profile_route=Blueprint('profile_route',__name__)
@profile_route.route('/addwork',methods=['POST'])
def addwork():
    payload=request.json
    db_mongo=mongoconfig.createMongoConnection()
    exp=db_mongo['experience']
    try:
        exp.insert_one(payload)
        result="200"
    except:
        result="500"
    return jsonify(result)

@profile_route.route('/addedu',methods=['POST'])
def addedu():
    payload=request.json
    db_mongo=mongoconfig.createMongoConnection()
    edu=db_mongo['education']
    try:
        edu.insert_one(payload)
        result="200"
    except:
        result="500"
    return jsonify(result)

@profile_route.route('/addinterest',methods=['POST'])
def addinterest():
    payload=request.json
    db_mongo=mongoconfig.createMongoConnection()
    intr=db_mongo['interests']
    try:
        intr.insert_one(payload)
        result="200"
    except:
        result="500"
    return jsonify(result)

@profile_route.route('/addbio',methods=['POST'])
def addbio():
    payload=request.json
    db_mongo=mongoconfig.createMongoConnection()
    bio=db_mongo['bio']
    try:
        q={}
        q["email"]=payload["email"]
        if(bio.count_documents(q)==0):
            bio.insert_one(payload)
            result="200"
        else:
            result="500"
    except:
        result="500"
    return jsonify(result)