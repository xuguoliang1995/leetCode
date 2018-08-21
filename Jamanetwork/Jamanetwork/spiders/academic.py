import re
import scrapy
from scrapy import Request
from Jamanetwork.items import JamanetworkItem


def strip_tag(str_s):
    new_dr = ""
    for s in str_s:
        if s:
            s = s.replace('\n', " ").replace('\\u2009', "").replace('\xa0', "").replace('\u2005', "").replace('\u2009', "")
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


class AcademicSpider(scrapy.Spider):
    name = 'academic'
    allowed_domains = ['academic.oup.com']
    start_urls = [
        'https://academic.oup.com/eurheartj/advance-articles',
        'https://academic.oup.com/brain/advance-articles',
    ]

    def parse(self, response):
        count = 0
        detail_urls = response.xpath('//h5[@class="al-title"]//a/@href').extract()
        for detail_url in detail_urls:
            request_url = 'https://academic.oup.com' + detail_url
            print(request_url)
            count += 1
            request = Request(url=request_url, callback=self.parse_info, dont_filter=True)
            request.meta['link'] = request_url
            yield request
        print('*' * 30, count)

    def parse_info(self, response):
        item = JamanetworkItem()
        item['title'] = response.xpath('//meta[@property="og:title"]/@content').extract_first()
        link = response.meta['link']
        item['link'] = link
        item['source'] = "Brain : a journal of neurology" if 'brain' in link else "European heart journal"
        item['pub_date'] = response.xpath('//meta[@property="og:updated_time"]/@content').get()
        abstract = strip_tag(response.xpath('//section[@class="abstract"]//text()').extract()).strip("[']") or \
                   strip_tag(response.xpath('//div[@class="widget-items"]//p//text()').extract()).strip("[']")
        item['abstract'] = abstract if abstract else " "
        item['doi'] = response.xpath('//meta[@name="citation_doi"]/@content').get()
        item['authors'] = response.xpath('//meta[@name="citation_author"]/@content').extract()
        # item['AffiliationInfo'] = response.xpath('//meta[@name="citation_author_institution"]/@content').extract()
        item['if_2017'] = 10.84 if 'brain' in link else 23.425
        item['issn'] = tranfrom_issn(response.xpath('//div[@class="journal-footer-colophon"]//li//text()').get())
        item["is_pubmed"] = 0
        yield item
