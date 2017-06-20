#!/usr/bin/python
# -*- coding:utf-8 -*-
import pydotplus
from sklearn.datasets import load_iris
from sklearn import tree

iris = load_iris()
clf = tree.DecisionTreeClassifier(criterion='gini')
clf = clf.fit(iris.data, iris.target)

with open("iris.dot", 'w') as f:
    f = tree.export_graphviz(clf, out_file=f)

dot_data = tree.export_graphviz(clf, out_file=None) 
graph = pydotplus.graph_from_dot_data(dot_data) 
graph.write_pdf("iris.pdf") 
## tip：add the path where gediv.exe in,eg:c:/../bin

from IPython.display import Image  
dot_data = tree.export_graphviz(clf,out_file=None, 
                         feature_names=iris.feature_names,  
                         class_names=iris.target_names,  
                         filled=True, rounded=True,  
                         special_characters=True)  
graph = pydotplus.graph_from_dot_data(dot_data)  
Image(graph.create_png())  
with open('iris.png', 'wb') as f:
        f.write(graph.create_png())
        f.close() 