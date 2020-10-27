# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 11:31:56 2020

@author: jmmpad
"""

import scrapy
from pracuj.items import PracujItem
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst


class PracujSpider(scrapy.Spider):
    name = "num_pos"
    download_delay = 5
    start_urls = [
        'https://www.pracuj.pl/praca/warszawa;wp/it%20-%20administracja;cc,5015?rd=30',  # IT - Administracja, Warszawa
        'https://www.pracuj.pl/praca/warszawa;wp/it%20-%20rozw%c3%b3j%20oprogramowania;cc,5016?rd=30',# IT - Rozwój oprogramowania, Warszawa
        #'https://www.pracuj.pl/praca/warszawa;wp/administracja%20biurowa;cc,5001?rd=30', # Administracja biurowa, Warszawa
        #'https://www.pracuj.pl/praca/warszawa;wp/badania%20i%20rozw%c3%b3j;cc,5002?rd=30', # Badania i rozwój, Warszawa
        #'https://www.pracuj.pl/praca/warszawa;wp/bankowo%c5%9b%c4%87;cc,5003?rd=30', # Bankowość, Warszawa
        #'https://www.pracuj.pl/praca/warszawa;wp/bhp%20ochrona%20%c5%9brodowiska;cc,5004?rd=30', # BHP / Ochrona środowiska, Warszawa
        #'https://www.pracuj.pl/praca/warszawa;wp/budownictwo;cc,5005?rd=30', # Budownictwo, Warszawa
        #'https://www.pracuj.pl/praca/warszawa;wp/call%20center;cc,5006?rd=30', # Call Center, Warszawa
        #'https://www.pracuj.pl/praca/warszawa;wp/doradztwo%20konsulting;cc,5037?rd=30', # Doradztwo / Konsulting, Warszawa
        #'https://www.pracuj.pl/praca/warszawa;wp/energetyka;cc,5036?rd=30', # Energetyka, Warszawa
        #'https://www.pracuj.pl/praca/warszawa;wp/edukacja%20szkolenia;cc,5007?rd=30', # Edukacja / Szkolenia, Warszawa
        #'https://www.pracuj.pl/praca/warszawa;wp/finanse%20ekonomia;cc,5008?rd=30', # Finanse / Ekonomia, Warszawa
        #'https://www.pracuj.pl/praca/warszawa;wp/franczyza%20w%c5%82asny%20biznes;cc,5009?rd=30', # Franczyza / Własny biznes, Warszawa
        #'https://www.pracuj.pl/praca/warszawa;wp/hotelarstwo%20gastronomia%20turystyka;cc,5010?rd=30', # Hotelarstwo / Gastronomia / Turystyka, Warszawa
        #'https://www.pracuj.pl/praca/warszawa;wp/human%20resources%20zasoby%20ludzkie;cc,5011?rd=30', # Human Resources / Zasoby ludzkie, Warszawa
        #'https://www.pracuj.pl/praca/warszawa;wp/internet%20e-commerce%20nowe%20media;cc,5013?rd=30', # Internet / e-Commerce / Nowe media, Warszawa
        #'https://www.pracuj.pl/praca/warszawa;wp/in%c5%bcynieria;cc,5014?rd=30', # Inżynieria, Warszawa
        #'https://www.pracuj.pl/praca/warszawa;wp/kontrola%20jako%c5%9bci;cc,5034?rd=30', # Kontrola jakości, Warszawa
        #'https://www.pracuj.pl/praca/warszawa;wp/%c5%82a%c5%84cuch%20dostaw;cc,5017?rd=30', # Łańcuch dostaw, Warszawa
        #'https://www.pracuj.pl/praca/warszawa;wp/marketing;cc,5018?rd=30', # Marketing, Warszawa
        #'https://www.pracuj.pl/praca/warszawa;wp/media%20sztuka%20rozrywka;cc,5019?rd=30', # Media / Sztuka / Rozrywka, Warszawa
        #'https://www.pracuj.pl/praca/warszawa;wp/nieruchomo%c5%9bci;cc,5020?rd=30', # Nieruchomości, Warszawa
        #'https://www.pracuj.pl/praca/warszawa;wp/obs%c5%82uga%20klienta;cc,5021?rd=30', # Obsługa klienta, Warszawa
        #'https://www.pracuj.pl/praca/warszawa;wp/praca%20fizyczna;cc,5022?rd=30', # Praca fizyczna Warszawa
        #'https://www.pracuj.pl/praca/warszawa;wp/prawo;cc,5023?rd=30', # Prawo, Warszawa
        #'https://www.pracuj.pl/praca/warszawa;wp/produkcja;cc,5024?rd=30', # Produkcja, Warszawa
        #'https://www.pracuj.pl/praca/warszawa;wp/public%20relations;cc,5025?rd=30', # Public Relations, Warszawa
        #'https://www.pracuj.pl/praca/warszawa;wp/reklama%20grafika%20kreacja%20fotografia;cc,5026?rd=30', # Reklama / Grafika / Kreacja / Fotografia, Warszawa
        #'https://www.pracuj.pl/praca/warszawa;wp/sektor%20publiczny;cc,5027?rd=30', # Sektor publiczny, Warszawa
        #'https://www.pracuj.pl/praca/warszawa;wp/sprzeda%c5%bc;cc,5028?rd=30', # Sprzedaż, Warszawa
        #'https://www.pracuj.pl/praca/warszawa;wp/transport%20spedycja;cc,5031?rd=30', # Transport / Spedycja / Logistyka, Warszawa
        #'https://www.pracuj.pl/praca/warszawa;wp/ubezpieczenia;cc,5032?rd=30', # Ubezpieczenia, Warszawa
        #'https://www.pracuj.pl/praca/warszawa;wp/zakupy;cc,5033?rd=30', # Zakupy, Warszawa
        #'https://www.pracuj.pl/praca/warszawa;wp/zdrowie%20uroda%20rekreacja;cc,5035?rd=30', # Zdrowie / Uroda / Rekreacja, Warszawa
        #'https://www.pracuj.pl/praca/warszawa;wp/inne;cc,5012?rd=30' # Inne, Warszawa
    ]

    def parse(self, response):

        loader = ItemLoader(item=PracujItem(), response=response)
        loader.add_xpath('kat_mias', '//*[contains(concat( " ", @class, " " ), concat( " ", "results-header__keyword", " " ))]/text()')
        loader.add_xpath('liczba', '//*[contains(concat( " ", @class, " " ), concat( " ", "results-header__offer-count-text-number", " " ))]/text()', TakeFirst())
        data_item = loader.load_item()
        return data_item
