import datetime
import json
import pymongo
from scrapy import log
from scrapy.exceptions import DropItem
from scrapy.utils.project import get_project_settings


settings = get_project_settings()


class JamanetworkPipeline(object):
    def open_spider(self,spider):
        self.fp = open('../json/d.json','a',encoding='utf-8')

    def process_item(self, item, spider):
        json_str = json.dumps(dict(item),ensure_ascii=False)
        self.fp.write(json_str + "," +'\n')
        return item

    def close_spider(self,spider):
        self.fp.close()


# def find_if_source(issn):
#     client = pymongo.MongoClient('124.42.117.168:27017')
#     db = client.qisu
#     db.authenticate('qisu', 'qisu', source='qisu')
#     coll = db["journals"]
#     datas = coll.find({"$or":[{"issnElectronic": issn}, {"issnPrint": issn}]})
#     d = {}
#     for data in datas:
#         print('&&&&&')
#         d['if_2017'] = data['if_2017']
#         d['source'] = data['titleMain']
#     return d


class MongoDBPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient(settings['MONGODB_SERVER'], settings['MONGODB_PORT'])
        db = client[settings["MONGODB_DB"]]
        self.collection = db[settings['MONGODB_COLLECTION']]
        self.init_count = self.collection.find().count()
        self.count_insert = 0
        self.count_update = 0
    def process_item(self,item,spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem('丢失了{}从{}'.format(data,item['link']))
            if valid:
                Spider = [
                    {
                        'title': item["title"],
                        'link': item["link"],
                        'source': item["source"],
                        'pub_date': item["pub_date"],
                        'abstract': item["abstract"],
                        'doi': item["doi"],
                        'authors': item["authors"],
                        'if_2017': item["if_2017"],
                        'issn': item["issn"],
                        # 'AffiliationInfo': item[""],
                        "created_at": datetime.datetime.utcnow(),
                        "updated_at": datetime.datetime.utcnow(),
                    }
                ]
                datas = self.collection.find({'doi': item['doi']})
                if datas.count() == 0:
                    self.collection.insert_many(Spider)
                    self.count_insert += 1
                    log.msg(
                        'Item wrote to MongoDB database %s/%s' % (
                        settings['MONGODB_DB'], settings['MONGODB_COLLECTION']),
                        level=log.DEBUG, spider=spider)
                else:
                    # d = find_if_source(item['issn'])
                    # if_2017 = d.get('if_2017')
                    # source = d.get('source')
                    # if not (if_2017 or source):
                    #       with open('null.txt','a',encoding='utf-8') as f:
                    #           f.write(item['link'] + '\n')
                    for data in datas:
                        self.collection.update({'doi': data['doi']},
                                              {'$set':{'updated_at': Spider[0]['updated_at'],
                                                       "doi": item["doi"], 'pub_date': item["pub_date"],
                                                       'abstract': item["abstract"]
                                                       }})
                     # log.msg(
                     #            'Item update to MongoDB database %s/%s/%s' % (
                     #             settings['MONGODB_DB'], settings['MONGODB_COLLECTION'],item['doi']),
                     #             level=log.DEBUG, spider=spider)
                     # self.count_update = self.count_update + 1
        last_count = self.init_count + self.count_insert
        # print("&"*40,'数据库更新了%d' % self.count_update)
        print("&"*40,'数据库新插入了%d' % self.count_insert)
        print("&"*40,'数据库总共有%d' % last_count)
        return item



