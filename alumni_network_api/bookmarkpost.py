from flask import Blueprint
from flask import Flask,render_template,request,redirect,url_for,jsonify,session
import mongoconfig
from bson import json_util
import json

addbookmark_post_route=Blueprint('addbookmark_post_route',__name__)
@addbookmark_post_route.route('/addbookmark',methods=['POST'])
def addbookmarkpost():
    payload=request.json
    post=payload['post_id']
    user=payload['user']
    try:
        db_mongo=mongoconfig.createMongoConnection()
        mybookmarks=db_mongo['bookmarks']
        query={"user":user}
        mybookmarks.update(query,{"$push":{"bookmarks":post}},upsert=True)
        result=jsonify({'success':'Bookmark Added'})
    except:
        result=jsonify({'error':'Couldn\'t add to bookmark'})
    return result

removebookmark_post_route=Blueprint('removebookmark_post_route',__name__)
@removebookmark_post_route.route('/removebookmark',methods=['POST'])
def removebookmarkpost():
    payload=request.json
    post=payload['post_id']
    user=payload['user']
    try:
        db_mongo=mongoconfig.createMongoConnection()
        mybookmarks=db_mongo['bookmarks']
        query={"user":user}
        mybookmarks.update(query,{"$pull":{"bookmarks":post}})
        result=jsonify({'success':'Bookmark Removed'})
    except:
        result=jsonify({'error':'Couldn\'t remove bookmark'})
    return result

@removebookmark_post_route.route('/getbookmark',methods=['POST'])
def getmarkpost():
    payload=request.json
    user=payload['user']
    try:
        db_mongo=mongoconfig.createMongoConnection()
        mybookmarks=db_mongo['bookmarks']
        query={"user":user}
        result=json.loads(json_util.dumps(mybookmarks.find_one(query)))
    except:
        result=jsonify({'error':'Couldn\'t remove bookmark'})
    return result