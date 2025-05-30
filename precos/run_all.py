from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from precos.spiders.amazon import AmazonSpider
from precos.spiders.meli   import MeliSpider

if __name__ == "__main__":
    process = CrawlerProcess(get_project_settings())
    # Agende as duas spiders antes de iniciar:
    process.crawl(AmazonSpider)
    process.crawl(MeliSpider)
    process.start()  # executa ambas e só aí dispara o pipeline
