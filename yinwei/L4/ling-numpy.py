# numpy(Numerical Python extensions)是一个第三方的Python包，用于科学计算。

# import numpy as np
#
# a = [1, 2, 3, 4]  #
# b = np.array(a)
# print(b)# array([1, 2, 3, 4])
# print(type(b))  # <type 'numpy.ndarray'>
#
#
# print(b.shape)  # (4,)
# print(b.argmax())  # 3
# print(b.max())  # 4
# print(b.mean())  # 2.5
#
# c = [[1, 2], [3, 4]]  # 二维列表
# d = np.array(c)  # 二维numpy数组
# d.shape  # (2, 2)
# d.size  # 4
# d.max(axis=0)  # 找维度0，也就是最后一个维度上的最大值，array([3, 4])
# d.max(axis=1)  # 找维度1，也就是倒数第二个维度上的最大值，array([2, 4])
# d.mean(axis=0)  # 找维度0，也就是第一个维度上的均值，array([ 2.,  3.])
# d.flatten()  # 展开一个numpy数组为1维数组，array([1, 2, 3, 4])
# np.ravel(c)  # 展开一个可以解析的结构为1维数组，array([1, 2, 3, 4])
#
# # 3x3的浮点型2维数组，并且初始化所有元素值为1
# e = np.ones((3, 3), dtype=np.float)
#
# # 创建一个一维数组，元素值是把3重复4次，array([3, 3, 3, 3])
# f = np.repeat(3, 4)
#
# # 2x2x3的无符号8位整型3维数组，并且初始化所有元素值为0
# g = np.zeros((2, 2, 3), dtype=np.uint8)
# g.shape  # (2, 2, 3)
# h = g.astype(np.float)  # 用另一种类型表示
#
# l = np.arange(10)  # 类似range，array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# m = np.linspace(0, 6, 5)  # 等差数列，0到6之间5个取值，array([ 0., 1.5, 3., 4.5, 6.])
#
# p = np.array(
#     [[1, 2, 3, 4],
#      [5, 6, 7, 8]]
# )


# import numpy as np
#
# '''
# array([[[ 0,  1,  2,  3],
#         [ 4,  5,  6,  7],
#         [ 8,  9, 10, 11]],
#
#        [[12, 13, 14, 15],
#         [16, 17, 18, 19],
#         [20, 21, 22, 23]]])
# '''
# a = np.arange(24).reshape((2, 3, 4))
# b = a[1][1][1]  # 17
# print(b)
#
# '''
# array([[ 8,  9, 10, 11],
#        [20, 21, 22, 23]])
# '''
# c = a[:, 2, :]
#
# ''' 用:表示当前维度上所有下标
# array([[ 1,  5,  9],
#        [13, 17, 21]])
# '''
# d = a[:, :, 1]
#
# ''' 用...表示没有明确指出的维度
# array([[ 1,  5,  9],
#        [13, 17, 21]])
# '''
# e = a[..., 1]
#
# '''
# array([[[ 5,  6],
#         [ 9, 10]],
#
#        [[17, 18],
#         [21, 22]]])
# '''
# f = a[:, 1:, 1:-1]
#
# '''
# 平均分成3份
# [array([0, 1, 2]), array([3, 4, 5]), array([6, 7, 8])]
# '''
# g = np.split(np.arange(9), 3)
#
# '''
# 按照下标位置进行划分
# [array([0, 1]), array([2, 3, 4, 5]), array([6, 7, 8])]
# '''
# h = np.split(np.arange(9), [2, -3])
#
# l0 = np.arange(6).reshape((2, 3))
# l1 = np.arange(6, 12).reshape((2, 3))
#
# '''
# vstack是指沿着纵轴拼接两个array，vertical
# hstack是指沿着横轴拼接两个array，horizontal
# 更广义的拼接用concatenate实现，horizontal后的两句依次等效于vstack和hstack
# stack不是拼接而是在输入array的基础上增加一个新的维度
# '''
# m = np.vstack((l0, l1))
# p = np.hstack((l0, l1))
# q = np.concatenate((l0, l1))
# r = np.concatenate((l0, l1), axis=-1)
# s = np.stack((l0, l1))
#
# '''
# 按指定轴进行转置
# array([[[ 0,  3],
#         [ 6,  9]],
#
#        [[ 1,  4],
#         [ 7, 10]],
#
#        [[ 2,  5],
#         [ 8, 11]]])
# '''
# t = s.transpose((2, 0, 1))
#
# '''
# 默认转置将维度倒序，对于2维就是横纵轴互换
# array([[ 0,  4,  8],
#        [ 1,  5,  9],
#        [ 2,  6, 10],
#        [ 3,  7, 11]])
# '''
# u = a[0].transpose()	# 或者u=a[0].T也是获得转置
#
# '''
# 逆时针旋转90度，第二个参数是旋转次数
# array([[ 3,  2,  1,  0],
#        [ 7,  6,  5,  4],
#        [11, 10,  9,  8]])
# '''
# v = np.rot90(u, 3)
#
# '''
# 沿纵轴左右翻转
# array([[ 8,  4,  0],
#        [ 9,  5,  1],
#        [10,  6,  2],
#        [11,  7,  3]])
# '''
# w = np.fliplr(u)
#
# '''
# 沿水平轴上下翻转
# array([[ 3,  7, 11],
#        [ 2,  6, 10],
#        [ 1,  5,  9],
#        [ 0,  4,  8]])
# '''
# x = np.flipud(u)
#
# '''
# 按照一维顺序滚动位移
# array([[11,  0,  4],
#        [ 8,  1,  5],
#        [ 9,  2,  6],
#        [10,  3,  7]])
# '''
# y = np.roll(u, 1)
#
# '''
# 按照指定轴滚动位移
# array([[ 8,  0,  4],
#        [ 9,  1,  5],
#        [10,  2,  6],
#        [11,  3,  7]])
# '''
# z = np.roll(u, 1, axis=1)

