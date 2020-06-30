from flask import Blueprint
from flask import Flask,request,jsonify
import sqlconfig

select_category_route=Blueprint('select_category_route',__name__)
@select_category_route.route('/selectcategory',methods=['post'])
def select_category():
    payload=request.json
    email=payload['email']
    cat1=payload['category_1']
    cat2=payload['category_2']
    cat3=payload['category_3']
    try:
        profile_ins="INSERT INTO `user_profiles`(`email`, `cat1`, `cat2`, `cat3`) VALUES (%s,%s,%s,%s)"
        profile_ins_val=(email,cat1,cat2,cat3)
        db=sqlconfig.createConnection()
        select_category_cursor=db.cursor()
        select_category_cursor.execute(profile_ins,profile_ins_val)
        db.commit()
        select_category_cursor.close()
        db.close()
        result=jsonify({"msg":"success"})
    except:
        result=jsonify({"error":"Could not process request"})
    return result 
