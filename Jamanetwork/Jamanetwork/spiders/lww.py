import re
import scrapy
from scrapy import Request
from Jamanetwork.items import JamanetworkItem
from datetime import datetime


def tranfrom_date(s):
    count = 0
    if s:
        for i in s:
           if i == " ":
               count += 1
        if count == 1:
           time_format = datetime.strptime(s,"%B %Y")
        else:
           time_format = datetime.strptime(s,"%B %d, %Y")
        time_format = time_format.strftime('%Y-%m-%d')
        return time_format
    return ""


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


class LwwSpider(scrapy.Spider):
    name = 'lww'
    allowed_domains = ['journals.lww.com']
    start_urls = [
        'http://journals.lww.com/annalsofsurgery/pages/default.aspx',
        'https://journals.lww.com/jbjsjournal/pages/default.aspx',
        'https://journals.lww.com/annalsofsurgery/toc/publishahead',
         ]

    def parse(self, response):
        detail_urls = response.xpath('//header//h4//a//@href').extract()
        for request_url in detail_urls:
            print(request_url)
            request = Request(url=request_url, callback=self.parse_info, dont_filter=True)
            request.meta['link'] = request_url
            yield request

    def parse_info(self, response):
        item = JamanetworkItem()
        item['title'] = response.xpath('//meta[@name="wkhealth_title"]/@content').extract_first()
        item['link'] = response.meta['link']
        issn = response.xpath('//meta[@name="wkhealth_issn"]/@content').get()
        item['issn'] = issn
        if issn == "0021-9355":
            item['source'] = "The Journal of bone and joint surgery. American volume"
            item['if_2017'] = 4.583
        else:
            item['source'] = "Annals of surgery"
            item['if_2017'] = 9.203
        item['pub_date'] = tranfrom_date(response.xpath('//meta[@name="wkhealth_date"]/@content').get())
        item['abstract'] = strip_tag(response.xpath('//section[@class="article-abstract"]//div//p').extract()) or ''
        item['doi'] = response.xpath('//meta[@name="wkhealth_doi"]/@content').get()
        item['authors'] = response.xpath('//meta[@name="wkhealth_authors"]/@content').extract()
        # item['AffiliationInfo'] = response.xpath('//meta[@name="citation_author_institution"]/@content').extract()
        yield item







