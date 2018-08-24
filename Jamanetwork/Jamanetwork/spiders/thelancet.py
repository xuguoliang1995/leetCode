import re
import scrapy
from scrapy import Request
from Jamanetwork.items import JamanetworkItem


def strip_tag(str_s):
    new_dr = ""
    for s in str_s:
        if s:
            s = s.replace('\n', "").replace('\\u2009', "").replace('\xa0', "").replace('\u2005', "")
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
            new_str = new_str.replace('\n', '').replace('\u2009.', '').replace('\u202f', "")
        return new_str
    return ""


class ThelancetSpider(scrapy.Spider):
    name = 'thelancet'
    # allowed_domains = ['www.thelancet.com']
    start_urls = ['http://www.thelancet.com']

    def parse(self, response):
        detail_urls = response.xpath('//div[@class="articleTitle"]//a//@href').extract()
        for detail_url in detail_urls:
            request_url = 'http://www.thelancet.com' + detail_url
            request = Request(url=request_url, callback=self.parse_info, dont_filter=True)
            request.meta['link'] = request_url
            yield request

    def parse_info(self, response):
        item = JamanetworkItem()
        item['title'] = strip_tag(response.xpath('//meta[@property="og:title"]/@content').extract())
        item['link'] = response.meta['link']
        issn = response.xpath('//meta[@name="citation_issn"]/@content').extract()[0]
        item['issn'] = issn
        if issn == "0140-6736" or "1474-547X":
            item['source'] = "Lancet"
            item['if_2017'] = 53.254
        elif issn == "2468-2667":
            item['source'] = "The Lancet. Public health"
            item['if_2017'] = 1.441
        elif issn == "2213-2600" or "2213-2619":
            item['source'] = "The Lancet. Respiratory medicine"
            item['if_2017'] = 3.23
        elif issn == "2542-5196":
            item['source'] = "The Lancet. Planetary health"
            item['if_2017'] = ""
        elif issn == "2215-0366" or "2215-0374":
            item['source'] = "The Lancet. Child & adolescent health"
            item['if_2017'] = 15.233
        elif issn == "1474-4465" or "1474-4422":
            item['source'] = "The Lancet. Neurology"
            item['if_2017'] = 27.138
        elif issn == "1470-2045" or "1474-5488":
            item['source'] = "The Lancet. Oncology"
            item['if_2017'] = 36.418
        elif issn == "2213-8587" or "2213-8595":
            item['source'] = "The lancet. Diabetes & endocrinology"
            item['if_2017'] = 19.313
        else:
            item['source'] = ""
            item['if_2017'] = ""
        item['pub_date'] = tranfrom_date(response.xpath('//meta[contains(@name,"date")]/@content').get())
        item['abstract'] = strip_tag(response.xpath('//meta[@name="citation_abstract"]/@content').extract()) or \
                           handler_abstract(strip_tag(response.xpath('//div[@class="section-paragraph"]//text()').extract())) \
                           or " "
        item['doi'] = response.xpath('//meta[@name="citation_doi"]/@content').get()
        item['authors'] = response.xpath('//meta[@name="citation_author"]/@content').extract()
        # item['AffiliationInfo'] = response.xpath('//meta[@name="citation_author_institution"]/@content').extract()
        item["is_pubmed"] = 0
        yield item
