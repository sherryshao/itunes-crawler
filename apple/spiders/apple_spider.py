from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

from apple.items import AppItem

class AppleSpider(BaseSpider):
    name = "apple"
    allowed_domains = ["apple.com"]
    start_urls = ["http://www.apple.com/itunes/charts/free-apps/"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        apps = hxs.select('//*[@id="main"]/section/ul/li')
        count = 0
        items = []
        for app in apps:
            item = AppItem()
            item['app_name'] = app.select('//h3/a/text()')[count].extract()
            item['app_link'] = app.select('//h3/a/@href')[count].extract()
            item['category'] = app.select('//h4/a/text()')[count].extract()

            app_link = str(item['app_link'])
            item['app_id'] = app_link.split("id")[1].split("?")[0]
            
            item = Request(app_link,
        		callback=self.parse_link,
        		errback=lambda _: item,
                meta=dict(item=item),
                )

            items.append(item)
            count += 1
        return items

    def parse_link(self, response):
    	app_hxs = HtmlXPathSelector(response)
    	item = response.meta.get('item')
    	item['rating_count'] = app_hxs.select('//*[@class="rating-count"]/text()').extract()
    	# item['average_rating'] = app_hxs.select('//*[@class="rating-count"]/text()').extract()
    	return item