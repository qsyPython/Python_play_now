#经典类
#新式类

#类的定义
class Money:
    pass

#根据这个类,实例化一个对象
one = Money()
print(Money) #<class '__main__.Money'>
print(one) #<__main__.Money object at 0x1039c1940>

print("=====================对象属性相关")
#1.定义一个类
class Person:
    pass
#2.根据这个类创造一个对象
p = Person()

#3.给p对象,增加一些属性
p.age = 18
p.height = 180

#4.验证是否添加成功
print(p.age)

#查看当前对象的所有属性
print(p.__dict__)

#访问一个不存在的属性 (会报错)
# print(p.sex)

#对一个属性进行修改时,改变了指针的指向
p.pets = ["小花","小黑"]
print(p.pets,id(p.pets))
p.pets = [1,2]
print(p.pets,id(p.pets))
p.pets.append("小黄")
print(p.pets,id(p.pets))

#删除属性
print(p.age)
del p.age
# print(p.age) #报错

#不同的对象不能访问对方属性
p2 = Person()
p2.address = "上海"
# print(p.address)  #报错,p没有address属性

print("=====================类属性相关")
class Money1:
    pass
#增加类属性 方式1
Money1.count = 1
print(Money1.count)
print(Money1.__dict__)

#增加类属性 方式2 (常用)
class Money2:
    age = 18
    count = 1
    number = 666

#1.类属性查询
#通过类访问
print(Money2.age)
print(Money2.count)
print(Money2.number)
print(Money2.__dict__)

#通过对象访问
m = Money2()
print(m.age)
print(m.count)
print(m.number)

#2.类属性的修改
Money2.age = 22
print(Money2.age)
#有一点需要注意,如果是通过对象去修改类属性 eg:m.age = 33 这样只会给m这个对象增加一个age属性,而不能修改类属性的age
m = Money2()
print(Money2.age) #22
m.age = 19
print(Money2.age) #22  说明类属性age并没有改变
print(m.__dict__) #可以看到 m 对象中增加了一个age属性

#3.类属性的删除
#注意,不能通过对象进行删除
del Money2.age
#print(Money2.age)  #报错

#比如我想通过对象去删除一个类属性
o = Money2()
del o.number
# print(o.number)  #会报错, 因为o自身没有number属性,只有类有number,所以删除不了类的属性

#总结: 类型的查改删  只有查能通过对象去访问类属性,改和查都不能对类属性有任何操作





