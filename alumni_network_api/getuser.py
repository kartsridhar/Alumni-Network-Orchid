from flask import Blueprint
from flask import Flask,request,jsonify
import mongoconfig,sqlconfig
from bson import json_util
import json

get_user_route=Blueprint('get_user_route',__name__)
@get_user_route.route('/getuser',methods=['POST'])
def getuser():
    payload=request.json
    user_email=payload['user_email']
    try:
        user={}
        db=sqlconfig.createConnection()
        get_user_cursor=db.cursor(dictionary=True)
        gtus="SELECT*FROM users WHERE email='{}'".format(user_email)
        get_user_cursor.execute(gtus)
        user.update(get_user_cursor.fetchone())
        get_user_cursor=db.cursor(dictionary=True)
        gtuscat="SELECT cat1,cat2,cat3 FROM user_profiles WHERE email='{}'".format(user_email)
        get_user_cursor.execute(gtuscat)
        categories=get_user_cursor.fetchone()
        user.update(categories)
        result=jsonify(user)
    except:
        result=jsonify({'error':'User Not found'})
    return result