# -*- coding: utf-8 -*-
from Tkinter import *
import tkFileDialog as tkfile
import os
import tkMessageBox
import pandas as pd
from PIL import Image, ImageTk
from alg514 import *
from paperlib import *
from autoWeight import *

class FeatureSelection():    
    def __init__(self, master):
        
        self.weight_list = [2,3,1]
        # set up the main frame
        self.parent = master
        self.parent.title("Feature Selection")
        self.frame = Frame(self.parent)
        self.frame.pack(fill = BOTH, expand = 1)
#         self.frame.pack()
#         self.parent.resizable(width = FALSE, height = FALSE)

        self.menubar = Menu(self.parent)
        self.algorithms = None

        #创建下拉菜单File，然后将其加入到顶级的菜单栏中
        self.algmenu = Menu(self.menubar,tearoff=0)
        self.algmenu.add_command(label="KMeans", command=self.alg1)
        self.algmenu.add_command(label="ReliefF", command=self.alg2)
        self.algmenu.add_command(label="MI", command=self.alg3)
        self.algmenu.add_command(label="Ensemble", command=self.alg4)
        self.menubar.add_cascade(label="算法", menu=self.algmenu)
        self.parent.config(menu=self.menubar)
        
        self.label = Label(self.frame, text = "原始数据集路径:")
        self.label.grid(row = 0, column = 0, sticky = W, padx = 10)
        self.entry = Listbox(self.frame, height = 1,width=50)
        self.entry.grid(row = 0, column = 1, sticky = W)
#         self.loadButton = Button(self.frame, text = "Load dataSet", width = 10)
        self.loadButton = Button(self.frame, text = "设置", width = 20, command = self.LoadDataDir)
        self.loadButton.grid(row = 0, column = 2, sticky = W+E, padx = 20, pady = 5)
        
        self.label2 = Label(self.frame, text = "结果数据集输出路径:")
        self.label2.grid(row = 1, column = 0, sticky = W, padx = 10) 
        self.entry2 = Listbox(self.frame, height = 1,width=50)
        self.entry2.grid(row = 1, column = 1, sticky = W)
        self.loadButton = Button(self.frame, text = "设置", width = 10, command = self.OutDataDir)
        self.loadButton.grid(row = 1, column = 2, sticky = W+E, padx = 20, pady = 5)
        
        self.bboxlabel = Label(self.frame, text = "提取特征数目:")
        self.bboxlabel.grid(row = 2, column = 0, sticky = W,padx = 10)
        self.entrylabel = Entry(self.frame, width = 50,textvariable=StringVar())
        self.entrylabel.grid(row = 2,column = 1, sticky = W, padx = 0)
        self.loadButton = Button(self.frame, text = "确定", width = 10, command = self.getFeatureNum)
        self.loadButton.grid(row = 2, column = 2, sticky = W+E, padx = 20, pady = 5)
        
        self.loadButton = Button(self.frame, text = "绘制参考曲线", width = 35, command = self.save_plotImage)
        self.loadButton.grid(row = 3,column=1,sticky = W+E, padx = 20, pady = 5)
        
        self.loadButton = Button(self.frame, text = "输出结果特征文件", width = 2,command = self.algorithms)
        self.loadButton.grid(row = 4,column=1,sticky = W+E, padx = 20, pady = 5) 
        
        
    def alg1(self):
        self.algorithms = "kmeans"
        tkMessageBox.showinfo("Warning","选择的特征选择算法是:KMeans")
    def alg2(self):
        self.algorithms = "relieff"
        tkMessageBox.showinfo("Warning","选择的特征选择算法是:ReliefF") 
    def alg3(self):
        self.algorithms = "mi"
        tkMessageBox.showinfo("Warning","选择的特征选择算法是:MI")
    def alg4(self):
        self.algorithms = "ensemble"
        tkMessageBox.showinfo("Warning","选择的特征选择算法是:ensemble")
    

    def save_plotImage(self):
        weightList = self.weight_list
        datapath = self.datadir
        alg_name = self.algorithms
        plot_image(datapath,alg_name,weightList)
#        self.LoadImage()
        
    def LoadImage(self):
        window =Toplevel()
        window.title('picture result') 
        canvas = Canvas(window,cursor = "tcross", width=500,height=500)
        canvas.pack(expand=YES,fill=BOTH)
        imagepath = './test.png'
        pro_image = Image.open(imagepath)
        self.cur_img = ImageTk.PhotoImage(pro_image)
        canvas.create_image(0, 0,image = self.cur_img, anchor = NW) 
    
    def LoadDataDir(self):
        self.datadir = tkfile.askopenfilename()
        self.entry.insert(0, self.datadir)
        self.LoadData()

    def LoadData(self):
        datapath = self.datadir
#         tkMessageBox.showinfo('imageMessage',datapath)
        df = pd.read_csv(datapath,header=None)
        featureNum = int(len(df.columns)-1)
        tkMessageBox.showinfo("Warning","数据集一共有%d个特征,请输入小于%d的特征数目"%(featureNum,featureNum))
        
    def OutDataDir(self):
        self.dataoutdir = tkfile.askdirectory()
        self.entry2.insert(0, self.dataoutdir)
        tkMessageBox.showinfo('imageMessage',self.dataoutdir)
     
    def getFeatureNum(self):
        self.featureNum = self.entrylabel.get()
        tkMessageBox.showinfo('特征选择数目',self.featureNum)
        
    def algorithms(self):
        fsNumStr = str(self.featureNum)
        fsNum = int(self.featureNum)
        dataPath = self.datadir
        algorithms = self.algorithms
        weightList = self.weight_list 
        
        outName = str(dataPath)
        outName = outName.split('/')[-1]
        outName = outName.split('.')[0]
#        print outName
        outPath = self.dataoutdir
        outPath = os.path.join(outPath,'%s_%s_%s.csv'%(outName,algorithms,fsNumStr))
        
        if(algorithms=="kmeans"):
            y,topN = gen_evalList(dataPath,fsNum)
        if(algorithms=="relieff"):
            y,topN = fsReliefF(dataPath,fsNum)
        if(algorithms=="mi"):
            y,topN = fsMI(dataPath,fsNum)
        if(algorithms=="ensemble"):
            y,topN = fsEnsemble(dataPath,weightList,fsNum)
        df = pd.read_csv(dataPath,header=None)
        arraySelected = df.values[:,topN+[-1]]   # contain the features and the label
#         print arraySelected
        outFile = open(outPath,'w')
        lineLen = len(arraySelected[0])
        for line in arraySelected:
            for i in range(lineLen):
                if(i==lineLen-1):
                    outFile.write(str(line[i])+'\n')
                else:
                    outFile.write(str(line[i])+',')
        outFile.close()
        tkMessageBox.showinfo('Message','successful!')
        
if __name__ == "__main__":
    root = Tk() 
    tool = FeatureSelection(root)
    root.mainloop()