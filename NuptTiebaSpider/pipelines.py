#-*- coding: utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#import pyodbc
import MySQLdb
import time
import re
import os



class NupttiebaspiderPipeline(object):
    def __init__(self):
    #connect MySQL
        self.conn = MySQLdb.connect(host="127.0.0.1",user="root",passwd="liurusi321",charset="utf8")
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        localtime = time.strftime('%Y_%m_%d', time.localtime())
        localtime2 = time.strftime('%Y%m%d', time.localtime())
        if not item['topic_desc']:
            item['topic_desc'].append('NULL')    

        if not item['topic_desc_img']:
            item['topic_desc_img'].append('NULL')  

        """
        if not item['rep_num']:
            item['rep_num'].append('NULL')

        if not item['title']:
            item['title'].append('NULL')

        if not item['title_url']:
            item['title_url'].append('NULL')

        if not item['author']:
            item['author'].append('NULL')


        if not item['last_rep_time']:
            item['last_rep_time'].append('NULL')

        if not item['last_rep_aur']:
            item['topic_desc_img'].append('NULL')

        if not item['last_rep_aur_home']:
            item['last_rep_aur_home'].append('NULL')
        """
        #for i in range(len(item['title'])):
        self.cursor.execute("USE POWDATA;")
        self.cursor.execute("insert into %s \
            (rep_num,title,title_url,author,topic_desc,topic_desc_img,last_rep_time,last_rep_aur,last_rep_aur_home,rep_day) \
            values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"\
            %(localtime, item['rep_num'][0], item['title'][0], item['title_url'][0], item['author'][0], item['topic_desc'][0], item['topic_desc_img'][0], item['last_rep_time'][0], item['last_rep_aur'][0], item['last_rep_aur_home'][0],localtime2))
        #self.cursor.execute("insert into %s (rep_num) values ('%s');"% (localtime,item['rep_num'][0]))
        #self.conn.commit()
        #print item
        #return item
        
        self.u = re.split(r'/',item['title_url'][0])
        #print item['rep_num'][0]
        self.i = int(item['rep_num'][0])
        tb_n1 = int(self.u[2])
        tb_n2 = localtime2
        tb_n = self.u[2]+'_'+tb_n2
        tb_n3 = '_'+self.u[2]
        print tb_n
        if self.i>100:
            self.cursor.execute("use POWANA")
            self.cursor.execute("create table if not exists %s (rep_num NVARCHAR(100), title NVARCHAR(1000), title_url NVARCHAR(1000), author NVARCHAR(100), topic_desc NVARCHAR(1000), topic_desc_img NVARCHAR(1000), last_rep_time NVARCHAR(100), last_rep_aur NVARCHAR(1000), last_rep_aur_home NVARCHAR(1000),rep_day NVARCHAR(100), trend NVARCHAR(100));"%tb_n3)
            self.cursor.execute("insert into %s (rep_num,title,title_url,author,topic_desc,topic_desc_img,last_rep_time,last_rep_aur,last_rep_aur_home,rep_day) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(tb_n3, item['rep_num'][0], item['title'][0], item['title_url'][0], item['author'][0], item['topic_desc'][0], item['topic_desc_img'][0], item['last_rep_time'][0], item['last_rep_aur'][0], item['last_rep_aur_home'][0],localtime2))
            #os.makedirs(r"/home/mio/Desktop/testANA/charts/%s/"%item['title'][0])
            print 'yes 100'
            print ' '
        else :
            print 'not 100'
            print ' '
        #self.cursor.close()
        #self.conn.close()
        self.conn.commit()
        return item
        
        #self.conn.close()
        #self.conn.close()
