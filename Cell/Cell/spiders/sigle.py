
import re
import scrapy
from scrapy import Request
from Cell.items import CellItem
from datetime import datetime


def strip_tag(str_s):
    new_dr = ""
    for s in str_s:
        if s:
            s = s.replace('\n',"").replace('\xa0',"").replace('\u2005',"")
            fr = re.compile(r'<[^>]+>',re.S)
            dr = fr.sub('',s)
            for i in dr:
                new_dr = new_dr + i
    new_dr = re.sub(r"\s{2,}", "", new_dr)
    return new_dr


def tranfrom_date(t):
    if t:
        try:
            time_format = datetime.strptime(t,"%d %b %Y")
        except:
            time_format = datetime.strptime(t, "%d %B %Y")
        time_format = time_format.strftime("%Y-%m-%d")
        return time_format
    return ""


def tranfrom_date1(t):
    if t:
        year,month,day = t.split('/')
        return '%s-%s-%s' % (year,month,day)
    return ""


def handler_abstract(extract_list):
    new_str = ""
    if extract_list:
        for i in extract_list:
            new_str = new_str + i
        return new_str
    return ""

def doi_str(s):
    s = s.split('/')[2:]
    new_s = ""
    for i in s:
        new_s = new_s + i
    return new_s

class ElifesciencesSpider(scrapy.Spider):
    name = 'sigle'
    # allowed_domains = ['elifesciences.org']
    start_urls = ['http://elifesciences.org']

    def parse(self, response):
        detail_urls = response.xpath('//ol//header//a//@href').extract()
        for detail_url in detail_urls:
            request_url = 'https://elifesciences.org' + detail_url
            print(request_url)
            request = Request(url=request_url, callback=self.parse_info, dont_filter=True)
            request.meta['link'] = request_url
            yield request

    def parse_info(self, response):
        item = CellItem()
        item['title'] = response.xpath('//meta[@name="dc.title"]/@content').extract_first()
        item['link'] = response.meta['link']
        item['source'] = "eLife"
        item['pub_date'] = response.xpath('//meta[@name="dc.date"]/@content').get()
        item['abstract'] = strip_tag(response.xpath('//section[@id="abstract"]//p//text()').extract())
        item['doi'] = response.xpath('//meta[@name="dc.identifier"]/@content').get()
        item['authors'] = response.xpath('//meta[@name="dc.contributor"]/@content').extract()
        # item['AffiliationInfo'] = response.xpath('//meta[@name="citation_author_institution"]/@content').extract()
        item['if_2017'] = 7.616
        item['issn'] = response.xpath('//hypothesis-highlight//text()').get() or '2050-084X'
        yield item


class JciSpider(scrapy.Spider):
    name = 'sigle1'
    # allowed_domains = ['elifesciences.org']
    start_urls = ['https://www.jci.org/just-published']

    def parse(self, response):
        detail_urls = response.xpath('//div[@class="small-12 columns"]//h5//a//@href').extract()
        for detail_url in detail_urls:
            request_url = 'https://www.jci.org' + detail_url
            print(request_url)
            request = Request(url=request_url, callback=self.parse_info, dont_filter=True)
            request.meta['link'] = request_url
            yield request

    def parse_info(self, response):
        item = CellItem()
        item['title'] = strip_tag(response.xpath('//meta[@name="citation_title"]//@content').extract_first())
        item['link'] = response.meta['link']
        item['source'] = "The Journal of clinical investigation"
        item['pub_date'] = response.xpath('///meta[@name="DC.Date"]/@content').get()
        item['abstract'] = strip_tag(response.xpath('//div[@id="section-abstract"]//p//text()').extract()) or\
                           strip_tag(response.xpath('//div[contains(@style,"margin-bottom")]//p//text()').extract())

        item['doi'] = response.xpath('//meta[@name="citation_doi"]/@content').get()
        item['authors'] = response.xpath('//meta[@name="citation_author"]//@content').extract()
        # item['AffiliationInfo'] = response.xpath('//meta[@name="citation_author_institution"]/@content').extract()
        item['if_2017'] = 13.251
        item['issn'] = response.xpath('//meta[@name="citation_issn"]/@content').get()
        yield item


