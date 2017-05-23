## the most effective method to handle chinese:add coding:utf8,and make the txt's encoding style be utf8
import re

def reg(line):
    pattern = r'[0-9]+\.[0-9]+'
    test = re.search(pattern,line)
    return test

# when the context of the txt have chinese,and it can't be read,you should convert the txt's encoding to utf8.or add coding:gb2312 at the head
# of the code
dataPath = 'C:/Users/Lenovo/Desktop/rawData/rawCsv/北拒马河渠段水力观测（Ⅲ-Ⅲ断面）.csv'
outPath = u'C:/Users/Lenovo/Desktop/rawData/resultCsv/北拒马河渠段水力观测（Ⅲ-Ⅲ断面）.csv'    
# beacause the encoding is utf8,so if you want to name the outfile with chinese name,the prefix should be u

uipath = unicode(dataPath,"utf8")   # read the file with chinese name
f = open(uipath,'r')
f_out = open(outPath,'w')

all_context = f.read()   # this will return one string of the whole txt

raw = ['观测时间','气温','太阳辐射','测线','水深(m)','水温(℃)']
new = ['time','temperature','sunlight','line','waterDepth','waterTemperature']

for i in range(6):
    all_context = all_context.replace(raw[i],new[i]) 

# print all_context

f_out.write('time'+','+'temperature'+','+'sunlight'+',')
for i in range(1,12):
    if(i==11):
        f_out.write('line'+str(i)+'waterDepth'+','+'line'+str(i)+'Temperature')
    else:
        f_out.write('line'+str(i)+'waterDepth'+','+'line'+str(i)+'Temperature'+',')
f_out.write('\n')

f2 = all_context.split('\n')

for line in f2:
    if(line.split(',')[0]=="time"):
        st = line.split(',')
        time = st[1] 
        temperature = st[5]
        sunlight = st[9]
#         print time,temperature,sunlight
#         f_out.write(str(time)+','+str(temperature)+','+str(sunlight)+'\n')
    elif((reg(line)) and (line.find("DIV")==-1)):
        f_out.write(str(time)+','+str(temperature).strip()+','+str(sunlight).strip()+',')
        st = line.split(',')
        for index in range(1,23):
            if(index==22):
#                 print st[index].strip()
                f_out.write(st[index].strip()+'\n')
            else:
#                 print st[index].strip()+',' 
                f_out.write(st[index].strip()+',')
    else:
        pass
f_out.close() 