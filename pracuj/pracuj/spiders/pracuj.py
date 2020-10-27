# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 11:31:56 2020

@author: biern
"""

import scrapy
import cfscrape


class PracujSpider(scrapy.Spider):
    name = "num_IT-adm_war"

    def start_requests(self):
        start_urls = [
            'https://www.pracuj.pl/praca/warszawa;wp/it%20-%20administracja;cc,5015?rd=30'
        ]
        for url in self.start_urls:
            token, agent = cfscrape.get_tokens(url, 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')
            yield scrapy.Request(url=url, cookies=token, headers={'User-Agent': agent})

    def parse(self, response):
        pass

