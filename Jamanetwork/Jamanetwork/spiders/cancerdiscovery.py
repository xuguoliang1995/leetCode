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


class CancerdiscoverySpider(scrapy.Spider):
    name = 'cancerdiscovery'
    # allowed_domains = ['clincancerres.aacrjournals.org']
    start_urls = [
        'http://cancerdiscovery.aacrjournals.org/content/early/by/section?utm_source=early&utm_medium=dropdown&utm_campaign=menu',
        'http://cancerdiscovery.aacrjournals.org/content/8/7?utm_source=current&utm_medium=dropdown&utm_campaign=menu&current-issue=y',
    ]
    def parse(self, response):
        detail_urls = response.xpath('//div[@class="pane-content"]//div[@class="article-title"]//a//@href').extract()
        for detail_url in detail_urls:
            header_url = 'http://cancerdiscovery.aacrjournals.org'
            request_url = header_url + detail_url
            print(request_url)
            request = Request(url=request_url, callback=self.parse_info, dont_filter=True)
            request.meta['link'] = request_url
            yield request

    def parse_info(self, response):
        item = JamanetworkItem()
        item['title'] = response.xpath('//meta[@name="DC.Title"]/@content').extract_first()
        item['link'] = response.meta['link']
        item['issn'] = "2159-8290"
        item['source'] = "Cancer discovery"
        item['if_2017'] = 24.373
        item['pub_date'] = response.xpath('//meta[@name="DC.Date"]/@content').get()
        item['abstract'] = strip_tag(response.xpath('//meta[@name="DC.Description"]/@content').extract())
        item['doi'] = response.xpath('//meta[@name="DC.Identifier"]/@content').get()
        item['authors'] = response.xpath('//meta[@name="citation_author"]/@content').extract()
        # item['AffiliationInfo'] = response.xpath('//meta[@name="citation_author_institution"]/@content').extract()
        yield item


