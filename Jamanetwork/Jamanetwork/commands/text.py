# import pandas as pd
# 
# df = pd.read_table('"null".txt')
# 
# df.drop_duplicates(inplace=True)
# print(df)
# df.to_csv('new_"null".txt',index=False)
# 
# 
# import pymongo
# import json
# client = pymongo.MongoClient('localhost',27017)
# db = client.spider1
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
# with open('Map.txt', 'w',encoding='utf-8') as fp:
#      fp.write(d_json + '\n')


# import json
#
# L = []
# for i in a:
#     if i['issn'] not in L:
#        L.append(i['issn'])
#        L.append(i)
# json_str = json.dumps(L)
# with open('simple_Map.txt','w',encoding='utf-8') as f:
#     f.write(json_str)

