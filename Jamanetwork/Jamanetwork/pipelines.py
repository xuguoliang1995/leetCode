import datetime
import json
import pymongo
from scrapy import log
from scrapy.exceptions import DropItem
from scrapy.utils.project import get_project_settings

settings = get_project_settings()


class JamanetworkPipeline(object):
    def open_spider(self, spider):
        self.fp = open('../json/d.json', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        json_str = json.dumps(dict(item), ensure_ascii=False)
        self.fp.write(json_str + "," + '\n')
        return item

    def close_spider(self, spider):
        self.fp.close()


class MongoDBPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient(settings['MONGODB_SERVER'], settings['MONGODB_PORT'])
        db = client[settings["MONGODB_DB"]]
        db.authenticate('qisu', 'qisu', source='qisu')
        self.collection = db[settings['MONGODB_COLLECTION']]
        self.init_count = self.collection.find().count()
        self.count_insert = 0

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem('丢失了{}从{}'.format(data, item['link']))
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
                        "is_pubmed": 0,
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
                    for data in datas:
                        self.collection.update({'doi': data['doi']},
                                               {'$set': {'updated_at': Spider[0]['updated_at'],
                                                         "doi": item["doi"], 'pub_date': item["pub_date"],
                                                         'abstract': item["abstract"]
                                                         }})

        last_count = self.init_count + self.count_insert
        print("&" * 40, '数据库更新了%d' % (last_count - self.count_insert))
        print("&" * 40, '数据库新插入了%d' % self.count_insert)
        print("&" * 40, '数据库总共有%d' % last_count)
        return item
