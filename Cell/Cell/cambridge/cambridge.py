import re
import time
import datetime
import pymongo
from scrapy import log
from lxml import etree
from bs4 import BeautifulSoup
from selenium import webdriver
from scrapy.exceptions import DropItem
from scrapy.utils.project import get_project_settings
from selenium.webdriver.chrome.options import Options
settings = get_project_settings()


def strip_tag(str_s):
    new_dr = ""
    for s in str_s:
        if s:
            s = s.replace('\n', "").replace('\xa0', "").replace('\u2005', "")
            fr = re.compile(r'<[^>]+>', re.S)
            dr = fr.sub('', s)
            for i in dr:
                new_dr = new_dr + i
    new_dr = re.sub(r"\s{2,}", "", new_dr)
    return new_dr


def tranfrom_date(t):
    if t:
        year, month, day = t.split('/')
        return '%s-%s-%s' % (year, month, day)
    return ""


class MongoDBData(object):
    def __init__(self):
        client = pymongo.MongoClient(settings['MONGODB_SERVER'], settings['MONGODB_PORT'])
        db = client[settings["MONGODB_DB"]]
        db.authenticate("qisu","qisu",source="qisu")
        self.collection = db[settings['MONGODB_COLLECTION']]
        self.init_count = self.collection.find().count()
        self.count_insert = 0
        self.count_update = 0

    def html_parse(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        browser = webdriver.Chrome(chrome_options=chrome_options)
        host = "https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/latest-issue"
        browser.get(host)
        time.sleep(10)
        soup = BeautifulSoup(browser.page_source, "lxml")
        request_urls = soup.select("ul  li .part-link")
        spider = []
        for url in request_urls:
            request_url = "https://www.cambridge.org" + url.attrs.get("href")
            print(request_url)
            browser.get(request_url)
            time.sleep(10)
            text = browser.page_source
            html = etree.HTML(text)
            item = {}
            item['title'] = html.xpath('//meta[@name="citation_title"]//@content')[0]
            item['link'] = request_url
            item['source'] = "The Behavioral and brain sciences"
            item['pub_date'] = tranfrom_date(html.xpath('///meta[@name="citation_online_date"]/@content')[0])
            item['abstract'] = strip_tag(html.xpath('//div[@class="abstract"]//p//text()'))
            item['doi'] = html.xpath('//meta[@name="dc.identifier"]/@content')[0].split(":")[1]
            item['authors'] = html.xpath('//meta[@name="citation_author"]//@content')
            # item['AffiliationInfo'] = response.xpath('//meta[@name="citation_author_institution"]/@content').extract()
            item['if_2017'] = 15.071
            # "issnPrint": "0140-525X"
            item['issn'] = "1469-1825"
            item["is_pubmed"] = 0
            item["created_at"] = datetime.datetime.utcnow()
            item["updated_at"] = datetime.datetime.utcnow()
            print(item)
            spider.append(item)
        return spider

    def insert_mongodb(self, spider):
        valid = True
        for data in spider:
            if not data:
                valid = False
                raise DropItem('丢失了{}从{}'.format(data, data['link']))
            if valid:
                datas = self.collection.find({'doi': data['doi']})
                if datas.count() == 0:
                    self.collection.insert_many([data])
                    self.count_insert += 1
                    log.msg(
                        'Item wrote to MongoDB database %s/%s' % (
                            settings['MONGODB_DB'], settings['MONGODB_COLLECTION']),
                        level=log.DEBUG)
                else:
                    for data in datas:
                        self.collection.update({'doi': data['doi']},
                                               {'$set': {'updated_at': datetime.datetime.utcnow(),
                                                         "doi": data["doi"], 'pub_date': data["pub_date"],
                                                         'abstract': data["abstract"]}})

        last_count = self.init_count + self.count_insert
        print("&" * 40, '数据库更新了%d' % (last_count - self.count_insert))
        print("&" * 40, '数据库新插入了%d' % self.count_insert)
        print("&" * 40, '数据库总共有%d' % last_count)


insertMongodb = MongoDBData()
spider = insertMongodb.html_parse()
insertMongodb.insert_mongodb(spider)
