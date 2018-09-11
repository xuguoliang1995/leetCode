# import datetime
# import re
# import time
# from lxml import etree
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
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
#
#
# def tranfrom_date(t):
#     if t:
#         year,month,day = t.split('/')
#         return '%s-%s-%s' % (year,month,day)
#     return ""
#
#
# def share_browser():
#     chrome_options = Options()
#     chrome_options.add_argument('--headless')
#     chrome_options.add_argument('--disable-gpu')
#     browser = webdriver.Chrome(chrome_options=chrome_options)
#     return browser
# def html_parse():
#     brower = share_browser()
#     host = "https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/latest-issue"
#     brower.get(host)
#     time.sleep(10)
#     soup = BeautifulSoup(brower.page_source, "lxml")
#     request_urls = soup.select("ul  li .part-link")
#     spider = []
#     for url in request_urls:
#         request_url = "https://www.cambridge.org" + url.attrs.get("href")
#         print(request_url)
#         brower.get(request_url)
#         time.sleep(10)
#         text = brower.page_source
#         html = etree.HTML(text)
#         item = {}
#         item['title'] = html.xpath('//meta[@name="citation_title"]//@content')[0]
#         item['link'] = request_url
#         item['source'] = "The Behavioral and brain sciences"
#         item['pub_date'] = tranfrom_date(html.xpath('///meta[@name="citation_online_date"]/@content')[0])
#         item['abstract'] = strip_tag(html.xpath('//div[@class="abstract"]//p//text()'))
#         item['doi'] = html.xpath('//meta[@name="dc.identifier"]/@content')[0].split(":")[1]
#         item['authors'] = html.xpath('//meta[@name="citation_author"]//@content')
#         # item['AffiliationInfo'] = response.xpath('//meta[@name="citation_author_institution"]/@content').extract()
#         item['if_2017'] = 15.071
#         # "issnPrint": "0140-525X"
#         item['issn'] = "1469-1825"
#         item["created_at"] = datetime.datetime.utcnow()
#         item["updated_at"] = datetime.datetime.utcnow()
#         print(item)
#         spider.append(item)
#     return spider
#
#
# spider = html_parse()
# print(spider)
#
