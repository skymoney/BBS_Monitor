#-*- coding:utf-8 -*-

from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy.settings import Settings
from scrapy import log
from spiders import Lily_bbs

def spider_setup():
	spider=Lily_bbs()
	crawler=Crawler(Settings())
	crawler.configure()
	crawler.crawl(spider)
	crawler.start()
	log.start()
	reactor.run()

if __name__=='__main__':
	spider_setup()