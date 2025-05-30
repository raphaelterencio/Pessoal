import scrapy
import json
from precos.items import ProductItem
from datetime import datetime

class AmazonSpider(scrapy.Spider):
    name = "amazon"
    allowed_domains = ["amazon.com.br"]

    def start_requests(self):
        # Carrega o JSON com seus produtos
        with open('products.json', 'r', encoding='utf-8') as f:
            products = json.load(f)

        for prod in products:
            produto_id = prod['id']
            asin       = prod['asin']
            url        = f"https://www.amazon.com.br/dp/{asin}"
            yield scrapy.Request(
                url=url,
                callback=self.parse,
                meta={'produto_id': produto_id}
            )

    def parse(self, response):
        item = ProductItem()
        item['produto_id']   = response.meta['produto_id']
        item['nome']         = response.css('#productTitle::text').get(default='').strip()

        # Extrai preço
        whole = response.css('.a-price-whole::text').get(default='').replace('.', '')
        frac  = response.css('.a-price-fraction::text').get(default='')
        preco = float(f"{whole}.{frac}") if whole and frac else None

        item['preco_amazon'] = preco
        item['url_amazon']   = response.url

        yield item
