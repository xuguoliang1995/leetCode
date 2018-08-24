import re
import scrapy
from scrapy import Request
from nature.items import NatureItem


def strip_tag(s):
    if s:
        fr = re.compile(r'<[^>]+>',re.S)
        dr = fr.sub('',s)
        return dr
    return ""


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
        for detail_url in detail_urls:
            if "http" in detail_url:
                print("我打印出来了", detail_url)
                continue
            else:
                head_url = "https://www.nature.com"
                request_url = head_url + detail_url
                request = Request(url=request_url, callback=self.parse_info, dont_filter=True)
                request.meta['link'] = request_url
                yield request

    def parse_info(self, response):
        item = NatureItem()
        item['title'] = strip_tag(response.xpath('//meta[@name="dc.title"]/@content').extract_first())
        item['link'] = response.meta['link']
        issn = response.xpath('//meta[@name="prism.issn"]/@content').get() or ""
        item['issn'] = issn
        if issn == "1476-4687":
            item['source'] = "Nature"
            item['if_2017'] = 41.577
        elif issn == "1546-1696":
            item['source'] = "Nature biotechnology"
            item['if_2017'] = 35.724
        elif issn == "1546-1718":
            item['source'] = "Nature genetics"
            item['if_2017'] = 27.125
        elif issn == "2058-5276":
            item['source'] = "Nature microbiology"
            item['if_2017'] = 14.174
        elif issn == "2041-1723":
            item['source'] = "Nature communications"
            item['if_2017'] = 12.353
        elif issn == "1476-4679":
            item['if_2017'] = 19.064
            item['source'] = "Nature cell biology"
        elif issn == "1529-2916":
            item['if_2017'] = 21.809
            item['source'] = "Nature immunology"
        elif issn == "1546-170X":
            item['if_2017'] = 32.621
            item['source'] = "Nature medicine"
        elif issn == "1748-3395":
            item['if_2017'] = 37.49
            item['source'] = "Nature nanotechnology"
        elif issn == "1759-5010":
            item['if_2017'] = 1.714
            item['source'] = "Nature reviews. Cardiology"
        elif issn == "1759-4782":
            item['if_2017'] = 3.055
            item['source'] = "Nature reviews. Clinical oncology"
        elif issn == "1474-1768":
            item['if_2017'] = 42.784
            item['source'] = "Nature reviews. Cancer"
        elif issn == "1476-5551":
            item['if_2017'] = 10.023
            item['source'] = "Leukemia"
        elif issn == "1546-1726":
            item['if_2017'] = 19.912
            item['source'] = "Nature neuroscience"
        elif issn == "1476-4660":
            item['if_2017'] = 39.235
            item['source'] = "Nature materials"
        item['pub_date'] = response.xpath('//meta[@name="dc.date"]/@content').get()
        item['abstract'] = handler_abstract(response.xpath('//section[@aria-labelledby="abstract"]//div//p//text()').extract()) or\
                           handler_abstract(response.xpath('//section[@aria-labelledby="Abs1"]//div//p//text()').extract())\
                           or handler_abstract(response.xpath('//div[@class="pl20 mq875-pl0 serif"]/p//text()').extract())\
                           or response.xpath('//meta[@property="og:description"]//@content').get() or ""
        item['doi'] = response.xpath('//meta[@name="citation_doi"]/@content').get() or\
                      response.xpath('//meta[@name="prism.doi"]/@content').get().split(':')[1]
        item['authors'] = response.xpath('//meta[@name="citation_author"]/@content').extract() or\
                        response.xpath('//meta[@name="dc.creator"]/@content').get() or ""
        yield item

