import json
import pymongo
from scrapy import log
from scrapy.utils.project import get_project_settings
from scrapy.exceptions import DropItem


settings = get_project_settings()
class NaturePipeline(object):
    def open_spider(self,spider):
        self.fp = open('../json/immunology.json','w',encoding='utf-8')

    def close_spider(self,spider):
        self.fp.close()

    def process_item(self, item, spider):
        json_str = json.dumps(dict(item),ensure_ascii=False)
        self.fp.write(json_str+ "," + '\n')
        return item

class MongoDBPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient(settings['MONGODB_SERVER'], settings['MONGODB_PORT'])
        db = client[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self,item,spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem('丢失了{0}从{0}'.format(data,item['link']))
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
                        '_if': item["_if"],
                        'issn': item["issn"],
                        # 'AffiliationInfo': item[""]
                    }
                ]
                self.collection.insert_many(Spider)
                log.msg(
                    'Item wrote to MongoDB database %s/%s' % (settings['MONGODB_DB'], settings['MONGODB_COLLECTION']),
                level=log.DEBUG,spider=spider)
        return item












