#-*- coding:utf-8 -*-

from scrapy.spider import BaseSpider
from scrapy.http import Request

from bs4 import BeautifulSoup
import re

from bbs_crawler.items import Lily

class Lilybbs(BaseSpider):
	name='lily'

	start_urls=['http://bbs.nju.edu.cn/bbstop10']

	allowed_domains=['bbs.nju.edu.cn']

	def parse(self,response):
		import sys
		reload(sys)
		sys.setdefaultencoding('utf-8')

		dom=BeautifulSoup(response.body)

		bbs_set=dom.find('table').find_all('tr')[1:]

		for bbs in bbs_set:
			item=Lily()
			item['rank']=bbs.find('td').string
			item['board']=bbs.find('td').find_next('td').find('a').string
			item['author']=bbs.find_all('td')[3].find('a').string
			item['authorlink']=''.join(['http://bbs.nju.edu.cn/',
				bbs.find_all('td')[3].find('a').get('href')])
			item['title']=bbs.find_all('td')[2].find('a').string
			item['link']=''.join(['http://bbs.nju.edu.cn/',
				bbs.find_all('td')[2].find('a').get('href'),'&start=-1'])
			yield Request(item['link'],meta={'item':item},callback=self.parse_single_bbs)


	def parse_single_bbs(self,response):
		#process single bbs
		dom=BeautifulSoup(response.body)
		item=response.meta['item']
		item['content']=dom.find('table').find('pre')
		comments=dom.find_all('table')[1:]
		print len(comments)
		item['comment']=[]
		for comment in comments:
			item['comment'].append({
				'author':comment.find('td').find_all('a')[2].string,
				'comment':comment.find_all('tr')[1].find('pre')
				})
		return item

