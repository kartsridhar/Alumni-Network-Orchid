from flask import Blueprint
from flask import Flask,render_template,request,redirect,url_for,jsonify,session
import mongoconfig


addbookmark_post_route=Blueprint('addbookmark_post_route',__name__)
@addbookmark_post_route.route('/addbookmark',methods=['POST'])
def addbookmarkpost():
    payload=request.json
    bookmark={}
    bookmark["bk_id"]=payload['post_id']
    bookmark["user"]=payload['email']
    try:
        db_mongo=mongoconfig.createMongoConnection()
        mybookmarks=db_mongo['bookmarks']
        mybookmarks.insert_one(bookmark)
        result=jsonify({'success':'Bookmark Added'})
        db_mongo.close()
    except:
        result=jsonify({'error':'Couldn\'t add to bookmark'})
    return result

removebookmark_post_route=Blueprint('removebookmark_post_route',__name__)
@removebookmark_post_route.route('/removebookmark',methods=['POST'])
def removebookmarkpost():
    payload=request.json
    bookmark={}
    bookmark["bk_id"]=payload['post_id']
    bookmark["user"]=payload['email']
    try:
        db_mongo=mongoconfig.createMongoConnection()
        mybookmarks=db_mongo['bookmarks']
        mybookmarks.delete_one(bookmark)
        result=jsonify({'success':'Bookmark Removed'})
        db_mongo.close()
    except:
        result=jsonify({'error':'Couldn\'t remove bookmark'})
    return result