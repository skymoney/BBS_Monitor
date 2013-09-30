# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from bbs_crawler.items import Lily

import simplejson as json
import redis

class BbsCrawlerPipeline(object):
	def __init__(self):
		self.lily_file=open('lily.json','wb')

	def process_item(self, item, spider):
		if isinstance(item,Lily):
			self.lily_file.write(json.dumps(dict(item))+'\n')
		return item
