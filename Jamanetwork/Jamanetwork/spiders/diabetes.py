import re
import scrapy
from scrapy import Request
from Jamanetwork.items import JamanetworkItem


def strip_tag(str_s):
    new_dr = ""
    for s in str_s:
        if s:
            s = s.replace('\n', " ").replace('\\u2009', "").replace('\xa0', "").replace('\u2005', "")
            fr = re.compile(r'<[^>]+>', re.S)
            dr = fr.sub('', s)
            for i in dr:
                new_dr = new_dr + i
    return new_dr


def tranfrom_date(t):
    if t:
        year, month, day = t.split('/')
        return '%s-%s-%s' % (year, month, day)
    return ""


def handler_abstract(extract_list):
    new_str = ""
    if extract_list:
        for i in extract_list:
            new_str = new_str + i
        return new_str
    return ""


class DiabetesSpider(scrapy.Spider):
    name = 'diabetes'
    # allowed_domains = ['diabetes.diabetesjournals.org']
    start_urls = [
        'http://diabetes.diabetesjournals.org/content/current',
        'http://diabetes.diabetesjournals.org/content/early/recent'
    ]

    def parse(self, response):
        detail_urls = response.xpath('//li//a[@class="highwire-cite-linked-title"]//@href').extract()[:-5]
        for detail_url in detail_urls:
            request_url = 'http://diabetes.diabetesjournals.org' + detail_url
            request = Request(url=request_url, callback=self.parse_info, dont_filter=True)
            request.meta['link'] = request_url
            print(request_url)
            yield request

    def parse_info(self, response):
        item = JamanetworkItem()
        item['title'] = strip_tag(response.xpath('//meta[@property="og:title"]/@content').extract())
        item['link'] = response.meta['link']
        item['source'] = "Diabetes"
        item['pub_date'] = response.xpath('//meta[@name="DC.Date"]/@content').get()
        item['abstract'] = strip_tag(response.xpath('//meta[@name="og:description"]//@content').extract()) or \
                           strip_tag(handler_abstract(response.xpath('//meta[@name="citation_abstract"]//@content').extract()))
        item['doi'] = response.xpath('//meta[@name="citation_doi"]/@content').get()
        item['authors'] = response.xpath('//meta[@name="citation_author"]/@content').extract()
        # item['AffiliationInfo'] = response.xpath('//meta[@name="citation_author_institution"]/@content').extract()
        item['if_2017'] = 7.273
        # "issnElectronic": "1939-327X"
        item['issn'] = '0012-1797'
        item["is_pubmed"] = 0
        yield item
