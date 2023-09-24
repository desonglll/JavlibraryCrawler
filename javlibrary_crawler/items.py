# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WorkSpider(scrapy.Item):
    preview = scrapy.Field()
    title = scrapy.Field()
    actor_id = scrapy.Field()
    release_date = scrapy.Field()
    serial_number = scrapy.Field()
    comments = scrapy.Field()
    reviews = scrapy.Field()
    link = scrapy.Field()
    maker = scrapy.Field()
    id = scrapy.Field()
    length = scrapy.Field()
    director = scrapy.Field()
    label = scrapy.Field()
    user_rating = scrapy.Field()
    genres = scrapy.Field()
    cast = scrapy.Field()


class ActorItem(scrapy.Item):
    actor_name = scrapy.Field()
    actor_id = scrapy.Field()