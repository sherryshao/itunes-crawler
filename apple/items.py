# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class AppItem(Item):
    # define the fields for your item here like:
    app_id = Field()
    app_name = Field()
    app_link = Field()
    category = Field()
    rating_count = Field()
    average_rating = Field()
