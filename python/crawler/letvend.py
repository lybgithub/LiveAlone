#coding:utf8
#url，评分，观看人数，直接在主页面上爬
import urllib2,urllib
import os
import time
import sys
import socket
import re
import cookielib
import requests
from lxml import etree

#url
a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39]
for line0 in a:
    urla='http://list.letv.com/listn/c2_t-1_a-1_y-1_s1_md_o20_d1_p'+str(line0)+'.html'
    html=urllib2.urlopen(urla)
    txt=html.readlines()
    for marks in txt:
        try:
            pattern1=re.compile(r'.*?<p class="p_t"><a href=".*?"')
            match1=pattern1.match(marks.strip())
            if match1:
                data1=match1.group()   #初步获得电视剧的url：<p class="p_t"><a href="http://www.letv.com/tv/22829.html"
                #print data1
                data2=data1.split('href="')
                data3=data2[1]
                data4=data3[0:-1]
                #print data4
                #电视剧url：
##                data4=data4.rstrip()
                
                
                res=urllib2.urlopen(data4).readlines()

                for line2 in res:
            #电视剧名称
                    pattern6=re.compile(r'.*?<title>.*?_')
                    match8=pattern6.match(line2.strip())
                    if match8:
                        neirong=match8.group()
                        data5=neirong.split('>')
                        data6=data5[1]
                        data7=data6.split('_')
                        mingzi=data7[0]
                        #print mingzi
                    #集数、地区、类型
                    #a=open('e11'+str(line0)+str(line)+'.txt','r+').read()
                a=urllib2.urlopen(data4).read()
                doc = etree.HTML(a.decode('utf8', 'ignore'))
                try:
                    tags00= doc.xpath('//span[@class="s-t"]')#集数
                    c=doc.xpath('//p[@class="p3"]/a[@target="_blank"]')#国家地区
                    d=doc.xpath('//p[@class="p5"]/a[@target="_blank"]')#类型
                    e=doc.xpath('//dl[@class="textInfo"]/dd/p[@class="p2"]/a/text()')#演员
                    f=doc.xpath('//p[@class="p1"]/a[@target="_blank"]')#导演
                    #h=doc.xpath('//p[@class="p"]/a[@target="_blank"]')#电视剧名称
                    g=doc.xpath('//p[@class="p4"]/a[@target="_blank"]')#上映日期
                    ##print tags00[0].text.strip()
                    length=tags00[0].text.strip()
                    area=c[0].text.strip()
                    star0=','.join(e)
                    #仍然存在的问题：类型里面没有东西怎么办，某个项里面的东西比较少怎么办
                    ##star1=e[1].text.strip()
                    ##star2=e[2].text.strip()
                    ##star3=e[3].text.strip()
                    ##star4=e[4].text.strip()
                    tutor=f[0].text.strip()
                    date=g[0].text.strip()
                    if d==[]:
                        final=date+'|'+tutor+'|'+length+'|'+star0+'|'+area
                    else:
                        types0=d[0].text.strip()
                        #types1=d[1].text.strip()
                        #types2=d[2].text.strip()
                        final=date+'|'+tutor+'|'+length+'|'+star0+'|'+area+'|'+types0
                    #print final #2002黎文彦共40集吴奇隆朱茵于波马雅舒万弘杰中国大陆古装武侠经典
                    #end=mingzi+area
                    final=final.encode('utf8')#可以使用type（final查看final的编码规则）
                    end=mingzi+'|'+final
                    
                    #print line
                    #print end
                except Exception,e:
                    print '陈云在一九四九 1998 詹相持 共8集 古月 中国大陆 战争'
##                filename='end.txt'
##                y=open(filename,'a')
##                y.write(line+'\n'+end+'\n'+'\n')
##                y.close()
        
            pattern2=re.compile(r'.*?class="blu">.*?</em><span.*?</span><span')
            match2=pattern2.match(marks.strip())
            if match2:
                mark=match2.group()
                mark=mark.split('">')
                mark=mark[2]
                mark=mark.split('<')
                mark=mark[0]+'分'
                #print mark
            pattern3=re.compile(r'.*?class="ico_play_num">.*?</span></p>')
            match3=pattern3.match(marks)
            if match3:
                num=match3.group().strip()
                num=num.split('">')
                num=num[1]
                num=num.split('</')
                num=num[0]
                num=num+'人'
                #print num
                df=data4+'|'+mark+'|'+num
                end1=end+df+'\n'
                #print end1
                #把上面的内容写入文档
                #end1=data4+' '+mark+'  '+num
                same='letv.txt'
                n=open(same,'a')#设置成为追加模式，也就是不清空之前的内容
                n.write(end1)
                n.close()
                
        except Exception,e:
            print 'error'
        
    
       
        
                #print num
    ##txt2=html.read()
    ##doc=etree.HTML(txt2.decode('utf8','ignore'))
    ##name=doc.xpath('//dd[@class="dd_cnt"]/p[@class="p_t"]/a[@target="_blank"]')
    ##leixing=doc.xpath('//p/span[@class="mr0"]')
    ##leixing1=leixing[0].text.strip()
    ##name1=name[1].text.strip()
    ##print leixing1
    ##print name1




       
            

         
    
            
            
    
    
         
            
