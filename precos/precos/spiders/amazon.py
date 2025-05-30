import scrapy
import json
from precos.items import ProductItem

class AmazonSpider(scrapy.Spider):
    name = "amazon"
    allowed_domains = ["amazon.com.br"]

    def start_requests(self):
        with open('products.json', 'r', encoding='utf-8') as f:
            products = json.load(f)
        for prod in products:
            produto_id = prod['id']
            asin       = prod.get('asin')
            if not asin:
                continue
            url = f"https://www.amazon.com.br/dp/{asin}"
            yield scrapy.Request(
                url=url,
                callback=self.parse,
                meta={'produto_id': produto_id},
                dont_filter=True
            )

    def parse(self, response):
        produto_id = response.meta['produto_id']

        whole = response.css('.a-price-whole::text').get(default='').replace('.', '')
        frac  = response.css('.a-price-fraction::text').get(default='')
        try:
            preco = float(f"{whole}.{frac}") if whole and frac else None
        except ValueError:
            preco = None

        yield {
            'produto_id':   produto_id,
            'preco_amazon': preco,
            'url_amazon':   response.url
        }
