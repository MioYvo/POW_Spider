# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
import creat_table
class DmozItem(Item):
    title = Field()
    link = Field()
    desc = Field()

class NuptPOWItem(Item):
    rep_num = Field()
    title = Field()
    title_url = Field()
    author = Field()
    #author_homepage = Field()  #url of author in baiduspace
    topic_desc = Field()
    topic_desc_img = Field()
    last_rep_time = Field()
    last_rep_aur = Field()
    last_rep_aur_home = Field()