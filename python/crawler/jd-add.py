# -*- coding: utf-8 -*-
#!/usr/bin/python
import urllib2
import os
import time
import sys
import socket
import re
import cookielib

today=time.strftime('%Y-%m-%d',time.localtime(time.time()))
b=open('jdid.txt','r').readlines()  #打开需要爬取id的文件
for line in b:
    line=line.rstrip() #去掉每个id后面的'\n'
    try:
        itemurl='http://item.jd.com/'+str(line)+'.html'#拼出url
        response= urllib2.urlopen(itemurl)
        html=response.readlines()
        
        for  x in html:
            x=x.strip()
            pattern1=re.compile(r'<title>.*?</title>')#找出名字
            match1=pattern1.match(x)
            if match1:
                data1=match1.group()
                name1=data1.split('e>')
                name2=name1[1]
                name=name2[0:-34]
                
                
            pattern2=re.compile(r'<strong><a href=.*? clstag=".*?">.*?</a></strong><span>&nbsp;&gt;&nbsp;<a href=.*? clstag=".*?">.*?</a>&nbsp;&gt;&nbsp;<a href=.*? clstag=".*?">.*?</a>&nbsp;&gt;&nbsp;</span>')#标签
            match2=pattern2.match(x)
            if match2:
                data2=match2.group()
                labels=data2.split('</a>')
                label1_1=labels[0].split('">')
                label1=label1_1[1]
                label2_1=labels[1].split('">')
                label2=label2_1[1]
                label3_1=labels[2].split('">')
                label3=label3_1[1]
                print line +' is ok'
    except Exception,e:
           print 'error'
           filename0=str(day)+'error.txt'
           
           file_obj=open(filename0,'a')
           file_obj.write(line+'\n')#写入文档      
           file_obj.close()
           continue
    try: #找价格
         priceurl = 'http://accy.jd.com/accessories/thirdTypeMatchScheme/6864/'+str(line)+'.jsonp'
         pricetext = urllib2.urlopen(priceurl)
         pricesome = pricetext.readlines()
         caoyu = ''.join(pricesome)#list改为str
         price1=caoyu.split('],')
         price2=price1[-1].split('"wMaprice":')
         price3=price2[1].split(',"wMeprice"')
         price=price3[0]                
            
    except Exception,e: #异常处理，保证继续运行
            print 'no price'
            continue
    final= itemurl+','+name+','+line+','+label1+','+label2+','+label3+','+str(price)       
    final=final.decode('GB2312').encode('utf-8')
    filename=str(today)+'.txt'
    file_obj=open(filename,'a')
    file_obj.write(final+'\n')
    file_obj.close() 
print 'end'
            
                
  
  
        
    
    
   



   