# 基础数学运算也是强大

# import numpy as np
#
# # 绝对值，1
# a = np.abs(-1)
# print(a)
#
# # sin函数，1.0
# b = np.sin(np.pi/2)
# print(b)
#
# # tanh逆函数，0.50000107157840523
# c = np.arctanh(0.462118)
# print(c)
#
# # e为底的指数函数，20.085536923187668
# d = np.exp(3)
# print(d)
#
# # 2的3次方，8
# f = np.power(2, 3)
# print(f)
#
# # 点积，1*3+2*4=11
# g = np.dot([1, 2], [3, 4])
# print(g)
#
# # 开方，5
# h = np.sqrt(25)
# print(h)
#
# # 求和，10
# l = np.sum([1, 2, 3, 4])
# print(l)
#
# # 平均值，5.5
# m = np.mean([4, 5, 6, 7])
# print(m)
#
# # 标准差，0.96824583655185426
# p = np.std([1, 2, 3, 2, 1, 3, 2, 0])
# print(p)


# import numpy as np
#
# a = np.array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])
#
# b = np.array([
#     [1, 2, 3],
#     [1, 2, 3]
# ])
#
# '''
# 维度一样的array，对位计算
# array([[2, 4, 6],
#        [5, 7, 9]])
# '''
# a + b
#
# '''
# array([[0, 0, 0],
#        [3, 3, 3]])
# '''
# a - b
#
# '''
# array([[ 1,  4,  9],
#        [ 4, 10, 18]])
# '''
# a * b
#
# '''
# array([[1, 1, 1],
#        [4, 2, 2]])
# '''
# a / b
#
# '''
# array([[ 1,  4,  9],
#        [16, 25, 36]])
# '''
# a ** 2
#
# '''
# array([[  1,   4,  27],
#        [  4,  25, 216]])
# '''
# a ** b
#
# c = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [10, 11, 12]
# ])
# d = np.array([2, 2, 2])
#
# '''
# 广播机制让计算的表达式保持简洁
# d和c的每一行分别进行运算
# array([[ 3,  4,  5],
#        [ 6,  7,  8],
#        [ 9, 10, 11],
#        [12, 13, 14]])
# '''
# c + d
#
# '''
# array([[ 2,  4,  6],
#        [ 8, 10, 12],
#        [14, 16, 18],
#        [20, 22, 24]])
# '''
# c * d
#
# '''
# 1和c的每个元素分别进行运算
# array([[ 0,  1,  2],
#        [ 3,  4,  5],
#        [ 6,  7,  8],
#        [ 9, 10, 11]])
# '''
# c - 1


