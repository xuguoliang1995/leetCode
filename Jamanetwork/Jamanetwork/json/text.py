# import pymongo
#
#
# def find_if_source(issn):
#     client = pymongo.MongoClient('124.42.117.168:27017')
#     db = client.qisu
#     db.authenticate('qisu', 'qisu', source='qisu')
#     coll = db["journals"]
#     datas = coll.find({"$or":[{"issnElectronic": issn}, {"issnPrint": issn}]})
#     d = {}
#     for data in datas:
#         print('&&&&&')
#         flag = False
#         d['if_2017'] = data['if_2017']
#         d['source'] = data['titleMain']
#     return d
#
# issn = "1934-5909"
# d = find_if_source(issn)
# print(d)
