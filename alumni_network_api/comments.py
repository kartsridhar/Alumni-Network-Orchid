from flask import Blueprint
from flask import Flask,request,jsonify
import mongoconfig
from bson.objectid import ObjectId
from bson import json_util
import json


add_comment_route=Blueprint('add_comment_route',__name__)
@add_comment_route.route('/addcomment',methods=['POST'])
def addcomment():
    payload=request.json
    comment={}
    comment['post_id']=payload['post_id']
    comment['user']=payload['email']
    comment['body']=payload['body']
    try:
        db_mongo=mongoconfig.createMongoConnection()
        comments=db_mongo['comments']
        comments.insert_one(comment)
        result=jsonify({'success':'Comment Added'})
    except:
        result=jsonify({'error':'Couldn\'t add the comment'})
    return result

delete_comment_route=Blueprint('delete_comment_route',__name__)
@delete_comment_route.route('/deletecomment',methods=['POST'])
def deletecomment():
    payload=request.json
    comment={}
    comment['_id']=ObjectId(payload['comment_id'])
    try:
        db_mongo=mongoconfig.createMongoConnection()
        comments=db_mongo['comments']
        comments.delete_one(comment)
        result=jsonify({'success':'Comment deleted'})
    except:
        result=jsonify({'error':'Couldn\'t delete the comment'})
    return result

update_comment_route=Blueprint('update_comment_route',__name__)
@update_comment_route.route('/updatecomment',methods=['POST'])
def updatecomment():
    payload=request.json
    comment={}
    comment['_id']=ObjectId(payload['comment_id'])
    updatecomment={ "$set": { "body": str(payload['body']) } }
    try:
        db_mongo=mongoconfig.createMongoConnection()
        comments=db_mongo['comments']
        comments.update_one(comment,updatecomment)
        result=jsonify({'success':'Comment updated'})
    except:
        result=jsonify({'error':'Couldn\'t update the comment'})
    return result

get_comment_route=Blueprint('get_comment_route',__name__)
@get_comment_route.route('/getcomment',methods=['POST'])
def getcomment():
    payload=request.json
    comment={}
    comment['post_id']=(payload['post_id'])
    try:
        db_mongo=mongoconfig.createMongoConnection()
        comments=db_mongo['comments']
        for i in comments.find(comment):
            print(i)
        result=jsonify(json.loads(json_util.dumps(comments.find(comment))))
    except:
        result=jsonify({'error':'Couldn\'t update the comment'})
    return result