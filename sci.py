import random
from lxml import etree
import requests
import redis

def get_url():
    url = "http://tool.yovisun.com/scihub/"
    user_agent = [
                  "Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
                  "Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
                  "Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
                  "Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11",
                  "Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11",
                  "Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11",
                  "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Maxthon2.0)",
                  "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)",
                  "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)",
                  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"
                  ]
    headers = {
                  "User-Agent":random.choice(user_agent),
                  "Host": "tool.yovisun.com",
              }
    response = requests.get(url=url,headers=headers)
    text = response.text
    tree = etree.HTML(text)
    link = tree.xpath('//body//div//div//table//td[@class="domain"]//a//text()')
    return link

def connect_redis(links):
    redis_config = {
        "host": "119.254.209.50",
        "port": 6379,
        "password":"Qidian2016"

    }
    redis_conn = redis.Redis(**redis_config )
    for link in links:
        redis_conn.sadd('link',link)
    
    query_link = redis_conn.smembers("link")
    count = redis_conn.scard("link")
    print(query_link,count)

connect_redis(get_url())































