
BOT_NAME = 'Jamanetwork'
SPIDER_MODULES = ['Jamanetwork.spiders']
NEWSPIDER_MODULE = 'Jamanetwork.spiders'

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'

ROBOTSTXT_OBEY = False
FEED_EXPORT_ENCODING = 'utf-8'

LOG_LEVEL = 'DEBUG'
LOG_FILE= '../json/name.log'

# 代服务器的设置。
PROXIES = [
 'http://124.89.2.250:63000',
 'http://106.75.71.122:80',
 'http://222.190.126.62:808',
 'http://106.8.17.14:60443',
 'http://183.167.217.152:63000',
 'http://118.190.95.35:9001',
 'http://39.106.191.64:1801',
 'http://125.118.75.168:6666',

]

HTTPPROXY_ENABLED = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 16

DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
#SPIDER_MIDDLEWARES = {
#    'Jamanetwork.middlewares.JamanetworkSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# DOWNLOADER_MIDDLEWARES = {
   # 'Jamanetwork.middlewares.JamanetworkDownloaderMiddleware': 543,
#    'Jamanetwork.middlewares.RandomProxyMiddleware': 749,
#
# }

# Enable or disable extensions
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
ITEM_PIPELINES = {
   'Jamanetwork.pipelines.JamanetworkPipeline': 300,
   'Jamanetwork.pipelines.MongoDBPipeline': 301,

}

# Enable and configure the AutoThrottle extension (disabled by default)
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

COMMANDS_MODULE = 'Jamanetwork.commands'

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "xuguoliang"
MONGODB_COLLECTION = "xuguoliang"