import scrapy
import json
from datetime import datetime

class MeliSpider(scrapy.Spider):
    name = "meli"
    allowed_domains = ["mercadolivre.com.br", "produto.mercadolivre.com.br"]

    def start_requests(self):
        # Carrega o JSON com seus produtos
        with open('products.json', 'r', encoding='utf-8') as f:
            products = json.load(f)

        for prod in products:
            produto_id = prod['id']
            ml_id = prod['ml_id']
            url = f"https://produto.mercadolivre.com.br/{ml_id}"
            yield scrapy.Request(
                url=url,
                callback=self.parse,
                meta={'produto_id': produto_id}
            )

    def parse(self, response):
        produto_id = response.meta['produto_id']
        # Extrai parte inteira e decimal do preço
        whole = response.css('.price-tag-fraction::text').get(default='').replace('.', '')
        cents = response.css('.price-tag-cents::text').get(default='')
        preco = float(f"{whole}.{cents}") if whole and cents else None

        yield {
            'produto_id': produto_id,
            'preco_mercadolivre': preco,
            'url_mercadolivre': response.url
        }
