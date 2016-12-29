# -*- coding: utf8 -*-
import os
path = "F:\wiresharkPackage\mogujie"      #文件夹名称,只需要修改这一个地方
os.chdir(path)                       #切换当前目录
sumf = open(r'sumFile.txt','w')      ##生成的处理文件
files= os.listdir(path)              #得到文件夹下的所有文件名称   
for file in files:                   #遍历文件夹   
     f = open(path+"/"+file,'r');    #打开文件  
     for line in f:
         sumf.write(line)
sumf.close()

fileName = "sumFile.txt"                    ##处理的文件
f = open(fileName,'r+')
f1 = open(r'allHost.txt','w')
for line in f:
    try:
        newLine = line.split(' ')
        newLine = newLine[4]+newLine[5]
        ifHost = newLine[0]+newLine[1]+newLine[2]+newLine[3]
        if(ifHost=="Host"):
            newLine = newLine[5:-5]+'\n'
            f1.write(newLine)
    except:
        continue
f1.close()

##去重
outfilename = 'distinctHost.txt'  
infilename = 'allHost.txt'
lines_seen = set() 
outfile = open(outfilename, 'w')
infile = open(infilename,'r')

for line in infile:
    if line not in lines_seen:
        outfile.write(line)
        lines_seen.add(line)
infile.close()
outfile.close()



