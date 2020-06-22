from flask import Blueprint
from flask import Flask,request,jsonify
import mongoconfig


create_post_route=Blueprint('create_post_route',__name__)
@create_post_route.route('/createpost',methods=['post'])
def createpost():
    payload=request.json
    email=payload['email']
    title=payload['title']
    content=payload['content']
    cat=payload['category']
    post_dict={}
    post_dict["author"]=email
    post_dict["title"]=title
    post_dict["content"]=content
    post_dict["categories"]=cat
    try:
        db_mongo=mongoconfig.createMongoConnection()
        posts=db_mongo["posts"]
        posts.insert_one(post_dict)
        result=jsonify({"msg":"Post created"})
    except:
        result=jsonify({"error":"Post not created"})
    return result