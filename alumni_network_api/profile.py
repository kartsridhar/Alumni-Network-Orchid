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

@profile_route.route('/getwork',methods=['POST'])
def getwork():
    payload = request.json
    user = payload["user"]
    db_mongo = mongoconfig.createMongoConnection()
    exp = db_mongo['experience']
    documents = list(exp.find({"user" : user}))
    
    companies = []
    durations = []
    positions = []

    for i in range(len(documents)):
        companies.append(documents[i]["place"])
        positions.append(documents[i]["position"])
        duration = str(documents[i]["start"]) + " to " + str(documents[i]["end"])
        durations.append(duration)

    result = {
        "companies" : companies,
        "durations" : durations,
        "positions" : positions
    }

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

@profile_route.route('/getinterest',methods=['POST'])
def getinterest():
    user = request.json["user"]
    db_mongo = mongoconfig.createMongoConnection()
    interests = db_mongo['interests'].find_one({"user" : user})['interest']
    return jsonify(interests)

@profile_route.route('/editinterest',methods=['POST'])
def editinterest():
    payload = request.json
    user = payload["user"]
    interest = payload["interest"]
    db_mongo = mongoconfig.createMongoConnection()
    db_mongo['interests'].find_one_and_update({"user" : user}, {"$set" : {"interest" : interest}})
    return jsonify(interest)

@profile_route.route('/addbio',methods=['POST'])
def addbio():
    payload=request.json
    db_mongo=mongoconfig.createMongoConnection()
    bio=db_mongo['bio']
    try:
        q={}
        q["user"]=payload["user"]
        if(bio.count_documents(q)==0):
            bio.insert_one(payload)
            result="200"
        else:
            result="500"
    except:
        result="500"
    return jsonify(result)

@profile_route.route('/getbio',methods=['POST'])
def getbio():
    user = request.json["user"]
    db_mongo = mongoconfig.createMongoConnection()
    bio = db_mongo['bio'].find_one({"user" : user})['bio']
    return jsonify(bio)

@profile_route.route('/editbio',methods=['POST'])
def editbio():
    payload = request.json
    user = payload["user"]
    bio = payload["bio"]
    db_mongo = mongoconfig.createMongoConnection()
    db_mongo['bio'].find_one_and_update({"user" : user}, {"$set" : {"bio" : bio}})
    return jsonify(bio)