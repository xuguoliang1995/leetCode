
# import re
# import scrapy
# from scrapy import Request
# from Cell.items import CellItem
# import time
#
# def strip_tag(str_s):
#     new_dr = ""
#     for s in str_s:
#         if s:
#             s = s.replace('\n',"").replace('\xa0',"").replace('\u2005',"")
#             fr = re.compile(r'<[^>]+>',re.S)
#             dr = fr.sub('',s)
#             for i in dr:
#                 new_dr = new_dr + i
#     new_dr = re.sub(r"\s{2,}", "", new_dr)
#     return new_dr


# class CambridgetSpider(scrapy.Spider):
#     name = 'sigle2'
#     # allowed_domains = ['www.cambridge.org']
#     # start_urls = ['https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/latest-issue']
#     def start_requests(self):
#         start_urls = 'https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/latest-issue'
#         yield Request(start_urls,dont_filter=True)
#     def make_requests_from_url(self, url):
#         url = "https://www.cambridge.org/cdn-cgi/l/chk_jschl?jschl_vc=4e9598abdf62a163b02c29b0bbc515ae&pass=1533722044.845-Y5GrrUIdqO&jschl_answer=211.8857270428"
#         return Request(url,dont_filter=True,)
#
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
#         item['if_2017'] = "15.071"
#         item['issn'] = response.xpath('//meta[@name="citation_issn"]/@content').extract()[1]
#         yield item



# import requests
# from bs4 import BeautifulSoup
# url = "https://www.cambridge.org"
# headers = {
#      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
#      "referer":"https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/latest-issue"
# }
#
# # data = {
# #     "a" :"4e9598abdf62a163b02c29b0bbc515ae&pass=1533722044.845-Y5GrrUIdqO",
# #     "jschl_answer":"211.8857270428"
# # }
# response = requests.get(url,headers=headers)
# text = response.text
# print(text)
# soup = BeautifulSoup(text, "lxml")
# hideen_tags = soup.find_all("input",type="hidden")
# print(hideen_tags)
# d = {}
# d["jschl_vc"] = hideen_tags[0].attrs.get("value")
# d["pass"] = hideen_tags[1].attrs.get('value')
# print(d)

# class Countdown:
#     def __init__(self,start):
#         self.start = start
#     def __iter__(self):
#         n = self.start
#         while n > 0:
#             yield n
#             n -= 1
#     def __reversed__(self):
#         n = 1
#         while n < self.start:
#             yield n
#             n += 1
#
#
# if __name__ == "__main__":
























