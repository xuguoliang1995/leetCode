
import scrapy
from scrapy import Field


class NatureItem(scrapy.Item):
    title = Field()
    link = Field()
    source = Field()
    pub_date = Field()
    abstract = Field()
    doi = Field()
    authors = Field()
    if_2017 = Field()
    type = Field()
    issn = Field()