# class CambridgetSpider(scrapy.Spider):
#     name = 'sigle2'
#     # allowed_domains = ['www.cambridge.org']
#     start_urls = ['https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/latest-issue']
#     def parse(self, response):
#         detail_urls = response.xpath('//ul[@class="details"]//li[@class="title"]//a//@href').extract()
#         for detail_url in detail_urls:
#             request_url = 'https://www.cambridge.org' + detail_url
#             print(request_url)
#             request = Request(url=request_url, callback=self.parse_info, dont_filter=False)
#             request.meta['link'] = request_url
#             yield request
#
#     def parse_info(self, response):
#         item = CellItem()
#         item['title'] = response.xpath('//meta[@name="citation_title"]//@content').extract_first()
#         item['link'] = response.meta['link']
#         item['source'] = "The Behavioral and brain sciences"
#         item['pub_date'] = response.xpath('///meta[@name="citation_online_date"]/@content').get()
#         item['abstract'] = strip_tag(response.xpath('//div[@class="abstract"]//p//text()').extract())
#         item['doi'] = response.xpath('//meta[@name="dc.identifier"]/@content').get()
#         item['authors'] = response.xpath('//meta[@name="citation_author"]//@content').extract()
#         # item['AffiliationInfo'] = response.xpath('//meta[@name="citation_author_institution"]/@content').extract()
#         item['if_2017'] = 15.071
#         item['issn'] = response.xpath('//meta[@name="citation_issn"]/@content').extract()[1]
#         yield item


class NatureSpider(scrapy.Spider):
    name = 'sigle3'
    # allowed_domains = ['www.cambridge.org']
    start_urls = ['https://www.nature.com/mp']

    def parse(self, response):
        detail_urls = response.xpath('//article//h3//a//@href').extract()
        for detail_url in detail_urls:
            request_url = 'https://www.nature.com' + detail_url
            print(request_url)
            request = Request(url=request_url, callback=self.parse_info, dont_filter=True)
            request.meta['link'] = request_url
            yield request

    def parse_info(self, response):
        item = CellItem()
        item['title'] = strip_tag(response.xpath('//meta[@name="citation_title"]//@content').extract_first())
        item['link'] = response.meta['link']
        item['source'] = "Molecular psychiatry"
        item['pub_date'] = response.xpath('///meta[@name="dc.date"]/@content').get()
        item['abstract'] = strip_tag(response.xpath('//div[@itemprop="description"]//p//text()').extract()) or strip_tag(
            response.xpath('//div[@id="Abs1-content"]//p//text()').extract())
        item['doi'] = response.xpath('//meta[@name="prism.doi"]/@content').get()
        item['authors'] = response.xpath('//meta[@name="citation_author"]//@content').extract()
        # item['AffiliationInfo'] = response.xpath('//meta[@name="citation_author_institution"]/@content').extract()
        item['if_2017'] = 11.64
        item['issn'] = response.xpath('//meta[@name="citation_issn"]/@content').get()
        yield item


class JemSpider(scrapy.Spider):
    name = 'sigle4'
    # allowed_domains = ['www.cambridge.org']
    start_urls = ['http://jem.rupress.org/newest']

    def parse(self, response):
        detail_urls = response.xpath('//ul//li//div//a//@href').extract()
        for detail_url in detail_urls:
            request_url = 'http://jem.rupress.org' + detail_url
            print(request_url)
            request = Request(url=request_url, callback=self.parse_info, dont_filter=True)
            request.meta['link'] = request_url
            yield request

    def parse_info(self, response):
        item = CellItem()
        item['title'] = response.xpath('//meta[@name="citation_title"]//@content').extract_first()
        item['link'] = response.meta['link']
        item['source'] = "The Journal of experimental medicine"
        item['pub_date'] = response.xpath('//meta[@name="DC.Date"]/@content').get()
        item['abstract'] = strip_tag(response.xpath('//meta[@name="og:description"]/@content').get())
        item['doi'] = response.xpath('//meta[@name="DC.Identifier"]/@content').get()
        item['authors'] = response.xpath('//meta[@name="citation_author"]//@content').extract()
        # item['AffiliationInfo'] = response.xpath('//meta[@name="citation_author_institution"]/@content').extract()
        item['if_2017'] = 10.79
        item['issn'] = response.xpath('//meta[@name="citation_issn"]/@content').extract()[1]
        yield item

