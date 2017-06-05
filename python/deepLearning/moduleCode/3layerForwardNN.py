import tensorflow as tf

## 定义变量
w1= tf.Variable(tf.random_normal([2, 3], stddev=1, seed=1))
w2= tf.Variable(tf.random_normal([3, 1], stddev=1, seed=1))
x = tf.constant([[0.7, 0.9]])  
## 定义前向传播的网络
a = tf.matmul(x, w1)
y = tf.matmul(a, w2)
## 调用会话输出结果
sess = tf.Session()
sess.run(w1.initializer)  
sess.run(w2.initializer)  
print(sess.run(y))  
sess.close()


## 使用placeholder处理多个输入
x = tf.placeholder(tf.float32, shape=(3, 2), name="input")
a = tf.matmul(x, w1)
y = tf.matmul(a, w2)

sess = tf.Session()
#使用tf.global_variables_initializer()来初始化所有的变量
init_op = tf.global_variables_initializer()  
sess.run(init_op)

print(sess.run(y, feed_dict={x: [[0.7,0.9],[0.1,0.4],[0.5,0.8]]})) 