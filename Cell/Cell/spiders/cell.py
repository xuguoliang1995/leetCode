import re
import scrapy
from scrapy import Request
from Cell.items import CellItem


def strip_tag(s):
    if s:
        fr = re.compile(r'</?\w+[^>]*>', re.S)
        dr = fr.sub('', s).replace('\xa0', "")
        return dr
    return ""


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


class CellSpider(scrapy.Spider):
    name = 'cell'
    # allowed_domains = ['www.cell.com']
    # start_urls = ['http://www.cell.com/cell/current',
    #               'https://www.cell.com/cell-host-microbe/current']

    def start_requests(self):
        urls = [
            'https://www.cell.com/cell/current',
            'https://www.cell.com/cell-host-microbe/current',
            'https://www.cell.com/cell/newarticles',
            'https://www.cell.com/neuron/newarticles',
            'http://www.cell.com/cell-metabolism/issue?pii=S1550-4131(16)X0007-1',
            'http://www.cell.com/stem/newarticles',
            'http://www.cell.com/cell-stem-cell/current',
            'http://www.cell.com/cell-host-microbe/newarticles',
            'http://www.cell.com/molecular-cell/current',
            'http://www.cell.com/molecular-cell/newarticles',
            'http://www.cell.com/immunity',
            'https://www.cell.com/cancer-cell/newarticles',
            'https://www.cell.com/cell-metabolism/newarticles',
        ]
        for url in urls:
            yield Request(url=url, dont_filter=True)

    def make_requests_from_url(self, url):
        """ This method is deprecated. """
        return Request(url, dont_filter=True)

    def parse(self, response):
        detail_urls = response.xpath('//div//div[@class="articleTitle"]//a//@href').extract()
        for detail_url in detail_urls:
            header_url = 'https://www.cell.com'
            request_url = header_url + detail_url
            print(request_url)
            request = Request(url=request_url, callback=self.parse_info, dont_filter=True)
            request.meta['link'] = request_url
            yield request
        print('#' * 30)

    def parse_info(self, response):
        item = CellItem()
        item['title'] = strip_tag(response.xpath('//meta[@name="citation_title"]/@content').extract_first())
        item['link'] = response.meta['link']
        issn = response.xpath('//meta[@name="citation_issn"]/@content').extract()[0] or ""
        item['issn'] = issn
        if issn == "0092-8674":
            item['if_2017'] = 31.398
            item['source'] = "Cell"
        elif issn == "1931-3128":
            item['if_2017'] = 17.872
            item['source'] = "Cell host & microbe"
        elif issn == "1097-2765":
            item['if_2017'] = 14.248
            item['source'] = "Molecular cell"
        elif issn == "1074-7613":
            item['if_2017'] = 19.734
            item['source'] = "Immunity"
        elif issn == "1535-6108":
            item['if_2017'] = 22.844
            item['source'] = "Cancer cell"
        elif issn == "1550-4131":
            item['if_2017'] = 20.565
            item['source'] = "Cell metabolism"
        elif issn == "1471-4906":
            item['if_2017'] = 14.188
            item['source'] = "Trends in immunology"
        elif issn == "1471-4914":
            item['if_2017'] = 11.021
            item['source'] = "Trends in molecular medicine"
        elif issn == "0896-6273":
            item['if_2017'] = 14.318
            item['source'] = "Neuron"
        elif issn == "1934-5909":
            item['if_2017'] = 23.29
            item['source'] = "Cell stem cell"
        item['pub_date'] = tranfrom_date(response.xpath('//meta[contains(@name, "date")]/@content').get())
        item['abstract'] = handler_abstract(
            response.xpath('//div[@id="article"]//div[@class="content"]//p/text()').extract()) or \
                           strip_tag(response.xpath('//meta[@name="citation_abstract"]/@content').get()) or ""
        item['doi'] = response.xpath('//meta[@name="citation_doi"]/@content').get()
        item['authors'] = response.xpath('//meta[@name="citation_author"]/@content').extract()
        item["is_pubmed"] = 0
        # item['AffiliationInfo'] = response.xpath('//meta[@name="citation_author_institution"]').get()
        yield item


