from flask import Blueprint
from flask import Flask,request,jsonify
import mongoconfig,sqlconfig
from bson import json_util
import json


get_post_route=Blueprint('get_post_route',__name__)
@get_post_route.route('/getpost',methods=['POST'])
def getpost():
    payload=request.json
    email=payload['email']
    get_cat="SELECT cat1,cat2,cat3 FROM user_profiles WHERE email='{}'".format(email)
    db_sql=sqlconfig.createConnection()
    get_category_cursor=db_sql.cursor(dictionary=True)
    get_category_cursor.execute(get_cat)
    categories= (get_category_cursor.fetchone())
    db_mongo=mongoconfig.createMongoConnection()
    post_collection=db_mongo['posts']
    allposts=[]
    for i in categories:
        for j in post_collection.find({"categories": categories[i]}):
            allposts.append(json.loads(json_util.dumps(j)))        
    return jsonify(allposts)