class AtsjournalsSpider(scrapy.Spider):
    name = 'sigle5'
    # allowed_domains = ['www.cambridge.org']
    start_urls = ['https://www.atsjournals.org/toc/ajrccm/0/ja']

    def parse(self, response):
        detail_urls = response.xpath('//div[@class="art_title linkable"]//a//@href').extract()
        for detail_url in detail_urls:
            request_url = 'https://www.atsjournals.org' + detail_url
            print(request_url)
            request = Request(url=request_url, callback=self.parse_info, dont_filter=True)
            request.meta['link'] = request_url
            yield request

    def parse_info(self, response):
        item = CellItem()
        item['title'] = response.xpath('//meta[@name="dc.Title"]//@content').extract_first()
        item['link'] = response.meta['link']
        item['source'] = 'American journal of respiratory and critical care medicine'
        item['pub_date'] = response.xpath('//meta[@name="dc.Date"]/@content').get()
        item['abstract'] = strip_tag(response.xpath('//div[@class="hlFld-Abstract"]//p//text() ').extract()) or\
                           strip_tag(response.xpath('//div[@class="abstract"]//p//text()').extract())
        item['doi'] = response.xpath('//meta[@name="dc.Identifier"]/@content').get()
        item['authors'] = response.xpath('//meta[@name="dc.Creator"]//@content').extract()
        # item['AffiliationInfo'] = response.xpath('//meta[@name="citation_author_institution"]/@content').extract()
        item['if_2017'] = 15.239
        item['issn'] = '1535-4970'
        yield item


class OnlinejaccSpider(scrapy.Spider):
    name = 'sigle6'
    # allowed_domains = ['www.cambridge.org']
    start_urls = ['http://www.onlinejacc.org/content/72/6?current-issue=y']
    def parse(self, response):
        detail_urls = response.xpath('//div[@class="toc-citation"]//a[@class="highwire-cite-linked-title"]//@href').extract()
        for detail_url in detail_urls:
            request_url = 'https://www.onlinejacc.org' + detail_url
            print(request_url)
            request = Request(url=request_url, callback=self.parse_info, dont_filter=True)
            request.meta['link'] = request_url
            yield request

    def parse_info(self, response):
        item = CellItem()
        item['title'] = response.xpath('//meta[@name="citation_title"]//@content').extract_first()
        item['link'] = response.meta['link']
        item['source'] = "Journal of the American College of Cardiology"
        item['pub_date'] = response.xpath('///meta[@name="DC.Date"]/@content').get()
        item['abstract'] = strip_tag(response.xpath('//meta[@name="DC.Description"]/@content').extract())
        item['doi'] = response.xpath('//meta[@name="DC.Identifier"]/@content').get()
        item['authors'] = response.xpath('//meta[@name="DC.Contributor"]//@content').extract()
        # item['AffiliationInfo'] = response.xpath('//meta[@name="citation_author_institution"]/@content').extract()
        item['if_2017'] = 16.834
        item['issn'] = response.xpath('//meta[@name="citation_issn"]/@content').extract()[1]
        yield item


