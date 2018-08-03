import re
import scrapy
from scrapy import Request
from nature.items import NatureItem


def strip_tag(s):
    if s:
        fr = re.compile(r'<[^>]+>',re.S)
        dr = fr.sub('',s)
        return dr
    return " "


def handler_abstract(extract_list):
    new_str = ""
    if extract_list:
        for i in extract_list:
            new_str = new_str + i
            new_str = new_str.replace('\n','').replace('\u2009.','').replace('\u202f',"")
        return new_str
    return ""


class ImmunologySpider(scrapy.Spider):
    name = 'immunology'
    # allowed_domains = ['www.nature.com/ni/research']
    start_urls = [
                'http://www.nature.com/nature/research/biological-sciences.html',
                'https://www.nature.com/nbt/research',
                'http://www.nature.com/nbt/newsandcomment/index.html',
                'https://www.nature.com/ng/research',
                'http://www.nature.com/ni/research/index.html',
                'http://www.nature.com/nm/research/index.html',
                'http://www.nature.com/nmicrobiol/news-and-comment',
                'http://www.nature.com/nmicrobiol/research',
                'http://www.nature.com/nnano/newsandcomment/index.html',
                'http://www.nature.com/nnano/research/index.html',
                'http://www.nature.com/neuro/research/index.html',
                'http://www.nature.com/neuro/newsandcomment/index.html',
                'https://www.nature.com/ncomms/articles',
                'https://www.nature.com/ncomms/research',
                'https://www.nature.com/nmat/research',
                'https://www.nature.com/ncb/research',
                'https://www.nature.com/mp/articles'
                'http://www.nature.com/ng/newsandcomment/index.html',
                'http://www.nature.com/ni/newsandcomment/index.html',
                'http://www.nature.com/nm/newsandcomment/index.html',
                'https://www.nature.com/nrcardio',
                'https://www.nature.com/nrclinonc',
                'https://www.nature.com/nrc',
                'http://www.nature.com/leu/current_issue/rss/index.html',
                ]

    def parse(self, response):
        detail_urls = response.xpath('//div//ul//li//h3//a//@href').extract()
        count = 0
        for detail_url in detail_urls:
            head_url = 'https://www.nature.com'
            request_url = head_url + detail_url
            print(request_url)
            count += 1
            request = Request(url=request_url, callback=self.parse_info, dont_filter=True)
            request.meta['link'] = request_url
            yield request
        print("*"*30,count)
    def parse_info(self, response):
        item = NatureItem()
        item['title'] = strip_tag(response.xpath('//meta[@name="dc.title"]/@content').extract_first())
        item['link'] = response.meta['link']
        item['source'] = response.xpath('//meta[@name="dc.source"]/@content').get()
        item['pub_date'] = response.xpath('//meta[@name="dc.date"]/@content').get()
        item['abstract'] = handler_abstract(response.xpath('//section[@aria-labelledby="abstract"]//div//p//text()').extract()) or\
                           handler_abstract(response.xpath('//section[@aria-labelledby="Abs1"]//div//p//text()').extract())\
                           or handler_abstract(response.xpath('//div[@class="pl20 mq875-pl0 serif"]/p//text()').extract())\
                           or response.xpath('//meta[@property="og:description"]//@content').get() or ""
        item['doi'] = response.xpath('//meta[@name="citation_doi"]/@content').get() or\
                      response.xpath('//meta[@name="prism.doi"]/@content').get()
        item['authors'] = response.xpath('//meta[@name="citation_author"]/@content').extract() or\
                        response.xpath('//meta[@name="dc.creator"]/@content').get() or ""
        item['_if'] = ""
        item['issn'] = response.xpath('//meta[@name="prism.issn"]/@content').get() or ""
        yield item

