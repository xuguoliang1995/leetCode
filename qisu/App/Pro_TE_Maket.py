import pymongo
from itertools import islice
import threading
MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "Pro_TE_Market"
MONGODB_COLLECTION = "Pro_TE_Market"


client = pymongo.MongoClient(MONGODB_SERVER,MONGODB_PORT)
db = client[MONGODB_DB]
collection = db[MONGODB_COLLECTION]

def insert_mongodb():
    path = r"/Users/xuguoliang/Demo/qisu/file/Pro_TE_mark_makelookup.csv"
    with open(path, "r") as f:
        datas = f.readlines()
        for data in islice(datas, 1, None):
            ApplNo, *other_tag = data.strip().split("#")
            d = [
                {
                    "ApplNo": "{:0>6}".format(ApplNo),
                    "ProductNo": other_tag[0],
                    "Form": other_tag[1],
                    "Strength": other_tag[2],
                    "DrugName": other_tag[3],
                    "ActiveIngredient": other_tag[4],
                    "ReferenceStandard": other_tag[5],
                    "ReviewPriority": other_tag[6],
                    "MarketingStatusID": other_tag[7],
                    "TECode": other_tag[8],
                    "MarketingStatusDescription": other_tag[9],
                }
            ]
            database_data = collection.find({
                    'ApplNo': d[0]['ApplNo'],
                    "ProductNo": other_tag[0],
                    "Form": other_tag[1],
                    "Strength": other_tag[2],
                    "DrugName": other_tag[3],
                    "ActiveIngredient": other_tag[4],
                    "ReferenceStandard": other_tag[5],
                    "ReviewPriority": other_tag[6],
                    "MarketingStatusID": other_tag[7],
                    "TECode": other_tag[8],
                    "MarketingStatusDescription": other_tag[9],
            })
            if database_data.count() == 0:
                collection.insert_many(d)
            else:
                collection.update_many({
                    'ApplNo': d[0]['ApplNo'],
                    "ProductNo": other_tag[0],
                    "Form": other_tag[1],
                    "Strength": other_tag[2],
                    "DrugName": other_tag[3],
                    "ActiveIngredient": other_tag[4],
                    "ReferenceStandard": other_tag[5],
                    "ReviewPriority": other_tag[6],
                    "MarketingStatusID": other_tag[7],
                    "TECode": other_tag[8],
                    "MarketingStatusDescription": other_tag[9],
                },
                    {'$set': {
                        'ApplNo': d[0]['ApplNo'],
                        "ProductNo": other_tag[0],
                        "Form": other_tag[1],
                        "Strength": other_tag[2],
                        "DrugName": other_tag[3],
                        "ActiveIngredient": other_tag[4],
                        "ReferenceStandard": other_tag[5],
                        "ReviewPriority": other_tag[6],
                        "MarketingStatusID": other_tag[7],
                        "TECode": other_tag[8],
                        "MarketingStatusDescription": other_tag[9]
                    }})


if __name__ == "__main__":
    t1 = threading.Thread(target=insert_mongodb)
    t2 = threading.Thread(target=insert_mongodb)
    t1.start()
    t2.start()
    t1.join()
    t2.join()