class AhajournalSpider(scrapy.Spider):
    name = 'sigle7'
    # allowed_domains = ['www.cambridge.org']
    start_urls = ['https://www.ahajournals.org/toc/circ/0/0']

    def parse(self, response):
        detail_urls = set(response.xpath('//div//div[@class="article-meta"]//a//@href').extract())
        for detail_url in detail_urls:
            request_url = 'https://www.ahajournals.org' + detail_url
            print(request_url)
            request = Request(url=request_url, callback=self.parse_info, dont_filter=True)
            request.meta['link'] = request_url
            yield request

    def parse_info(self, response):
        item = CellItem()
        item['title'] = response.xpath('//meta[@name="dc.Title"]//@content').extract_first().strip('\n')
        item['link'] = response.meta['link']
        item['source'] = "Circulation"
        item['pub_date'] = tranfrom_date(response.xpath('//div[@class="epub-section"]//span[@class="epub-section__date"]//text()').get())
        item['abstract'] = strip_tag(response.xpath('//div[@class="hlFld-Abstract"]//p//text()').extract())
        item['doi'] = doi_str(response.xpath('//input[@name="redirectUri"]//@value').get())
        item['authors'] = response.xpath('//meta[@name="dc.Creator"]//@content').extract()
        # item['AffiliationInfo'] = response.xpath('//meta[@name="citation_author_institution"]/@content').extract()
        item['if_2017'] = 18.88
        item['issn'] = response.xpath('//meta[@name="citation_issn"]/@content').extract() or "0009-7322"
        yield item


class EuropeanurologySpider(scrapy.Spider):
    name = 'sigle8'
    # allowed_domains = ['www.cambridge.org']
    start_urls = ['https://www.europeanurology.com/inpress']

    def parse(self, response):
        detail_urls = response.xpath('//div[@class="articleTitle"]//a//@href').extract()
        for detail_url in detail_urls:
            request_url = 'https://www.europeanurology.com' + detail_url
            print(request_url)
            request = Request(url=request_url, callback=self.parse_info, dont_filter=True)
            request.meta['link'] = request_url
            yield request

    def parse_info(self, response):
        item = CellItem()
        item['title'] = response.xpath('//meta[@name="citation_title"]//@content').extract_first()
        item['link'] = response.meta['link']
        item['source'] = "European urology"
        item['pub_date'] = tranfrom_date1(response.xpath('//meta[@name="citation_online_date"]/@content').get())
        item['abstract'] = strip_tag(response.xpath('//div[@class="content"]//text()').extract())
        item['doi'] = response.xpath('//meta[@name="citation_doi"]/@content').get()
        item['authors'] = response.xpath('//meta[@name="citation_author"]//@content').extract()
        # item['AffiliationInfo'] = response.xpath('//meta[@name="citation_author_institution"]/@content').extract()
        item['if_2017'] = 17.581
        item['issn'] = response.xpath('//meta[@name="citation_issn"]/@content').extract()[0]
        yield item


class BloodSpider(scrapy.Spider):
    name = 'sigle9'
    # allowed_domains = ['www.cambridge.org']
    start_urls = ['http://www.bloodjournal.org/content/early/recent']

    def parse(self, response):
        detail_urls = response.xpath('//div[@class="pane-content"]//li[@class="first odd"]//a//@href').extract()
        for detail_url in detail_urls:
            request_url = 'http://www.bloodjournal.org' + detail_url
            print(request_url)
            request = Request(url=request_url, callback=self.parse_info, dont_filter=True)
            request.meta['link'] = request_url
            yield request

    def parse_info(self, response):
        item = CellItem()
        item['title'] = response.xpath('//meta[@name="citation_title"]//@content').extract_first()
        item['link'] = response.meta['link']
        item['source'] = "Blood"
        item['pub_date'] = response.xpath('//meta[@name="DC.Date"]/@content').get()
        item['abstract'] = strip_tag(response.xpath('///meta[@name="citation_abstract"]/@content').extract())
        item['doi'] = response.xpath('//meta[@name="citation_doi"]/@content').get()
        item['authors'] = response.xpath('//meta[@name="citation_author"]//@content').extract()
        # item['AffiliationInfo'] = response.xpath('//meta[@name="citation_author_institution"]/@content').extract()
        item['if_2017'] = 15.132
        item['issn'] = response.xpath('//meta[@name="citation_issn"]/@content').extract()[0]
        yield item


