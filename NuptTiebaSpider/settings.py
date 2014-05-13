# Scrapy settings for NuptTiebaSpider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'NuptTiebaSpider'

SPIDER_MODULES = ['NuptTiebaSpider.spiders']
NEWSPIDER_MODULE = 'NuptTiebaSpider.spiders'

ITEM_PIPELINES = ['NuptTiebaSpider.pipelines.NupttiebaspiderPipeline']

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'NuptTiebaSpider (+http://www.yourdomain.com)'
