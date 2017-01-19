
from flask import Flask, jsonify, render_template, request
import os
import linecache
import pymongo
import urllib2
import re

import sys




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
    ipaddr = request.remote_addr
    url = "http://www.ip138.com/ips138.asp?ip=%s&action=2" % ipaddr
    u = urllib2.urlopen(url)
    s = u.read()
    # Get IP Address
    ip = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', s)
    # print "\n****** Below Result From IP138 Database *****"
    # print "IP Address:", ip[0]
    reload(sys)
    sys.setdefaultencoding('gb18030')
    # Get IP Address Location
    result = re.findall(r'(<li>.*?</li>)', s)
    # print result
    address=str(result[0])
    location=address[14:-5]
    # print location
    # for i in result:
    #     print i[4:-5]


        # print i
    # print "*" * 45
    # print "\n"

    return render_template("fangwei.html",**locals())



if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    app.run(host = "0.0.0.0",port = 8000, debug = True,)