class JacionlineSpider(scrapy.Spider):
    name = 'sigle10'
    # allowed_domains = ['www.cambridge.org']
    start_urls = ['https://www.jacionline.org/inpress']

    def parse(self, response):
        detail_urls = response.xpath('//div[@class="articleTitle"]//a//@href').extract()
        for detail_url in detail_urls:
            request_url = 'https://www.jacionline.org' + detail_url
            print(request_url)
            request = Request(url=request_url, callback=self.parse_info, dont_filter=True)
            request.meta['link'] = request_url
            yield request

    def parse_info(self, response):
        item = CellItem()
        item['title'] = strip_tag(response.xpath('//meta[@name="citation_title"]//@content').extract_first())
        item['link'] = response.meta['link']
        item['source'] = "The Journal of allergy and clinical immunology"
        item['pub_date'] = tranfrom_date1(response.xpath('//meta[@name="citation_online_date"]/@content').get())
        item['abstract'] = strip_tag(response.xpath('//div[@class="content"]//text()').extract())
        item['doi'] = response.xpath('//meta[@name="citation_doi"]/@content').get()
        item['authors'] = response.xpath('//meta[@name="citation_author"]//@content').extract()
        # item['AffiliationInfo'] = response.xpath('//meta[@name="citation_author_institution"]/@content').extract()
        item['if_2017'] = 13.258
        item['issn'] = response.xpath('//meta[@name="citation_issn"]/@content').extract()[0]
        yield item


class ErjSpider(scrapy.Spider):
    name = 'sigle11'
    # allowed_domains = ['www.cambridge.org']
    start_urls = ['http://erj.ersjournals.com/content/early/recent']

    def parse(self, response):
        detail_urls = response.xpath('//div[@class="pane-content"]//li//div//a//@href').extract()
        for detail_url in detail_urls:
            request_url = 'http://erj.ersjournals.com' + detail_url
            print(request_url)
            request = Request(url=request_url, callback=self.parse_info, dont_filter=True)
            request.meta['link'] = request_url
            yield request

    def parse_info(self, response):
        item = CellItem()
        item['title'] = response.xpath('//meta[@name="citation_title"]//@content').extract_first()
        item['link'] = response.meta['link']
        item['source'] = "The European respiratory journal"
        item['pub_date'] = response.xpath('//meta[@name="article:published_time"]/@content').get()
        item['abstract'] = strip_tag(response.xpath('//meta[@name="DC.Description"]/@content').extract())
        item['doi'] = response.xpath('//meta[@name="citation_doi"]/@content').get()
        item['authors'] = response.xpath('//meta[@name="citation_author"]//@content').extract()
        # item['AffiliationInfo'] = response.xpath('//meta[@name="citation_author_institution"]/@content').extract()
        item['if_2017'] = 12.242
        item['issn'] = response.xpath('//meta[@name="citation_issn"]/@content').extract()[1]
        yield item


class HepatologySpider(scrapy.Spider):
    name = 'sigle12'
    # allowed_domains = ['www.cambridge.org']
    start_urls = ['https://www.journal-of-hepatology.eu/inpress']
    def parse(self, response):
        detail_urls = response.xpath('//div[@class="articleTitle"]//a//@href').extract()
        for detail_url in detail_urls:
            request_url = 'https://www.journal-of-hepatology.eu' + detail_url
            print(request_url)
            request = Request(url=request_url, callback=self.parse_info, dont_filter=True)
            request.meta['link'] = request_url
            yield request

    def parse_info(self, response):
        item = CellItem()
        item['title'] = response.xpath('//meta[@name="citation_title"]//@content').extract_first()
        item['link'] = response.meta['link']
        item['source'] = "Journal of hepatology"
        item['pub_date'] = tranfrom_date1(response.xpath('//meta[@name="citation_online_date"]/@content').get())
        item['abstract'] = strip_tag(response.xpath('//div[@class="content"]//text()').extract())
        item['doi'] = response.xpath('//meta[@name="citation_doi"]/@content').get()
        item['authors'] = response.xpath('//meta[@name="citation_author"]//@content').extract()
        # item['AffiliationInfo'] = response.xpath('//meta[@name="citation_author_institution"]/@content').extract()
        item['if_2017'] = 14.911
        item['issn'] = response.xpath('//meta[@name="citation_issn"]/@content').extract()[0]
        yield item

