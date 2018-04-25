import tensorflow as tf
import numpy as np
#import os
#os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'# 1 默认的显示等级，显示所有信息 2 只显示 warning 和 Error  3只显示 Error


a=tf.constant(5,name="input_a")
b=tf.constant(3,name="input_b")

c=tf.multiply(a,b,name="mul_c")
d=tf.add(a,b,name="add_d")

e=tf.add(c,d,name="add_e")

sess=tf.Session()
print(sess.run(e))
