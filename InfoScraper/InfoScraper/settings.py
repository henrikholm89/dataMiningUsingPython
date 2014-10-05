# -*- coding: utf-8 -*-

# Scrapy settings for InfoScraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'InfoScraper'

SPIDER_MODULES = ['InfoScraper.spiders']
NEWSPIDER_MODULE = 'InfoScraper.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'InfoScraperBot/0.1'

DOWNLOAD_DELAY = 60.0
