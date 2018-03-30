from collections import namedtuple

student =('jim',16,'male','jim8721@gmail.com')

#name
print(student[0])

#age
print(student[1])

#C语言用预定义或者枚举类型 python 没有枚举模拟枚举


NAME,AGE,SEX,EMAIL = range(4)


print(student[NAME])



#使用标准库

Student =namedtuple('Student',['name','age','sex','email'])

s =Student('dabin',18,'male','aaa@eeee.com')

print(s.name)



