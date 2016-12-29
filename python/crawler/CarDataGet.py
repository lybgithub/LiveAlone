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

smallCarUrl = 'http://k.autohome.com.cn/a01/#pvareaid=102517'
midCarUrl = 'http://k.autohome.com.cn/b1/#pvareaid=102517'
bigCarUrl1 = 'http://k.autohome.com.cn/d1/#pvareaid=102517'
bigCarUrl2 = 'http://k.autohome.com.cn/c1/#pvareaid=102517'
bigCarUrl3 = 'http://k.autohome.com.cn/s1/#pvareaid=102517'

#小型车数据爬取
def carData(txt,carUrl,carClass):
    #smallTxt = 'small.txt'
    readSmallContent = urllib2.urlopen(carUrl).read()
    getSmallContent = etree.HTML(readSmallContent.decode('gb2312','ignore'))
    getSmallCarId = getSmallContent.xpath('//div[@class="cont-pic"]/a//@href')
    num = len(getSmallCarId)
    for i in xrange(num):
        eachSmallCarUrl = 'http://k.autohome.com.cn/' + str(getSmallCarId[i])  #每一个小型车的url
        eachSmallCarContent = urllib2.urlopen(eachSmallCarUrl).read()
        eachSmallContent = etree.HTML(eachSmallCarContent.decode('gb2312','ignore'))
        carScore = eachSmallContent.xpath('//span[@class="font-arial number-fen"]/text()')
        carScore = carScore[0].strip()                                         #每一个小型车的评分
        try:
            carOil = eachSmallContent.xpath('//em[@class="font-arial font-number"]/text()')  #每一个小型车耗油量
            carOil = carOil[0].strip()
        except Exception,e:
            carOil = 6.5
        carPrice = eachSmallContent.xpath('//li[@class="price"]/span/a/text()')   #小型车的价格范围
        carPrice = carPrice[0].strip()
        carPrice = carPrice.split('-')
        minCarPrice = carPrice[0]
        #openSmallFile = open(smallTxt,'a+')
        openSmallFile = open(txt,'a+')
        openSmallFile.write(carClass+'/'+str(carOil)+'/'+str(carScore)+'/'+str(minCarPrice)+'\n')
        openSmallFile.close()
        #print '小型车'+'|'+str(carOil)+'|'+str(carScore)+'|'+str(minCarPrice)        #耗油量+评分+车最低价格

carData('small.txt',smallCarUrl,'小型车')
carData('mid.txt',midCarUrl,'中型车')
carData('big.txt',bigCarUrl1,'大型车')
carData('big.txt',bigCarUrl2,'大型车')
carData('big.txt',bigCarUrl3,'大型车')

    

    
    

    





