from flask import Blueprint
from flask import Flask,request,jsonify
import mongoconfig


delete_post_route=Blueprint('delete_post_route',__name__)
@delete_post_route.route('/deletepost',methods=['post'])
def deletepost():
    payload=request.json
    email=payload['email']
    title=payload['title']
    post_dict={}
    post_dict["author"]=email
    post_dict["title"]=title
    try:
        db_mongo=mongoconfig.createMongoConnection()
        posts=db_mongo["posts"]
        posts.delete_one(post_dict)
        result=jsonify({"msg":"Post deleted "})
    except:
        result=jsonify({"error":"Post not Deleted"})
    return result