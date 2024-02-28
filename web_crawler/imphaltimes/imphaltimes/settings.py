BOT_NAME = "imphaltimes"

SPIDER_MODULES = ["imphaltimes.spiders"]
NEWSPIDER_MODULE = "imphaltimes.spiders"

ROBOTSTXT_OBEY = True

# REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
# TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
# FEED_EXPORT_ENCODING = "utf-8"

# PROXY_POOL_ENABLED = True
# DOWNLOADER_MIDDLEWARES = {
#     'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
#     'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
#     'scrapy_proxy_pool.middlewares.ProxyPoolMiddleware': 610,
#     'scrapy_proxy_pool.middlewares.BanDetectionMiddleware': 620,
# }

# PROXY_POOL_BAN_POLICY = 'imphaltimes.policy.MyPolicy'
