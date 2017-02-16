# -*- coding: utf-8 -*-
#!/usr/bin/python

from lxml import etree

htmlFile = open(r"C:\Users\Administrator\Desktop\A1_R1_val_1_fastqc.html",'r')   ##r后面的是本地路径
content = htmlFile.read()
htmlContent = etree.HTML(content.decode('gb2312','ignore'))
BasicStatistics = htmlContent.xpath('//div[@class="module"]/table/tbody/tr/td/text()')
TotalSequences = BasicStatistics[7]
GC = BasicStatistics[13]
print "TotalSequences:"+TotalSequences+"\n"+"%GC:"+GC








