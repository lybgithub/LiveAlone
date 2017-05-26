import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

def convert(date_str):
    a = datetime.strptime(date_str,'%Y-%m-%d %H:%M')
    return a

df = pd.read_csv('C:/Users/Administrator/Desktop/result_2.csv')
df['日期'] = pd.to_datetime(df['日期'])   # convert this column in dataframe into datetime
df = df.sort('日期')  # This now sorts in date order

df2 = df.copy()
df2 = df2[df2.location==2]  
df2 = df2[df2.line_id==1]
df2 = df2[df2['截面']==3]

date = list(df2['日期'])
temperature = np.array(df2['temperature']) 
pre = np.array(df2['pre'])  
# x = pd.to_datetime(date) 
# x2 = map(convert,date) 
y = temperature 
y2 = pre 

plt.figure(figsize=(12, 8))
plt.plot_date(date,y,'b-',linewidth=2,label='real data')
plt.plot_date(date,y2,'r-',linewidth=2,label='pre data')
plt.title('river data', fontsize=18) 
plt.legend(loc='upper left',numpoints=1)   #如果不使用这个不会图例不会显示出来
# plt.xlim(x.min() * 0.8, x.max() * 1.1)             #array数组可以使用max和min获得数组的最大和最小值.如果是list是不可以的
plt.ylim(y.min() * 0.8, y.max() * 1.3)

plt.grid() 
plt.savefig('./riverPic.png')
plt.show() 

