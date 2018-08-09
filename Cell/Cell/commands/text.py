# import pandas as pd
#
#
# import pymongo
#
# def find_if_source(issn):
#     client = pymongo.MongoClient('124.42.117.168:27017')
#     db = client.qisu
#     db.authenticate('qisu', 'qisu', source='qisu')
#     coll = db["journals"]
#     datas = coll.find({'issnElectronic':issn})
#     d = {}
#     for data in datas:
#         d['issn'] = data['if_2017']
#         d['source'] = data['titleMain']
#     return d
#
#
# def find_if_source1(issn):
#     client = pymongo.MongoClient('124.42.117.168:27017')
#     db = client.qisu
#     db.authenticate('qisu', 'qisu', source='qisu')
#     coll = db["journals"]
#     datas = coll.find({'issnElectronic':issn})
#     d = {}
#     for data in datas:
#         print(data)
#         d['if_2017'] = data['if_2017']
#         d['source'] = data['titleMain']
#     return d
# d = find_if_source1("1468-2060")
# print(d)
# if_2017 = d['if_2017']
# print(if_2017)



# df = pd.read_table(''null'.txt')
# 
# df.drop_duplicates(inplace=True)
# print(df)
# df.to_csv('new_'null'1.txt',index=False)
# 
# import pymongo
# import json
# client = pymongo.MongoClient('localhost',27017)
# db = client.Spider
# collection = db.coll
# datas = collection.find()
# count = 0
# d_list = []
# for data in datas:
#     d = {}
#     d['link'] = data['link']
#     d['issn'] = data['issn']
#     d['if_2017'] = data['if_2017']
#     d['source'] = data['source']
#     d_list.append(d)
#     print(data['link'])
#     print(data['issn'])
#     print(data['if_2017'])
#     print(data['source'])
#     count += 1
# print(count)
# d_json = json.dumps(d_list)
# with open('Map1.txt', 'w',encoding='utf-8') as fp:
#      fp.write(d_json + '\n')


# import json
# L = []
# for i in a:
#     if i['issn'] not in L:
#        L.append(i['issn'])
#        L.append(i)
# json_str = json.dumps(L)
# with open('simple_Map1.txt','w',encoding='utf-8') as f:
#     f.write(json_str)









