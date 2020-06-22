from flask import Blueprint
from flask import Flask,request,jsonify
import sqlconfig

get_category_route=Blueprint('get_category_route',__name__)
@get_category_route.route('/getcategories',methods=['GET'])
def getcategories():
    db=sqlconfig.createConnection()
    get_category_cursor=db.cursor(dictionary=True)
    getallcat="SELECT name FROM subcategories ORDER BY parentcat"
    get_category_cursor.execute(getallcat)
    return jsonify(get_category_cursor.fetchall())