
import pymongo

id=123456


def get_db():

    client = pymongo.MongoClient(host='139.129.27.197',port=12345)
    db = client['fangwei']

    return db



def find_one_and_replace(db):
    coll = db['fangwei']

    count=coll.find_one()
    print count
    coll_count=count["count"]
    num=coll_count



    information1 = {"id": id}
    information2={'$set':{"count": 0}}
    information_id = coll.update(information1,information2)
    print information_id




if __name__ == '__main__':
    db = get_db()
    find_one_and_replace(db)