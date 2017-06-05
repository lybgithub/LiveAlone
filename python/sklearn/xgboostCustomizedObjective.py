## maxRecall只是一个评估效果的函数，后面的custom_loss才是真正的损失函数
## 需要注意的一点是，这里的目标函数objective function就是loss函数，所以后面在train的时候，obj = loss，feval只是我们根据
## 我们自己定义的损失函数制定的一个评测函数而已
## 在train参数里面，需要加上maximize参数的值为False


def maxRecall(preds,dtrain): #preds是结果（概率值），dtrain是个带label的DMatrix
    labels=dtrain.get_label() #提取label
    preds=1-preds
    precision,recall,threshold=precision_recall_curve(labels,preds,pos_label=0)
    pr=pd.DataFrame({'precision':precision,'recall':recall})
    return 'Max Recall:',pr[pr.precision>=0.97].recall.max()

## 自己定义的损失函数需要返回两个值，原始损失函数的一阶导数和二阶导数
def custom_loss(y_pre,dtrain): #别人的自定义损失函数
    label=dtrain.get_label()
    penalty=2.0
    grad=-label/y_pre+penalty*(1-label)/(1-y_pre) #梯度
    hess=label/(y_pre**2)+penalty*(1-label)/(1-y_pre)**2 #2阶导
    return grad,hess


bst=xgb.train(param,xg_train,n_round,watchlist,feval=maxRecall,obj=custom_loss,maximize=False)