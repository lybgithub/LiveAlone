## first generate one network
## second make the dataset with numpy
## third train the network
## last save the weights and bias to checkpoints
## reload the checkpoints and then train the network based on it

import tensorflow as tf 
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
def createNetwork(X,layerList,activateFun):
#     loss = tf.losses.mean_squared_error(y,y_hat)
#     optimizer = tf.train.AdamOptimizer(0.001).minimize(loss)
    with tf.variable_scope('regression',reuse=True):
        layer_num = len(layerList) 
        for i in range(layer_num-1):
            with tf.variable_scope('layer%d'%(i+1),reuse=True): 
                layer_shape = [layerList[i],layerList[i+1]] 
                W = tf.Variable(tf.random_normal(shape=layer_shape,seed=1,stddev=1), dtype=tf.float32)
                b = tf.Variable(tf.constant(0.1,shape=[layer_shape[1]])) 
#                 W = tf.Variable(name='W',shape=layer_shape,initializer=tf.truncated_normal_initializer(stddev=1))
#                 print(layer_shape[1]) 
#                 b = tf.Variable(name='b',shape=[layer_shape[1]],initializer=tf.constant_initializer(value=0.1)) 
                X = tf.matmul(X,W)+b 
                if(i<layer_num-2 and activateFun is not None):
                    X = activateFun(X)
    return X


## make fake dataset
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-1, 1, 10000)[:,np.newaxis]          # shape (100, 1)
noise = np.random.normal(0, 0.1,size=x.shape)
y = np.power(x,2) + noise                          # shape (100, 1) + some noise
# plot data
print(x.shape)
plt.scatter(x, y)
plt.show() 



## train the network
## define the loss and make true the optimizer the get the session start and train the net

if __name__ == '__main__':
    X = tf.placeholder(name='x_input',shape=[None,1],dtype=tf.float32)
    Y = tf.placeholder(name='y_input',shape=[None,1],dtype=tf.float32)  
    layerList = [1,10,30,1] 
    y_hat = createNetwork(X,layerList,activateFun=tf.nn.relu) 
    loss = tf.losses.mean_squared_error(Y,y_hat)
    optimizer = tf.train.AdamOptimizer(0.5).minimize(loss)
    with tf.Session() as sess:
        init_op = tf.global_variables_initializer() 
        sess.run(init_op) 
        saver = tf.train.Saver() 
        for i in range(100):
            sess.run(optimizer,feed_dict={X:x,Y:y}) 
            y_pre = sess.run(y_hat,feed_dict={X:x}) 
        plt.scatter(x,y_pre) 
        plt.show() 
        saver.save(sess, "./checkpoint/model.ckpt") 

## restore the ckpt：
   	with tf.Session() as sess:
	    saver = tf.train.Saver() 
	    saver.restore(sess,"./checkpoint/model.ckpt") 
	    y_pre