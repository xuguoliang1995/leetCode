import re
import scrapy
from scrapy import Request
from Jamanetwork.items import JamanetworkItem


def strip_tag(str_s):
    new_dr = ""
    for s in str_s:
        if s:
            s = s.replace('\n', " ").replace('\\u2009', "").replace('\xa0', "").replace('\u2005', "").replace("\u2009","")
            fr = re.compile(r'</?\w+[^>]*>', re.S)
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
            new_str = new_str.replace('\n', '').replace('\u2009.', '').replace('\u202f', "")
        return new_str
    return ""


class JamanetworkSpider(scrapy.Spider):
    name = 'jamanetwork'
    allowed_domains = ['jamanetwork.com']
    start_urls = [
        'https://jamanetwork.com/journals/jamaneurology/newonline',
        'https://jamanetwork.com/journals/jamapediatrics/newonline',
        'https://jamanetwork.com/journals/jamapsychiatry/newonline',
        'https://jamanetwork.com/journals/jamaoncology/newonline',
        'https://jamanetwork.com/journals/jamainternalmedicine/newoline',
        'http://jamanetwork.com/journals/jama/currentissue'
    ]

    def parse(self, response):
        detail_urls = set(response.xpath('//div[contains(@class,"issue-group-articles")]//h3//a/@href').extract())
        for request_url in detail_urls:
            print(request_url)
            request = Request(url=request_url, callback=self.parse_info, dont_filter=True)
            request.meta['link'] = request_url
            yield request

    def parse_info(self, response):
        item = JamanetworkItem()
        item['title'] = strip_tag(response.xpath('//meta[@property="og:title"]/@content').extract())
        item['link'] = response.meta['link']
        item['source'] = "JAMA internal medicine"
        item['pub_date'] = tranfrom_date(response.xpath('//meta[@name="citation_online_date"]/@content').get()) or \
                           tranfrom_date(response.xpath('//meta[@name="citation_publication_date"]/@content').get())
        abstract = response.xpath('//meta[@name="citation_abstract"]/@content').extract_first()
        abstract1 = strip_tag(handler_abstract(response.xpath('//div[@class="abstract-content"]//p[@class="para"]//text() | '
                                            '//div[@class="article-full-text"]//p[@class="para"]//text()').extract()))
        item['abstract'] = abstract1 if not abstract else strip_tag(abstract)
        item['doi'] = response.xpath('//meta[@name="citation_doi"]/@content').get()
        item['authors'] = response.xpath('//meta[@name="citation_author"]/@content').extract()
        # item['AffiliationInfo'] = response.xpath('//meta[@name="citation_author_institution"]/@content').extract()
        item['if_2017'] = 19.989
        item['issn'] = "2168-6114"
        item["is_pubmed"] = 0
        yield item
