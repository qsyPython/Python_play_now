import tensorflow as tf
import numpy as np
#import os
#os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'# 1 默认的显示等级，显示所有信息 2 只显示 warning 和 Error  3只显示 Error

# ---------------------------基础数据流图
# a=tf.constant(5,name="input_a")
# b=tf.constant(3,name="input_b")
#
# c=tf.multiply(a,b,name="mul_c")
# d=tf.add(a,b,name="add_d")
#
# e=tf.add(c,d,name="add_e")
#
# sess=tf.Session()
# print(sess.run(e))
# output=sess.run(e)
# writer=tf.summary.FileWriter('./my_graph',sess.graph)
#
# writer.close()
# sess.close()

#--------------------基础张量
# a=tf.constant([5,3],name="input_a")
# b=tf.reduce_prod(a,name="prod_b")
# c=tf.reduce_sum(a,name="sum_c")
# d=tf.add(c,b,name="add_d")

a=tf.add(2,5)

b=tf.multiply(a,3)
sess=tf.Session()
replace_dict={a:15}
print(sess.run(b,feed_dict=replace_dict))
writer=tf.summary.FileWriter('./my_graph',sess.graph)

writer.close()
sess.close()
