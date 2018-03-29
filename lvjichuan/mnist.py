# 下载mnist数据集,用于模拟训练
# mnist是一个轻量级的类。它以Numpy数组的形式存储着训练、校验和测试数据集。
import input_data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)