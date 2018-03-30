

#如何实现可迭代对象和迭代器对象


l = [1,2,3,4]
s ='abcd'

for x in l:print(x)
print("*"*20)
for x in s:print(x)

print(list(iter(l)))
