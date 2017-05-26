import codecs
filename = "C:/Users/Lenovo/Desktop/result.csv"
with codecs.open(filename,'r',encoding='gbk') as f:
    text = f.read()
# process Unicode text
with codecs.open(filename,'w',encoding='utf8') as f:
    f.write(text)