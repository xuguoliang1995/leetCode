import pymongo
from itertools import islice
import threading

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "Application"
MONGODB_COLLECTION = "Application"

client = pymongo.MongoClient(MONGODB_SERVER, MONGODB_PORT)
db = client[MONGODB_DB]
collection = db[MONGODB_COLLECTION]


def insert_mongodb():
    path = r"/Users/xuguoliang/Demo/qisu/file/Application_ApplicationDocs.csv"

    with open(path, "r") as f:
        datas = f.readlines()
        for data in islice(datas, 1, None):
            ApplNo, *other_tag = data.strip().split("#")
            d = [
                {
                    "ApplNo": "{:0>6}".format(ApplNo),
                    "ApplType": other_tag[0],
                    "ApplPublicNotes": other_tag[1],
                    "SponsorName": other_tag[2],
                    "ApplicationDocsID": other_tag[3],
                    "ApplicationDocsTypeID": other_tag[4],
                    "SubmissionType": other_tag[5],
                    "SubmissionNo": other_tag[6],
                    "ApplicationDocsTitle": other_tag[7],
                    "ApplicationDocsURL": other_tag[8],
                    "ApplicationDocsDate": other_tag[9],
                }
            ]
            database_data = collection.find({
                "ApplNo": "{:0>6}".format(ApplNo),
                "ApplType": other_tag[0],
                "ApplPublicNotes": other_tag[1],
                "SponsorName": other_tag[2],
                "ApplicationDocsID": other_tag[3],
                "ApplicationDocsTypeID": other_tag[4],
                "SubmissionType": other_tag[5],
                "SubmissionNo": other_tag[6],
                "ApplicationDocsTitle": other_tag[7],
                "ApplicationDocsURL": other_tag[8],
                "ApplicationDocsDate": other_tag[9],
            })
            if database_data.count() == 0:
                collection.insert_many(d)
            else:
                collection.update_many({
                    "ApplNo": "{:0>6}".format(ApplNo),
                    "ApplType": other_tag[0],
                    "ApplPublicNotes": other_tag[1],
                    "SponsorName": other_tag[2],
                    "ApplicationDocsID": other_tag[3],
                    "ApplicationDocsTypeID": other_tag[4],
                    "SubmissionType": other_tag[5],
                    "SubmissionNo": other_tag[6],
                    "ApplicationDocsTitle": other_tag[7],
                    "ApplicationDocsURL": other_tag[8],
                    "ApplicationDocsDate": other_tag[9],
                },
                    {'$set': {
                        "ApplNo": "{:0>6}".format(ApplNo),
                        "ApplType": other_tag[0],
                        "ApplPublicNotes": other_tag[1],
                        "SponsorName": other_tag[2],
                        "ApplicationDocsID": other_tag[3],
                        "ApplicationDocsTypeID": other_tag[4],
                        "SubmissionType": other_tag[5],
                        "SubmissionNo": other_tag[6],
                        "ApplicationDocsTitle": other_tag[7],
                        "ApplicationDocsURL": other_tag[8],
                        "ApplicationDocsDate": other_tag[9],
                    }})


t1 = threading.Thread(target=insert_mongodb)
t2 = threading.Thread(target=insert_mongodb)
t1.start()
t2.start()
t1.join()
t2.join()
