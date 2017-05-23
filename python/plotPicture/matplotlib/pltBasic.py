import numpy as np
import matplotlib.pyplot as plt
# x = [1,2,3,5,6,8]
# y = [2,3,4,6,9,11]
x = np.array([1,2,3,5,6,8])              # the performance will be better if the x,y are array like,this way,you can use xlim and ylim
y = np.array([2,3,4,6,9,11]) 
y2 = np.array([5,2,11,10,2,6])
# plt.plot(x,y) 
plt.plot(x,y,'r-o',linewidth=2,label='real')
plt.plot(x,y2,'b--^',linewidth=2,markersize=8,drawstyle='steps-post',label='test')    # wo can also display every dot!
# 'r-o'中的o是可选的，如果有这个就是源数据中每一个点
# linewidth和markersize分别是红色的线宽和绿色的点宽
# drawstyle可以改变插值方式
plt.title('title for test', fontsize=18)
plt.legend(loc='upper right',numpoints=1)   #如果不使用这个不会图例不会显示出来
plt.xlim(x.min() * 0.8, x.max() * 1.1)             #array数组可以使用max和min获得数组的最大和最小值.如果是list是不可以的
plt.ylim(y.min() * 0.8, y.max() * 1.3)

plt.grid() 
plt.show()


##############################################################

# -*- coding:utf-8 -*-       
# 上面一行保证，中文能正常转码
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams['font.sans-serif'] = [u'simHei']    # 保证上图像的中文能正常显示
mpl.rcParams['axes.unicode_minus'] = False

# x = [1,2,3,5,6,8]
# y = [2,3,4,6,9,11]
x = np.array([1,2,3,5,6,8])
y = np.array([2,3,4,6,9,11]) 
y2 = np.array([5,2,11,10,2,6])
# plt.plot(x,y) 
plt.plot(x,y,'r-',linewidth=2,label='real')
plt.plot(x,y2,'b-',linewidth=2,label='test')
plt.title(u'正常显示中文', fontsize=18)
plt.legend(loc='upper right')   #如果不使用这个不会图例不会显示出来
plt.xlim(x.min() * 0.8, x.max() * 1.1)             #array数组可以使用max和min获得数组的最大和最小值.如果是list是不可以的
plt.ylim(y.min() * 0.8, y.max() * 1.3)

plt.grid() 
plt.show()

#################################################
# 使用plt.figure,subplot在一个figure中画多张图

plt.figure(figsize=(8, 8), facecolor='grey')    #先设置外面的figure

plt.subplot(311)
x = np.arange(0,11,10)
y = np.arange(10,21,10)
plt.plot(x, y, 'g-', lw=2)   #lw是线宽
plt.title(u'频域信号', fontsize=15)   #分标题

##设置坐标轴的取值范围

plt.xlim(x.min() * 1.1, x.max() * 1.1)         #array数组可以使用max和min获得数组的最大和最小值
plt.ylim(y.min() * 1.1, y.max() * 1.1)
## 换下一个子图的框架，继续画图

plt.subplot(312)
x = np.linspace(0,100,10)
y = np.logspace(0,10,10,base=2)
plt.plot(x,y,'ro',lw=3) 
plt.title(u'李长远', fontsize=15)   #分标题

plt.subplot(313)
plt.plot(x,y,'r-',label='default',lw=3)                         
plt.plot(x,y,'b-', drawstyle='steps-post',label='step-post',lw=3)    #使用参数drawstyle改变插值方式，这里不能把drawstyle去掉，会识别不出来
plt.title(u'三角波', fontsize=15)                  #分标题
plt.xlim(x.min() * 1.1, x.max() * 1.1)             #array数组可以使用max和min获得数组的最大和最小值
plt.ylim(y.min() * 1.1, y.max() * 1.1)
plt.legend(loc='upper left')                       #设置图例的位置
#总标题
plt.suptitle(u'快速傅里叶变换FFT与频域滤波', fontsize=17)
plt.show()