#!/usr/bin/python

# itertools
"""
Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。

首先，我们看看itertools提供的几个“无限”迭代器：

"""

import itertools

# 因为count()会创建一个无限的迭代器，所以上述代码会打印出自然数序列，根本停不下来，只能按Ctrl+C退出。
natuals = itertools.count(1)
for n in natuals:
    print(n)
    if n > 100:
        break
# cycle()会把传入的一个序列无限重复下去：
cs = itertools.cycle('ABC')
for c in cs:
    print (c)
    if c == 'C':
        break

# repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：
ns = itertools.repeat('A', 10)
for n in ns:
    print(n)

# 无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列：
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
for n in ns:
    print(n)


# chain()
# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：

for c in itertools.chain('ABC', 'XYZ'):
    print (c)

# groupby()
# groupby()把迭代器中相邻的重复元素挑出来放在一起：
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))

"""
实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，
这两个元素就被认为是在一组的，而函数返回值作为组的key。如果我们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的key：
"""

for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))

'''  没有imap函数
# imap()
# imap()和map()的区别在于，imap()可以作用于无穷序列，并且，如果两个序列的长度不一致，以短的那个为准。
注意imap()返回一个迭代对象，而map()返回list。当你调用map()时，已经计算完毕：
r = map(lambda x: x*x, [1, 2, 3])   
当你调用imap()时，并没有进行任何计算：
 r = itertools.imap(lambda x: x*x, [1, 2, 3])
必须用for循环对r进行迭代，才会在每次循环过程中计算出下一个元素：
for x in r:
   print x
这说明imap()实现了“惰性计算”，也就是在需要获得结果的时候才计算。类似imap()这样能够实现惰性计算的函数就可以处理无限序列：

r = itertools.imap(lambda x: x*x, itertools.count(1))
for n in itertools.takewhile(lambda x: x<100, r):
print n

for x in itertools.imap(lambda x, y: x * y, [10, 20, 30], itertools.count(1)):
    print(x)
'''

"""
starmap()
针对list中的每一项，调用函数功能。starmap(func,list[]) ；
"""
from itertools import *

x = starmap(max,[[5,14,5],[2,34,6],[3,5,2]])
for i in  x:
    print(i)

