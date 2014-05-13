# -*- coding: utf-8 -*-  

import MySQLdb
import time


localtime = time.strftime('%Y_%m_%d', time.localtime())
print localtime

conn = MySQLdb.connect(host="127.0.0.1",user="root",passwd="liurusi321",charset="utf8")
cur = conn.cursor()
cur.execute("use NuptPOW_DB1")
#cur.execute("create table 2014_02_09(name nvarchar(100),age nvarchar(100))")
cur.execute("show tables;")
row = cur.fetchall()

if_creat = 'yes'
for i in range(len(row)):
    for ii in row[i]:
        if localtime == ii:
            if_creat = 'no'
print if_creat

st2 = u'\u6211\u53eb\u4f60\u5927\u5927'
st3 = u'\u6211\u60f3\u79df\u623f'

if if_creat == 'no':
	cur.execute("USE NuptPOW_DB1")
	cur.execute("insert into 2014_02_10 (name, title) values ('%s','%s')"%(st2,st3))
	#cur.execute("insert into 2014_02_10 (name, title) values ("u'/p/2858331482'","u'/p/2858331482'")")
	#cur.execute("create table %s (name NVARCHAR(100), title NVARCHAR(1000), title_url NVARCHAR(1000), author NVARCHAR(100), topic_desc NVARCHAR(1000), topic_desc_img NVARCHAR(1000), last_rep_time NVARCHAR(100), last_rep_aur NVARCHAR(1000), last_rep_aur_home NVARCHAR(1000));"%localtime)
    #cur.execute("insert into %s (name, title) values ("abc",'ab')"%localtime)
conn.commit()
conn.close()

row1 = cur.fetchall()
print row1

st1=u'\u6211\u53eb\u4f60\u5927\u5927'
print st1