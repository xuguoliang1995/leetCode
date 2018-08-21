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


def tranfrom_issn(s):
    if s:
        issn = s.split(' ')[2]
        return issn
    return ""


class Bmj1Spider(scrapy.Spider):
    name = 'bmj1'
    # allowed_domains = ['gut.bmj.com']
    start_urls = [
        'https://gut.bmj.com/content/early/recent',
        'https://ard.bmj.com/content/early/recent'
    ]

    def parse(self, response):
        detail_urls = response.xpath(
            '//div[@class="pane-content"]//ul//li//a[@class="highwire-cite-linked-title"]//@href').extract()
        for detail_url in detail_urls:
            if 'annrheumdis' in detail_url:
                request_url = 'https://ard.bmj.com' + detail_url
            elif 'gutjnl' in detail_url:
                request_url = 'https://gut.bmj.com' + detail_url
            else:
                request_url = ''
            print(request_url)
            request = Request(url=request_url, callback=self.parse_info, dont_filter=True)
            request.meta['link'] = request_url
            yield request

    def parse_info(self, response):
        item = JamanetworkItem()
        item['title'] = response.xpath('//meta[@property="og:title"]/@content').extract_first()
        item['link'] = response.meta['link']
        issn = tranfrom_issn(response.xpath('//small//span//text()').get())
        item['issn'] = issn
        if issn == "1468-2060":
            item['source'] = "Annals of the rheumatic diseases"
            item['if_2017'] = 12.35
        elif issn == "1468-3288":
            item['source'] = "Gut"
            item['if_2017'] = 17.016
        item['pub_date'] = response.xpath('//meta[@name="DC.Date"]/@content').get()
        item['abstract'] = strip_tag(response.xpath('//meta[@name="DC.Description"]/@content').extract())
        item['doi'] = response.xpath('//meta[@name="citation_doi"]/@content').get()
        item['authors'] = response.xpath('//meta[@name="citation_author"]/@content').extract()
        # item['AffiliationInfo'] = response.xpath('//meta[@name="citation_author_institution"]/@content').extract()
        item["is_pubmed"] = 0
        yield item
