__author__ = 'mio'
#import pymssql
import MySQLdb
import time

class CreatTable(object):
    def __init__(self):
        #connect mysql
        self.conn = MySQLdb.connect(host="127.0.0.1",user="root",passwd="liurusi321",charset="utf8")
        self.conn.set_character_set('utf8')
        self.cursor = self.conn.cursor()

    def creat(self):
        localtime = time.strftime('%Y_%m_%d', time.localtime())
        self.cursor.execute("use POWDATA;")
        self.cursor.execute("show tables;")
        row = self.cursor.fetchall()
        if_creat = 'yes'
        for i in range(len(row)):
            for ii in row[i]:
                if localtime == ii:
                    if_creat = 'no'
        if if_creat == 'yes':
            self.cursor.execute("USE POWDATA")
            self.cursor.execute("create table %s (rep_num NVARCHAR(100), title NVARCHAR(1000), title_url NVARCHAR(1000), author NVARCHAR(100), topic_desc NVARCHAR(1000), topic_desc_img NVARCHAR(1000), last_rep_time NVARCHAR(100), last_rep_aur NVARCHAR(1000), last_rep_aur_home NVARCHAR(1000), rep_day NVARCHAR(100), trend NVARCHAR(100));"%localtime)
            self.conn.commit()
        self.conn.close()