class AjpSpider(scrapy.Spider):
    name = 'sigle13'
    # allowed_domains = ['www.cambridge.org']
    start_urls = ['https://ajp.psychiatryonline.org/toc/ajp/0/0']

    def parse(self, response):
        detail_urls = response.xpath('//div[@class="issue-item"]//h5//a//@href').extract()
        for detail_url in detail_urls:
            request_url = 'https://ajp.psychiatryonline.org' + detail_url
            print(request_url)
            request = Request(url=request_url, callback=self.parse_info, dont_filter=True)
            request.meta['link'] = request_url
            yield request

    def parse_info(self, response):
        item = CellItem()
        item['title'] = response.xpath('//meta[@name="dc.Title"]//@content').extract_first()
        item['link'] = response.meta['link']
        item['source'] = 'The American journal of psychiatry'
        item['pub_date'] = response.xpath('//meta[@name="dc.Date"]/@content').get()
        item['abstract'] = strip_tag(response.xpath('//div[@class="abstractSection abstractInFull"]//p//text()').extract())
        item['doi'] = response.xpath('//meta[@name="dc.Identifier"]/@content').extract()[1]
        item['authors'] = response.xpath('//meta[@name="dc.Creator"]//@content').extract()
        # item['AffiliationInfo'] = response.xpath('//meta[@name="citation_author_institution"]/@content').extract()
        item['if_2017'] = 13.391
        item['issn'] = '1535-7228'
        yield item


class AnnalsSpider(scrapy.Spider):
    name = 'sigle14'
    # allowed_domains = ['elifesciences.org']
    start_urls = ['http://annals.org/aim/latest']
    def parse(self, response):
        detail_urls = response.xpath('//div[@class="text-links"]//a//@href').extract()
        for detail_url in detail_urls:
            request_url = detail_url
            print(request_url)
            request = Request(url=request_url, callback=self.parse_info, dont_filter=True)
            request.meta['link'] = request_url
            yield request

    def parse_info(self, response):
        item = CellItem()
        item['title'] = response.xpath('//meta[@name="citation_title"]/@content').extract_first()
        item['link'] = response.meta['link']
        item['source'] = "Annals of internal medicine"
        item['pub_date'] = tranfrom_date(response.xpath('//span[@class="wi-pub-date large-view-only"]//text()').extract()[2].strip())
        item['abstract'] = strip_tag(response.xpath('//div[@class="typed para"]//text()').extract())or response.xpath('//section[@class="abstract"]//p//text()').extract_first()
        item['doi'] = response.xpath('//meta[@name="citation_doi"]/@content').get()
        item['authors'] = response.xpath('//meta[@name="citation_author"]/@content').extract()
        # item['AffiliationInfo'] = response.xpath('//meta[@name="citation_author_institution"]/@content').extract()
        item['if_2017'] = 19.384
        # "issnPrint" : "0003-4819"
        item['issn'] = "1539-3704"
        yield item


