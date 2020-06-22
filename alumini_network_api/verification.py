from flask import Blueprint,jsonify,request
from sqlconfig import createConnection

verification_route=Blueprint('verification_route',__name__)
@verification_route.route('/verify',methods=['post'])
def verify():
    payload=request.json
    #email 
    ue=payload['email']
    #conformation code
    ucon=payload['confirmation_code']
    db=createConnection()
    conf="SELECT * FROM users WHERE email='{}' AND confirmation_code='{}'".format(ue,ucon)
    verification_route_cursor=db.cursor(dictionary=True)
    verification_route_cursor.execute(conf)
    num=len(verification_route_cursor.fetchall())
    if(num==1):
        upstat="UPDATE users SET confirmation_status=1 WHERE email='{}'".format(ue)
        verification_route_cursor.execute(upstat)
        db.commit()
        result=jsonify({"msg":'Email Confirmed'})
        verification_route_cursor.close()
        db.close()
    else:
        result=jsonify({"error":"Couldn't Verify"})
    return result