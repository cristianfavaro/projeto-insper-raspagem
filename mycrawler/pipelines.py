# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from bs4 import BeautifulSoup as bs


def check_words(bsItem):
    ignore_words = ['Foto: ', 'Our Standards: ']

    for word in ignore_words:
        if word in bsItem:
            return False

    return True 


def fix_text(param):
    """Função para ajustar os parágrafos antes de adicionar ao sistema"""

    data = []
    for item in param:
        try:
            bsItem = bs(item, "lxml").get_text().strip()
            if bsItem:
                add = check_words(bsItem)
                if add:             
                    data.append(bsItem)
        
        except: 
            pass

    return '\n'.join(data)      

class MycrawlerPipeline(object):
    def process_item(self, item, spider):
        import pandas as pd
        # import ipdb; ipdb.set_trace()
        item = dict(item)
        item["fullText"] = fix_text(item["fullText"])

        try:
            df = pd.read_csv("base_noticias.csv", sep=";")
            
        except:
            df = pd.DataFrame(columns=["title","subTitle","author","fullText","img","headLine","newsPaper","section","link"])

        df = df.append(item, ignore_index=True)

        df.to_csv("base_noticias.csv", sep=";", index=False)

        return item
