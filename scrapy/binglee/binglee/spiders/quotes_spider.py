import scrapy
import os
from htmlanalyser import HtmlAnalyser

htmlanalyser = HtmlAnalyser()


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = htmlanalyser.scrape_product_pages_url('LED TVs - UHD (4K), FHD, Smart & 3D Televisions - Buy Online with Bing Lee.html')
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-1]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
