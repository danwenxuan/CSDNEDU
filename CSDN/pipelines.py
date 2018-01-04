# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class CsdnPipeline(object):
    def  __init__(self):
        self.file=open("csdn.txt","w")
    def __del__(self):
        self.file.close()
    def process_item(self, item, spider):
        text=str(item)+"\r\n"
        self.file.write(text)
        self.file.flush()
        return item
