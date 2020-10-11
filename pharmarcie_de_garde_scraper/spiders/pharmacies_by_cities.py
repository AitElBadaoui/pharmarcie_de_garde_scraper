import scrapy
import logging
from scrapy.http.request import Request

class PharmaciesByCitiesSpider(scrapy.Spider):
    pharmacies = {'pharmacies': []}
    name = 'pharmacies_by_cities'
    allowed_domains = ['www.annuaire-gratuit.ma']
    start_urls = ['https://www.annuaire-gratuit.ma/pharmacie-garde-maroc.html']
    
    def parse(self, response):
        index = 0
        for city in response.css('article'):
            if city.css('h3 a::text').get():
                url = city.css('a::attr(href)').extract_first()
                pharmacie_url = 'https://www.annuaire-gratuit.ma'+ url
                request =  Request(pharmacie_url,  callback =self.parse_product)
                request.meta['city_fr']= city.css('h3 a::text').get().strip()
                request.meta['city_ar']= city.css('h3> a > span::text').get().strip()
                request.meta['count'] =  city.css('p::text').get().strip()
                yield request

    def parse_product(self, response):
        for pharmacie in response.css('article'):
            city = response.meta.get('city_fr')
            list_pharmacies_of_city = []
            if pharmacie.css('h3::text'):
                name = pharmacie.css('h3::text').extract_first() 
                address = pharmacie.css('p[itemprop="streetAddress"]::text').extract_first() 
                phone = pharmacie.css('span[itemprop="telephone"] a::text').extract_first() 
                district = pharmacie.css('span[itemprop="addressLocality"]::text').extract_first() 
                list_pharmacies_of_city.append({"name": name, "address": address, "phone": phone, "district": district})
        yield {
                'city_fr': response.meta.get('city_fr'),
                'city_ar': response.meta.get('city_ar'),
                'count': response.meta.get('count'),
                'pharmacies': list_pharmacies_of_city
            }
