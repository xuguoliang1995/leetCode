
import random
from scrapy import signals
from scrapy.exceptions import NotConfigured


class RandomProxyMiddleware(object):
    """随机动态IP代理池"""

    def __init__(self, settings):
        # 2. 判断是否配置了IP代理池
        if not settings.getlist('PROXIES'):
            raise NotConfigured
        # 从配置里读取出来
        self.proxies = settings.getlist('PROXIES')
        # 设置代理IP的错误统计，默认设置为0
        self.stats = {}.fromkeys(self.proxies, 0)
        # 最大失败次数
        self.max_failed = 3

    @classmethod
    def from_crawler(cls, crawler):
        # 1. 首先判断是否启用了proxy
        if not crawler.settings.getbool('HTTPPROXY_ENABLED'):
            raise NotConfigured
        # 创建中间件对象
        return cls(crawler.settings)

    def process_request(self, request, spider):
        # 3. 随机设置一个代理
        # 通过设置meta内的proxy属性，利用系统本身的proxy中间件去实现代理
        if 'proxy' not in request.meta:
            proxy_url = random.choice(self.proxies)
            request.meta['proxy'] = proxy_url

    def remove_proxy(self, proxy):
        if proxy in self.proxies:
            self.proxies.remove(proxy)
            print('proxy %s removed from proxies list' % proxy)

    def process_response(self, request, response, spider):
        # 4. 代理正常，但对方服务器返回了错误的状态码，有可能是被封掉
        cur_proxy = request.meta['proxy']
        if response.status != 200:
            print('none 200 status code: %s when use %s'
                  % (response.status, cur_proxy))
        if response.status >= 400:
            self.stats[cur_proxy] += 1
        # 如果异常status在该代理上出现了N次，也从代理池中删除
        if self.stats[cur_proxy] >= self.max_failed:
            self.remove_proxy(cur_proxy)
            # 删除当前request对象的代理，并返回重新调度下载
            del request.meta['proxy']
            return request
        # 如果一切正常，返回response对象，以让下面的中间件继续执行。
        return response

    def process_exception(self, request, exception, spider):
        # 4. 如果代理不可用，则会触发此方法
        cur_proxy = request.meta['proxy']
        # print一下异常信息
        print('raise exception: %s when use %s' % (exception, cur_proxy))
        # 从代理池中删除该代理
        self.remove_proxy(cur_proxy)
        # 删除当前request对象的代理，并返回重新调度下载
        del request.meta['proxy']
        return request


class JamanetworkSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class JamanetworkDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
