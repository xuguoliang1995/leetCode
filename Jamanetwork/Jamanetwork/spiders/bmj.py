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


class BmjSpider(scrapy.Spider):
    name = 'bmj'
    # allowed_domains = ['www.bmj.com']
    start_urls = ['http://www.bmj.com/news/news?category=News',
                  'http://www.bmj.com/research/research',
                  'http://www.bmj.com/research/research%20news']

    def parse(self, response):
        detail_urls = response.xpath('//div[@class="view-content"]//h3//a//@href').extract()
        for detail_url in detail_urls:
            header_url = 'https://www.bmj.com'
            request_url = header_url + detail_url
            print(request_url)
            request = Request(url=request_url, callback=self.parse_info, dont_filter=True)
            request.meta['link'] = request_url
            yield request
        print('******' * 30)

    def parse_info(self, response):
        item = JamanetworkItem()
        item['title'] = response.xpath('//meta[@name="citation_title"]/@content').extract_first()
        item['link'] = response.meta['link']
        item['issn'] = response.xpath('//meta[@name="citation_issn"]/@content').extract()[0]
        item['source'] = "BMJ : British medical journal"
        item['if_2017'] = 23.259
        item['pub_date'] = response.xpath('//meta[@name="article:published_time"]/@content').get()
        item['abstract'] = strip_tag(response.xpath('//meta[@name="DC.Description"]//@content').get())
        item['doi'] = response.xpath('//meta[@name="citation_doi"]/@content').get()
        item['authors'] = response.xpath('//meta[@name="citation_author"]/@content').extract()
        # item['AffiliationInfo'] = response.xpath('//meta[@name="citation_author_institution"]/@content').extract()
        item["is_pubmed"] = 0
        yield item
