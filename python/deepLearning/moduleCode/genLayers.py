import tensorflow as tf 

def createNetwork(X,layerList,activateFun):
	with Variable.scope('regression or classifier'):
		layer_num = len(layerList)
		for i in range(layer_num-1):
			with Variable.scope('layer%d'%(i+1)):
				layer_shape = [layerList[i],layerList[i+1]]
				W = tf.get_varible(name='W',shape=layer_shape,initializer)
				b = tf.get_varible(name='b',shape=layer_shape[i+1],initializer)
				X = tf.matmul(X,w)+b
				if(i<layer_num-2 and activateFun is not None):
					X = activateFun(X)			
	return X
