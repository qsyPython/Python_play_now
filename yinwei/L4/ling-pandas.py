# 一、　　Pandas简介
#
# 1、Python Data Analysis Library 或 pandas 是基于NumPy 的一种工具，该工具是为了解决数据分析任务而创建的。Pandas 纳入了大量库和一些标准的数据模型，提供了高效地操作大型数据集所需的工具。
# pandas提供了大量能使我们快速便捷地处理数据的函数和方法。你很快就会发现，它是使Python成为强大而高效的数据分析环境的重要因素之一。
#
# 2、Pandas 是python的一个数据分析包，最初由AQR Capital Management于2008年4月开发，并于2009年底开源出来，
# 目前由专注于Python数据包开发的PyData开发team继续开发和维护，属于PyData项目的一部分。Pandas最初被作为金融数据分析工具而开发出来，因此，pandas为时间序列分析提供了很好的支持。
# Pandas的名称来自于面板数据（panel data）和python数据分析（data analysis）。panel data是经济学中关于多维数据集的一个术语，在Pandas中也提供了panel的数据类型。
#
# 3、数据结构：
#
# Series：一维数组，与Numpy中的一维array类似。二者与Python基本的数据结构List也很相近，其区别是：List中的元素可以是不同的数据类型，而Array和Series中则只允许存储相同的数据类型，这样可以更有效的使用内存，提高运算效率。
# Time- Series：以时间为索引的Series。
# DataFrame：二维的表格型数据结构。很多功能与R中的data.frame类似。可以将DataFrame理解为Series的容器。以下的内容主要以DataFrame为主。
# Panel ：三维的数组，可以理解为DataFrame的容器。
# Pandas 有两种自己独有的基本数据结构。读者应该注意的是，它固然有着两种数据结构，因为它依然是 Python 的一个库，所以，Python 中有的数据类型在这里依然适用，也同样还可以使用类自己定义数据类型。
# 只不过，Pandas 里面又定义了两种数据类型：Series 和 DataFrame，它们让数据操作更简单了。
# 二、　　Pandas安装
# 因为pandas是python的第三方库所以使用前需要安装一下，直接使用pip install pandas 就会自动安装pandas以及相关组件。

# from pandas import Series
# import pandas as pd
# s = Series([1,4,'ww','tt'])
# print(s)
#Series 就如同列表一样，一系列数据，每个数据对应一个索引值。

# Series 就是“竖起来”的 list：
# 0    1
# 1    4
# 2    ww
# 3    tt

# print(s.index)
#RangeIndex(start=0, stop=4, step=1)

# print(s.values)
#[1 4 'ww' 'tt']

# s2 = Series(['wangxing','man',24],index=['name','sex','age'])
#
# print(s2)
# name 　　 wangxing
# sex　　     man
# age 　　   24

# s2['name'] = 'lingdu'
# print(s2)
# name    lingdu
# sex        man
# age         24


# sd = {'python':9000,'c++':9001,'c#':9000}
#
# s3 = Series(sd)
#
# print(s3)
# c#        9000
# c++       9001
# python    9000

# s4 = Series(sd,index=['java','c++','c#'])

# print(s4)

# java       NaN
# c++     9001.0
# c#      9000.0

# 在 Pandas 中，如果没有值，都对齐赋给 NaN。

# Pandas 有专门的方法来判断值是否为空

# print(pd.isnull(s4))
#
# java     True
# c++     False
# c#      False

# Series就先简要写到这，下面看pandas的另一种数据结构DataFrame.


# DataFrame
# DataFrame 是一种二维的数据结构，非常接近于电子表格或者类似 mysql 数据库的形式。它的竖行称之为 columns，横行跟前面的 Series 一样，称之为 index，也就是说可以通过 columns 和 index 来确定一个主句的位置。

from pandas import Series,DataFrame

# data = {"name":['google','baidu','yahoo'],"marks":[100,200,300],"price":[1,2,3]}
#
# f1 = DataFrame(data)
#
# print(f1)

# 0    100  google      1
# 1    200   baidu      2
# 2    300   yahoo      3



