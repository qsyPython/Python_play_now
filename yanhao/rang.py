from random import randint
#词频统计

data = [randint(1,32) for _ in range(30)]

print(data)


c = dict.fromkeys(data,0)


for x in data:
    c[x] +=1


print(c)