# 线性代数模块（linalg）
#结合numpy提供的基本函数，可以对向量，矩阵，或是说多维张量进行一些基本的运算

# import numpy as np
#
# a = np.array([3, 4])
# np.linalg.norm(a)
#
# b = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])
# c = np.array([1, 0, 1])
#
# # 矩阵和向量之间的乘法
# np.dot(b, c)            		# array([ 4, 10, 16])
# np.dot(c, b.T)          		# array([ 4, 10, 16])
#
# np.trace(b)             		# 求矩阵的迹，15
# np.linalg.det(b)        		# 求矩阵的行列式值，0
# np.linalg.matrix_rank(b)	# 求矩阵的秩，2，不满秩，因为行与行之间等差
#
# d = np.array([
#     [2, 1],
#     [1, 2]
# ])
#
# '''
# 对正定矩阵求本征值和本征向量
# 本征值为u，array([ 3.,  1.])
# 本征向量构成的二维array为v，
# array([[ 0.70710678, -0.70710678],
#        [ 0.70710678,  0.70710678]])
# 是沿着45°方向
# eig()是一般情况的本征值分解，对于更常见的对称实数矩阵，
# eigh()更快且更稳定，不过输出的值的顺序和eig()是相反的
# '''
# u, v = np.linalg.eig(d)
#
# # Cholesky分解并重建
# l = np.linalg.cholesky(d)
#
# '''
# array([[ 2.,  1.],
#        [ 1.,  2.]])
# '''
# np.dot(l, l.T)
#
# e = np.array([
#     [1, 2],
#     [3, 4]
# ])
#
# # 对不镇定矩阵，进行SVD分解并重建
# U, s, V = np.linalg.svd(e)
#
# S = np.array([
#     [s[0], 0],
#     [0, s[1]]
# ])
#
# '''
# array([[ 1.,  2.],
#        [ 3.,  4.]])
# '''
# np.dot(U, np.dot(S, V))

#随机模块（random）

# import numpy as np
# import numpy.random as random
#
# # 设置随机数种子
# random.seed(42)
#
# # 产生一个1x3，[0,1)之间的浮点型随机数
# # array([[ 0.37454012,  0.95071431,  0.73199394]])
# # 后面的例子就不在注释中给出具体结果了
# random.rand(1, 3)
#
# # 产生一个[0,1)之间的浮点型随机数
# random.random()
#
# # 下边4个没有区别，都是按照指定大小产生[0,1)之间的浮点型随机数array，不Pythonic…
# random.random((3, 3))
# random.sample((3, 3))
# random.random_sample((3, 3))
# random.ranf((3, 3))
#
# # 产生10个[1,6)之间的浮点型随机数
# 5*random.random(10) + 1
# random.uniform(1, 6, 10)
#
# # 产生10个[1,6]之间的整型随机数
# random.randint(1, 6, 10)
#
# # 产生2x5的标准正态分布样本
# random.normal(size=(5, 2))
#
# # 产生5个，n=5，p=0.5的二项分布样本
# random.binomial(n=5, p=0.5, size=5)
#
# a = np.arange(10)
#
# # 从a中有回放的随机采样7个
# random.choice(a, 7)
#
# # 从a中无回放的随机采样7个
# random.choice(a, 7, replace=False)
#
# # 对a进行乱序并返回一个新的array
# b = random.permutation(a)
#
# # 对a进行in-place乱序
# random.shuffle(a)
#
# # 生成一个长度为9的随机bytes序列并作为str返回
# # '\x96\x9d\xd1?\xe6\x18\xbb\x9a\xec'
# random.bytes(9)