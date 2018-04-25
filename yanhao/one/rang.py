from random import randint
from collections import  Counter

#词频统计

data = [randint(1,32) for _ in range(30)]

print(data)


c = dict.fromkeys(data,0)


for x in data:
    c[x] +=1


print(c)

#使用Counter

c2 = Counter(data)

#获取频率最高的三个
print(c2.most_common(3))

print(c2)




