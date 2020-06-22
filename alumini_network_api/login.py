from flask import Blueprint,jsonify,request 
from sqlconfig import createConnection
from flask_jwt_extended import create_access_token

login_route=Blueprint('login_route',__name__)
@login_route.route('/login', methods=['POST'])
def login():
    payload=request.json
    #user email via form 
    ue=payload['email']
    #user password via form
    up=payload['password']
    try:
        db=createConnection()
        login_cursor=db.cursor(dictionary=True)
        ftc="SELECT * FROM users WHERE email='{}' AND password='{}'".format(ue,up)
        login_cursor.execute(ftc)
        rows=login_cursor.fetchone()
        result= create_access_token( identity={'full_name': rows['full_name'],'email': rows['email'],'user_name': rows['user_name']})
        login_cursor.close()
        db.close()	
    except:
        result=jsonify({"error": "Invalid Credentials"})
    return result
