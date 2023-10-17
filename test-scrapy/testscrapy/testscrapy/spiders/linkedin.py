from scrapy import Request, Spider
from ..items import LinkedinItem
 
class SpiderLinkedin(Spider):
    # Nom du spider
    name = "linkedin"
    # URL de la page à scraper
    url = "https://www.linkedin.com/in/ludovic-moncla/"
 
    def start_requests(self):
        yield Request(url=self.url, callback=self.parse_profile)
 
    def parse_profile(self, response):
        item = LinkedinItem()
        item['title'] = response.css("h1.top-card-layout__title::text").extract_first()
        yield item