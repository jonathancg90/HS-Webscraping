# Scrapy settings for hsscraping project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'hsscraping'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['hsscraping.spiders']
NEWSPIDER_MODULE = 'hsscraping.spiders'
DEFAULT_ITEM_CLASS = 'hsscraping.items.HsscrapingItem'
#USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.95 Safari/537.11'
#DOWNLOAD_DELAY = 2
#CONCURRENT_REQUESTS = 1