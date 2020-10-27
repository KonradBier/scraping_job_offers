# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field
from itemloaders.processors import MapCompose

def convert_to_int(a):
    # change to integer
    a = int(a)
    return a

def remove_n(text):
    # strip the /n and split on category and city
    text = text.strip("\n").split(",", 1)
    return text

class PracujItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    kat_mias = Field(input_processor=MapCompose(remove_n))
    liczba = Field()

