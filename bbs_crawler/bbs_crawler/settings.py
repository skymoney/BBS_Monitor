# Scrapy settings for bbs_crawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'bbs_crawler'

SPIDER_MODULES = ['bbs_crawler.spiders']
NEWSPIDER_MODULE = 'bbs_crawler.spiders'

DOWNLOAD_DELAY=5

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'bbs_crawler (+http://www.yourdomain.com)'
