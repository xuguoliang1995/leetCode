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


def tranfrom_issn(s):
    if s:
        issn = s.split(' ')[2].strip('.')
        return issn
    return ""


def tranfrom_url(url):
    if url:
        url = url.replace('pdf', 'full')
        return url
    return url


class NejmSpider(scrapy.Spider):
    name = 'nejm'
    allowed_domains = ['nejm.org']
    start_urls = [
        'http://www.nejm.org/medical-articles/research',
        'http://www.nejm.org/toc/nejm/medical-journal'
    ]

    def parse(self, response):
        detail_urls = response.xpath(' //div//li//a[contains(@class,"m-result__download")]//@href').extract()
        for detail_url in detail_urls:
            request_url = "https://www.nejm.org" + tranfrom_url(detail_url)
            request = Request(url=request_url, callback=self.parse_info, dont_filter=True)
            request.meta['link'] = request_url
            yield request
            print(request_url)

    def parse_info(self, response):
        item = JamanetworkItem()
        item['title'] = response.xpath('//meta[@name="twitter:title"]/@content').get()
        item['link'] = response.meta['link']
        item['source'] = "The New England journal of medicine"
        item['pub_date'] = response.xpath('//meta[@name="evt-dt"]/@content').get() or\
                           response.xpath('//meta[@name="dc.Date"]/@content').get()
        item['abstract'] = strip_tag(response.xpath('//section[@class="o-article-body__section"]//text()').extract()) or \
                           strip_tag(response.xpath('//div[@class="m-letter"]//p[@class="f-body"]//text()').extract()) or ''
        item['doi'] = response.xpath('//meta[@name="evt-doiPage"]/@content').get()
        item['authors'] = response.xpath(
            '//header//ul[contains(@class,"m-article-header__authors")]//li//text()').extract()
        # item['AffiliationInfo'] = response.xpath('//meta[@name="citation_author_institution"]/@content').extract()
        item['if_2017'] = 79.258
        # item['issn'] = tranfrom_issn(response.xpath('//li[@class="hidden-xs nowrap"]//text()').extract()[0])
        # "issnPrint" : "0028-4793"
        item['issn'] = "1533-4406"
        item["is_pubmed"] = 0
        yield item
