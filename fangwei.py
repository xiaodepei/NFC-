from flask import Flask
from flask import Flask, jsonify, render_template, request
import os
import linecache
import pymongo
import urllib2
import re







def get_db():
    client = pymongo.MongoClient(host='127.0.0.1',port=12345)
    db = client['fangwei']
    return db



def find_one_and_replace(db,id):
    coll = db['fangwei']
    count=coll.find_one({"id":id})
    # print count

    coll_count=count["count"]
    num=coll_count
    num=num+1
    # print num
    information1 = {"id": id}
    # print information1
    information2={'$set':{"count": num}}
    # print information2
    information_id = coll.update(information1,information2)
    # print information_id
    return num




app = Flask(__name__)



@app.route('/click')
def jianding():
    id = request.args.get('id', 0, type=str)
    db = get_db()
    lblToalNum = find_one_and_replace(db, id)
    lblToalNum = str(lblToalNum)
    return jsonify(jiandingcishu=lblToalNum)




@app.route('/fangwei/x=<id>')
def fangwei(id):
    id = int(id)
    # print id
    db = get_db()
    lblToalNum = find_one_and_replace(db, id)
    lblToalNum = str(lblToalNum)
    text=lblToalNum
    return render_template("fangwei.html",**locals())



if __name__ == '__main__':

    app.run(host = "0.0.0.0",port = 8000, debug = True,)
