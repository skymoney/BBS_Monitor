# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class BbsCrawlerItem(Item):
    # define the fields for your item here like:
    # name = Field()
    pass

class Lily(Item):
	rank=Field()
	board=Field()
	title=Field()
	author=Field()
	authorlink=Field()
	link=Field()
	content=Field()
	comment=Field()