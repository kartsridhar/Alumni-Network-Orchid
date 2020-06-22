import mysql.connector

def createConnection():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="alumini_network"
        )
    return db 