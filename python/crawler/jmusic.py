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
j=0
filename='jielun.txt'
while j<255:
    #filename='jielun.txt'
    url='http://music.douban.com/subject_search?start='+str(j)+'&search_text=%E5%91%A8%E6%9D%B0%E4%BC%A6'
    html=urllib2.urlopen(url).read()
    doc=etree.HTML(html.decode('utf8','ignore'))
    #name=doc.xpath('//div[@class="pl2"]/a/text()')
    murl=doc.xpath('//div[@class="pl2"]/a//@href')
    l=len(murl)
    for i in xrange(l):
    #music=name[9].strip()
        dizhi=murl[i].strip()
        res=urllib2.urlopen(dizhi).read()
        doc2=etree.HTML(res.decode('utf8','ignore'))
        music=doc2.xpath('//title/text()')
        music2=music[0].strip()  #音乐的名字
        #print music2+dizhi
        u=1
        while u<353:
            comurl=dizhi+'comments/hot?p='+str(u)
            res2=urllib2.urlopen(comurl).read()
            doc3=etree.HTML(res2.decode('utf8','ignore'))
            #ty=doc3.xpath('//div[class="comments-wrapper"]/span[@id="total-comments"]/text()')
            #geshu=ty[0].strip()
            comment=doc3.xpath('//li[@class="comment-item"]/div/a//@title')
            comment2=doc3.xpath('//li[@class="comment-item"]/p[@class="comment-content"]/text()')
            n=len(comment)
            for y in xrange(n):
                content=comment2[y].strip()
                zuozhe=comment[y].strip()  #评论人
                commenter=zuozhe+'|'+content
                end=music2+'|'+dizhi
                end2=end+'|'+commenter+'\n'
                #print end2
                end3=end2.encode('utf8')
                s=open(filename,'a')
                s.write(end3)
                s.close()
            u=u+1
    j=j+15
    
    



      


