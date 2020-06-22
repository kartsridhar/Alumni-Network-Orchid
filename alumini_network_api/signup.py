from flask import Blueprint,jsonify,request
from sqlconfig import createConnection
from flask_jwt_extended import create_access_token
import random

signup_route=Blueprint('signup_route',__name__)
@signup_route.route('/signup', methods=['POST'])
def signup():
    payload=request.json
    #user email via form
    ue=payload['email']
    #user password via form
    up=payload['password']
    #user full name via form
    fn=payload['full_name']
    #user name via form
    un=payload['user_name']
    #user initial conformation status
    uc="0"
    #user conformation code
    ucon=str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))
    try:
        db=createConnection()
        signup_cursor=db.cursor(dictionary=True)
        crt="INSERT INTO users VALUES ('{}','{}','{}','{}','{}','{}')".format(ue,up,fn,un,uc,ucon)
        signup_cursor.execute(crt)
        db.commit()
        signup_cursor.close()
        db.close
        access_token= create_access_token( identity={'confirmation_code': ucon,'email': ue,'full_name':fn,'user_name':un,'confirmation_status':uc})
        result=access_token
    except:
        result=jsonify({"erorr":"Could not SignUp Email already Exists"})
    return result
