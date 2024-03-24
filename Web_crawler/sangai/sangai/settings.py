BOT_NAME = "sangai"

SPIDER_MODULES = ["sangai.spiders"]
NEWSPIDER_MODULE = "sangai.spiders"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline': 1}
IMAGES_STORE = 'dowloaded_images'

# PROXY_POOL_ENABLED = True
# DOWNLOADER_MIDDLEWARES = {
#     'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
#     'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
#     'scrapy_proxy_pool.middlewares.ProxyPoolMiddleware': 610,
#     'scrapy_proxy_pool.middlewares.BanDetectionMiddleware': 620,
# }

# PROXY_POOL_BAN_POLICY = 'sangai.policy.MyPolicy'
# PROXY = ""
# CHROME_DRIVER_PATH ='/snap/bin/chromium.chromedriver'
# PDF_SAVE_PATH = "./downloaded_pdfs"
# PDF_SAVE_AS_PDF = False
# PDF_DOWNLOAD_TIMEOUT = 60
# PDF_PRINT_OPTIONS = {
#     'landscape': False,
#     'displayHeaderFooter': False,
#     'printBackground': True,
#     'preferCSSPageSize': True,
# }
# WEBDRIVER_HUB_URL = 'http://127.0.0.1:4444/wd/hub'


REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
