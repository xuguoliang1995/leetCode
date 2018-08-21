import pymongo
import threading


MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "submission"
MONGODB_COLLECTION = "submission"
from itertools import islice

client = pymongo.MongoClient(MONGODB_SERVER, MONGODB_PORT)
db = client[MONGODB_DB]
collection = db[MONGODB_COLLECTION]


def insert_mongodb():
   with open(r"/Users/xuguoliang/Demo/qisu/file/Submission_Submission_lookup_SubmissionProperty.csv", "r") as f:
    datas = f.readlines()
    for data in islice(datas, 1, None):
        ApplNo, *other_tag = data.strip().split("#")
        d = [
            {
                "ApplNo": "{:0>6}".format(ApplNo),
                "SubmissionClassCodeID": other_tag[0],
                "SubmissionType": other_tag[1],
                "SubmissionNo": other_tag[2],
                "SubmissionStatus": other_tag[3],
                "SubmissionStatusDate": other_tag[4],
                "SubmissionsPublicNotes": other_tag[5],
                "ReviewPriority": other_tag[6],
                "SubmissionClassCode": other_tag[7],
                "SubmissionClassCodeDescription": other_tag[8],
                "SubmissionPropertyTypeCode": other_tag[9],
                "SubmissionPropertyTypeID": other_tag[10]
            }
        ]
        database_data = collection.find({
            'ApplNo': d[0]['ApplNo'],
            "SubmissionClassCodeID": d[0]['SubmissionClassCodeID'],
            "SubmissionType": d[0]['SubmissionType'],
            "SubmissionNo": d[0]['SubmissionNo'],
            "SubmissionStatus": d[0]['SubmissionStatus'],
            "SubmissionStatusDate": d[0]['SubmissionStatusDate'],
            "SubmissionsPublicNotes": d[0]['SubmissionsPublicNotes'],
            "ReviewPriority": d[0]['ReviewPriority'],
            "SubmissionClassCode": d[0]['SubmissionClassCode'],
            "SubmissionClassCodeDescription": d[0]['SubmissionClassCodeDescription'],
            "SubmissionPropertyTypeCode": d[0]['SubmissionPropertyTypeCode'],
            "SubmissionPropertyTypeID": d[0]['SubmissionPropertyTypeID']
        })
        if database_data.count() == 0:
            collection.insert_many(d)
        else:
            collection.update_many({
                                        'ApplNo': d[0]['ApplNo'],
                                        "SubmissionClassCodeID": d[0]['SubmissionClassCodeID'],
                                        "SubmissionType": d[0]['SubmissionType'],
                                        "SubmissionNo": d[0]['SubmissionNo'],
                                        "SubmissionStatus": d[0]['SubmissionStatus'],
                                        "SubmissionStatusDate": d[0]['SubmissionStatusDate'],
                                        "SubmissionsPublicNotes": d[0]['SubmissionsPublicNotes'],
                                        "ReviewPriority": d[0]['ReviewPriority'],
                                        "SubmissionClassCode": d[0]['SubmissionClassCode'],
                                        "SubmissionClassCodeDescription": d[0]['SubmissionClassCodeDescription'],
                                        "SubmissionPropertyTypeCode": d[0]['SubmissionPropertyTypeCode'],
                                        "SubmissionPropertyTypeID": d[0]['SubmissionPropertyTypeID']
                                    },
                                       {'$set': {
                                           'ApplNo': d[0]['ApplNo'],
                                           "SubmissionClassCodeID": d[0]['SubmissionClassCodeID'],
                                           "SubmissionType": d[0]['SubmissionType'],
                                           "SubmissionNo": d[0]['SubmissionNo'],
                                           "SubmissionStatus": d[0]['SubmissionStatus'],
                                           "SubmissionStatusDate": d[0]['SubmissionStatusDate'],
                                           "SubmissionsPublicNotes": d[0]['SubmissionsPublicNotes'],
                                           "ReviewPriority": d[0]['ReviewPriority'],
                                           "SubmissionClassCode": d[0]['SubmissionClassCode'],
                                           "SubmissionClassCodeDescription": d[0]['SubmissionClassCodeDescription'],
                                           "SubmissionPropertyTypeCode": d[0]['SubmissionPropertyTypeCode'],
                                           "SubmissionPropertyTypeID": d[0]['SubmissionPropertyTypeID']
                                       }})


