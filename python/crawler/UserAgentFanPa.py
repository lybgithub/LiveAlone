# -*- coding: utf-8 -*-
#!/usr/bin/python
import urllib2
import os
import time
import sys
import socket
import re
import cookielib
import codecs
from lxml import etree
import cookielib
import mechanize
import adsl1
import adsl

#today=time.strftime('%Y-%m-%d',time.localtime(time.time()))
cj = cookielib.LWPCookieJar()
# Browser
br = mechanize.Browser()
br.set_cookiejar(cj)
# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(False)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
# Want debugging messages?
#br.set_debug_http(True)
#br.set_debug_redirects(True)
#br.set_debug_responses(True)
# User-Agent (http header)
br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0')]
# HTTP access and get response pack

#不能说的秘密
#支持人数
##url='http://movie.douban.com/subject/2124724/'
##secret=urllib2.urlopen(url).read()
##doc=etree.HTML(secret.decode('utf8','ignore'))
##vote=doc.xpath('//p/a/span[@property="v:votes"]')
##vote=vote[0].text.strip()
##vote='支持的人数为：'+vote
#print vote
#短评
#获得jay拍过所有电影使用的程序
##jay='http://movie.douban.com/subject_search?start=15&search_text=%E5%91%A8%E6%9D%B0%E4%BC%A6&cat=1002'
##html=urllib2.urlopen(jay).read()
##cc=etree.HTML(html.decode('utf8','ignore'))
###movie=cc.xpath('//td[@valign="top"]/div/span/text()')#电影的名称
##path=cc.xpath('//td[@valign="top"]/div/a//@href')#电影的路径
###movie=movie[0].strip()
##for p in xrange(20):
##    pa=path[p].strip()
##    print pa


filename='douban.txt'
web=open('jay.txt','r').readlines()#打开储存周杰伦所有电影原地址的txt
try:
    for x in web:                      #对于每一个电影进行循环
        x=x.rstrip()
        #获得这个电影的名称
        murl=x
        m=urllib2.urlopen(murl).read()
        mdoc=etree.HTML(m.decode('utf8','ignore'))
        mname=mdoc.xpath('//head/title/text()')
        yt=mname[0].strip()  #每一个电影的名称
        
        #print yt
        #filename='douban.txt'
##        t=open(filename,'a')
##        t.write('')
##        t.close()
        #每一个电影的操作
        b=50000
        j=0
        while j<b:                    #循环评论页，start项每次增加20，直至获得所有评论页                 
            url=str(x)+'comments?start='+str(j)+'&limit=20&sort=new_score'#获得每一个电影短评部分的url
            secret=urllib2.urlopen(url).read()
            time.sleep(1)
            doc=etree.HTML(secret.decode('utf8','ignore'))
            people=doc.xpath('//div[@class="comment"]/h3/span[@class="comment-info"]/a/text()')#粉丝的名字
            comment=doc.xpath('//div[@class="comment"]/p/text()')#粉丝的评论
            fans=doc.xpath('//div[@class="comment"]/h3/span[@class="comment-info"]/a//@href')#粉丝的地址
            a=len(people)                   #获得列表的长度
            #txt='screts.txt'
            for i in xrange(a):             #在一页评论页上循环，获得这一页上所有粉丝的名字、评论、地址
                name=people[i].strip()
                tk=comment[i].strip()
                tk2=tk.replace('\n','')
                tk3=tk2.replace('\r','')
                url=fans[i].strip()
                end=name+'|'+tk3  #粉丝姓名+粉丝评论
                url2=url.encode('utf8')
                end2=end.encode('utf8')
                yt2=yt.encode('utf8')
##                print end
##                print url
                t=open(filename,'a')
                t.write(yt2+':'+end2+'|'+url2+'\n')
                t.close()
            j=j+20
            time.sleep(2)
except Exception,e:
    print 'error'
    adsl1.main()
    adsl1.main()
    
 