class AscopubsSpider(scrapy.Spider):
    name = 'sigle15'
    # allowed_domains = ['elifesciences.org']
    start_urls = ['http://ascopubs.org/toc/jco/current']
    def parse(self, response):
        detail_urls = response.xpath('//div[@class="art_title linkable"]//a//@href').extract()
        for detail_url in detail_urls:
            request_url = 'http://ascopubs.org' + detail_url
            print(request_url)
            request = Request(url=request_url, callback=self.parse_info, dont_filter=True)
            request.meta['link'] = request_url
            request.meta['detail_url'] = detail_url
            yield request

    def parse_info(self, response):
        item = CellItem()
        item['title'] = strip_tag(response.xpath('//div[@class="publicationContentTitle"]//h1//text()').extract()).strip()
        item['link'] = response.meta['link']
        item['source'] = "Journal of clinical oncology : official journal of the American Society of Clinical Oncology"
        item['pub_date'] = response.xpath('//meta[@name="dc.Date"]/@content').get()
        item['abstract'] = strip_tag(response.xpath('//div[@class="abstractSection abstractInFull"]//text()').extract())
        item['doi'] = response.meta['detail_url']
        item['authors'] = response.xpath('//div[@class="header"]//text()').extract()
        # item['AffiliationInfo'] = response.xpath('//meta[@name="citation_author_institution"]/@content').extract()
        item['if_2017'] = 26.303
        item['issn'] = "1527-7755"
        yield item


class AstroSpider(scrapy.Spider):
    name = 'sigle16'
    # allowed_domains = ['elifesciences.org']
    start_urls = ['https://www.gastrojournal.org']
    def parse(self, response):
        detail_urls = response.xpath('//div[@class="articleTitle"]//a//@href').extract()
        for detail_url in detail_urls:
            request_url = 'https://www.gastrojournal.org' + detail_url
            print(request_url)
            request = Request(url=request_url, callback=self.parse_info, dont_filter=True)
            request.meta['link'] = request_url
            yield request

    def parse_info(self, response):
        item = CellItem()
        item['title'] = response.xpath('//meta[@name="citation_title"]/@content').extract_first()
        item['link'] = response.meta['link']
        item['source'] = "Gastroenterology"
        item['pub_date'] = tranfrom_date1(response.xpath('//meta[@name="citation_online_date"]/@content').get()) or \
                           tranfrom_date1(response.xpath('//meta[@name="citation_date"]/@content').get())
        item['abstract'] = strip_tag(response.xpath('//meta[@name="citation_abstract"]/@content').extract()) or\
                           strip_tag(response.xpath('//div[@class="content"]//text()').extract())
        item['doi'] = response.xpath('//meta[@name="citation_doi"]/@content').get()
        item['authors'] = response.xpath('//meta[@name="citation_author"]/@content').extract()
        # item['AffiliationInfo'] = response.xpath('//meta[@name="citation_author_institution"]/@content').extract()
        item['if_2017'] = 20.773
        item['issn'] = response.xpath('//meta[@name="citation_issn"]/@content').extract()[0]
        yield item


class OnlinelibrarySpider(scrapy.Spider):
    name = 'sigle17'
    # allowed_domains = ['elifesciences.org']
    start_urls = ['https://onlinelibrary.wiley.com/journal/15424863']
    def parse(self, response):
        detail_urls = response.xpath('//div[@class="issue-item"]/a//@href').extract()
        for detail_url in detail_urls:
            request_url = 'https://onlinelibrary.wiley.com' + detail_url
            print(request_url)
            request = Request(url=request_url, callback=self.parse_info, dont_filter=True)
            request.meta['link'] = request_url
            yield request

    def parse_info(self, response):
        item = CellItem()
        item['title'] = response.xpath('//meta[@name="citation_title"]/@content').extract_first()
        item['link'] = response.meta['link']
        item['source'] = "CA: a cancer journal for clinicians"
        item['pub_date'] = tranfrom_date(response.xpath('//div//span[@class="epub-date"]//text()').get())
        item['abstract'] = strip_tag(response.xpath('//div[@class="article-section__content"]/p/text()').extract())or\
                           strip_tag(response.xpath('//section//div[@class="article-section__content en main"]//p//text()').extract())
        item['doi'] = response.xpath('//meta[@name="citation_doi"]/@content').get()
        item['authors'] = response.xpath('//meta[@name="citation_author"]/@content').extract()
        # item['AffiliationInfo'] = response.xpath('//meta[@name="citation_author_institution"]/@content').extract()
        # "issnPrint" : "0007-9235",
        item['if_2017'] = 244.585
        item['issn'] = "1542-4863"
        yield item

