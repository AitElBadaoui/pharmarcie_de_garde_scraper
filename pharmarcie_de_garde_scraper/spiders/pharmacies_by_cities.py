import scrapy


class PharmaciesByCitiesSpider(scrapy.Spider):
    name = 'pharmacies_by_cities'
    allowed_domains = ['https://www.annuaire-gratuit.ma/pharmacie-garde-maroc.html']
    start_urls = ['https://www.annuaire-gratuit.ma/pharmacie-garde-maroc.html']
    def parse(self, response):
        index = 0
        for city in response.css('article'):
            index +=1
            if city.css('h3 a::text').get():
                yield {
                    'id':index, 'city_fr': city.css('h3 a::text').get().strip() , 'city_ar': city.css('h3> a > span::text').get().strip(), 'number': city.css('p::text').get().strip()
                    }
        
