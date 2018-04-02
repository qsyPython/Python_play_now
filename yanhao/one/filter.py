import timeit
from random import randint
#在-10到10之间生成10个元素

data = [randint(-10,10) for _ in range(10)]

def is_max(n):
    return n >=0

print(data)

#py2跟py3不一样  py3返回是一个迭代器 加上list将迭代器转换成列表
res = list(filter(lambda x:x >=0,data))
print(res)


#列表解析
data1 = [randint(-20,20) for _ in range(10)]

res1 = [x for x in data1 if x >= 0]

print(res1)


