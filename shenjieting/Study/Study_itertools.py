

import itertools

# Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。


# count()会创建一个无限的迭代器，所以上述代码会打印出自然数序列，根本停不下来，只能按Ctrl+C退出
# natuals = itertools.count(1)
# for n in  natuals:
#     print("count():{}".format(n))

# cycle() 会把传入的序列无限重复下去
# cs = itertools.cycle('ABC') #字符串也是序列的一种
# for c in cs:
#     print("cycle():{}".format(c))

# repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：
# ns = itertools.repeat('A', 3)
# for n in ns:
#     print("repeat():{}".format(n))

# 无限序列只有在for迭代时才会无限地迭代下去，如果只是创建了一个迭代对象，它不会事先把无限个元素生成出来，事实上也不可能在内存中创建无限多个元素。
# 无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列：
'''
lambda表示匿名函数
1.lambda只是一个表达式，函数体比def简单很多。
2.lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
3.lambda表达式是起到一个函数速写的作用。允许在代码内嵌入一个函数的定义。
注：  冒号:之前的表示它们是这个函数的参数。匿名函数不需要return来返回值，表达式本身结果就是返回值。
'''
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print("count():{}".format(list(ns)))

# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：给它一个列表如 lists/tuples/iterables，链接在一起；返回iterables对象。
for c in itertools.chain('ABC','XYZ'):
    print("chain():{}".format(c))

# groupby()把迭代器中相邻的重复元素挑出来放在一起：
for key,group in  itertools.groupby('AAABBBCCAAA'):
    print("groupby():",key,list(group))

# 实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，这两个元素就被认为是在一组的，
# 而函数返回值作为组的key。如果我们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的key：
for key,group in itertools.groupby('AaaaBBBbcCAAa', lambda c:c.upper()):#upper()方法将字符串中的小写字母转为大写字母。 返回小写字母转为大写字母的字符串。
    print("groupby() upper:", key, list(group))

