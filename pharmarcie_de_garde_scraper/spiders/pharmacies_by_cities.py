import scrapy


class PharmaciesByCitiesSpider(scrapy.Spider):
    name = 'pharmacies_by_cities'
    allowed_domains = ['https://www.annuaire-gratuit.ma/pharmacie-garde-maroc.html']
    start_urls = ['http://https://www.annuaire-gratuit.ma/pharmacie-garde-maroc.html/']

    def parse(self, response):
        pass
