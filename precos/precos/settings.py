# settings.py do seu projeto Scrapy

BOT_NAME = 'precos'

SPIDER_MODULES = ['precos.spiders']
NEWSPIDER_MODULE = 'precos.spiders'

# Respeitar robots.txt
ROBOTSTXT_OBEY = True

# Exportar feeds (JSON/CSV) em UTF-8
FEED_EXPORT_ENCODING = 'utf-8'

# ativa nosso pipeline de ordenação
ITEM_PIPELINES = {
    'precos.pipelines.ExcelPipeline': 300,
}


# garante UTF-8 na exportação
FEED_EXPORT_ENCODING = 'utf-8'

# (Opcional para evitar bans)
# DOWNLOAD_DELAY = 1
# CONCURRENT_REQUESTS = 8
# USER_AGENT = 'Mozilla/5.0 (compatible; PreçosBot/1.0; +http://seusite.com)'
