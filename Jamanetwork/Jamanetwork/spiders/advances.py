import re
import scrapy
from scrapy import Request
from Jamanetwork.items import JamanetworkItem


def strip_tag(str_s):
    new_dr = ""
    for s in str_s:
        if s:
            s = s.replace('\n'," ").replace('\\u2009',"").replace('\xa0',"").replace('\u2005',"")
            fr = re.compile(r'<[^>]+>',re.S)
            dr = fr.sub('',s)
            for i in dr:
                new_dr = new_dr + i
    return new_dr


def tranfrom_date(t):
    if t:
        year,month,day = t.split('/')
        return '%s-%s-%s' % (year,month,day)
    return ""


def handler_abstract(extract_list):
    new_str = ""
    if extract_list:
        for i in extract_list:
            new_str = new_str + i
            new_str.replace('\n','')
        return new_str
    return ""


class AdvancesSpider(scrapy.Spider):
    name = 'advances'
    # allowed_domains = ['advances.sciencemag.org']
    start_urls = [
                  'http://advances.sciencemag.org',
                  ]

    def parse(self, response):
        detail_urls = response.xpath('//article//h3//a/@href').extract() or response.xpath('//article//h2//a/@href').extract()
        for detail_url in detail_urls:
            header_url = 'http://advances.sciencemag.org'
            request_url = header_url + detail_url
            print(request_url)
            request = Request(url=request_url, callback=self.parse_info, dont_filter=True)
            request.meta['link'] = request_url
            yield request

    def parse_info(self, response):
        item = JamanetworkItem()
        item['title'] = strip_tag(response.xpath('//meta[@property="og:title"]/@content').extract_first())
        item['link'] = response.meta['link']
        item['source'] = "Science advances"
        item['pub_date'] = response.xpath('//meta[@name="DC.Date"]/@content').get() or \
                           response.xpath('//meta[@property="article:published_time"]/@content').get()[:10]
        item['abstract'] = strip_tag(response.xpath('//meta[@name="og:description"]/@content').extract()) or \
                           strip_tag(response.xpath('//meta[@itemprop="description"]/@content').extract())
        item['doi'] = response.xpath('//meta[@name="citation_doi"]/@content').get() or \
                      response.xpath('//meta[@name="news_doi"]/@content').get() or ' '
        item['authors'] = response.xpath('//meta[@name="citation_author"]/@content').extract() or " "
        # item['AffiliationInfo'] = response.xpath('//meta[@name="citation_author_institution"]/@content').extract() or ""
        item['if_2017'] = 11.511
        item['issn'] = '2375-2548'
        yield item
