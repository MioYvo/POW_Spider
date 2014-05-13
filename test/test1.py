__author__ = 'mio'
# -*- coding: cp1252 -*-
import time
import pyodbc
import sys


localtime = time.strftime('%Y-%m-%d', time.localtime()).decode()
conn = pyodbc.connect(
    'DRIVER={SQL Server};SERVER=MIO\NUPTTIEBAPOW;DATABASE=NuptPOW_DB1;UID=Yvo;PWD=Liu159762480')
cursor = conn.cursor()
cursor.execute("""USE [NuptPOW_DB1]""")
cursor.execute("""select [name] from sys.tables""")
row = cursor.fetchall()
print row

item = {
    'rep_num': [u'4'],
    'title': [u'\u4eca\u5929\u53bb\u6816\u971e\u5c71\u6709\u4e2a178\u7684\u59b9\u5b50'],
    'title_url': [u'/p/2734832086'],
    'author': [u'\u5929\u6674\u53d4'],
    'topic_desc': [
        u'\u5feb\u9012\u4ece\u4ed9\u6797\u5bc4\u5230\u672c\u90e8\uff0c10\u6765\u65a4\u7684\u4e1c\u897f\u8981\u591a\u5c11\u94b1\u554a\uff1f'],
    'topic_desc_img': [u'http://static.tieba.baidu.com/tb/static-frs/img/blankwhite_120.gif?v=1'],
    'last_rep_time': [u'21:23'],
    'last_rep_aur': [u'\u9f0e\u5c71\u72d0\u4ed9'],
    'last_rep_aur_home': [u'/home/main/?un=%B6%A6%C9%BD%BA%FC%CF%C9&fr=frs']
}
cursor.execute("USE [NuptPOW_DB1]")
#cursor.execute("create table [dbo].[%s]([rep_num] [nvarchar](max) NULL,[title] [nvarchar](max) NULL,[title_url] [nvarchar](max) NULL,[author] [nvarchar](max) NULL,[topic_desc] [nvarchar](max) NULL,[topic_desc_img] [nvarchar](max) NULL,[last_rep_time] [nvarchar](max) NULL,[last_rep_aur] [nvarchar](max) NULL,[last_rep_aur_home] [nvarchar](max) NULL) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]"%localtime)
#cursor.commit()
#for i in range(len(item['title'])):
#print item['rep_num'][0]
#print item['title_url'][0]
#print item['title'][0]
#print item['last_rep_time'][0]
#cursor.execute("INSERT INTO test1(rep_num,title_url) VALUES (?,?)",item['rep_num'][0], item['title_url'][0])
#cursor.execute("INSERT INTO test1(rep_num) values  (%s)" % (item['rep_num'][0]))
'''
for i in range(len(item['title'])):
    conn.execute("insert into test1 values(%s,'%s','%s')"%(item['rep_num'][i],item['title'][i],item['title_url'][i]))
    print "insert into test1 values(%s,'%s','%s')"%(item['rep_num'][i],item['title'][i],item['title_url'][i])
    conn.commit()
    #succesful !


conn.execute("insert into test1 values(%s,'%s','%s')"%(item['rep_num'][0],item['title'][0],item['title_url'][0]))
print "insert into test1 values(%s,'%s','%s')"%(item['rep_num'][0],item['title'][0],item['title_url'][0])
conn.commit()
 #successful !
conn.execute("insert into [%s](rep_num,title,title_url,author,topic_desc,topic_desc_img,last_rep_time,last_rep_aur,last_rep_aur_home) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(localtime, item['rep_num'][0], item['title'][0], item['title_url'][0], item['author'][0], item['topic_desc'][0], item['topic_desc_img'][0], item['last_rep_time'][0], item['last_rep_aur'][0], item['last_rep_aur_home'][0]))
print "insert into [%s](rep_num,title,title_url,author,topic_desc,topic_desc_img,last_rep_time,last_rep_aur,last_rep_aur_home) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(localtime, item['rep_num'][0], item['title'][0], item['title_url'][0], item['author'][0], item['topic_desc'][0], item['topic_desc_img'][0], item['last_rep_time'][0], item['last_rep_aur'][0], item['last_rep_aur_home'][0])
conn.commit()
'''#successful !
    #print "INSERT INTO test1 (title) values ('%s')"%(item['title'][i])
    #conn.commit()
    #print item['title'][i]
    #cursor.execute("INSERT INTO test1(rep_num,title) VALUES (%s,%s)" % (item['rep_num'][i] , item['title'][i]))
    #conn.commit()

    #cursor.execute(
    #    "insert into test1(rep_num ,title)) values ({0},{1})".format(item['rep_num'][i].encode('utf-8'), item['title'][i].encode('utf-8')))
    #conn.commit()

#print item['last_rep_aur'][0].encode('utf-8')




'''
IfCreat = 'yes'
for i in range(len(row)):
    print row[i]
    for ii in row[i]:
        print ii
        if 'test1' == ii:
            IfCreat = 'no'
            print IfCreat
print IfCreat

if IfCreat is 'yes':
    print 'creat new table and insert data'
else:
    print 'insert data to exit table'
#else:
#    print 'insert'
'''

'''
if localtime in a:
    print 'yes'
else:
    print 'no'

if u'2013-12-14'is localtime:
    print 'yes'
else:
    print 'no'
'''

'''
a='a'
b='b'
c='c'
i = ('test format string :%s,%s+%s'%(a,b,c))
print i
'''

cursor.execute("USE [NuptPOW_DB1]")
cursor.execute("create table [dbo].[%s]([rep_num] [nvarchar](max) NULL,[title] [nvarchar](max) NULL,[title_url] [nvarchar](max) NULL,[author] [nvarchar](max) NULL,[topic_desc] [nvarchar](max) NULL,[topic_desc_img] [nvarchar](max) NULL,[last_rep_time] [nvarchar](max) NULL,[last_rep_aur] [nvarchar](max) NULL,[last_rep_aur_home] [nvarchar](max) NULL) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]"%localtime)
conn.commit()
