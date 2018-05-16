#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 类定义
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, sName, iAge, iWeight):
        self.name = sName
        self.age = iAge
        self.__weight = iWeight

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 实例化类
oPeople = people('Jack', 10, 30)
oPeople.speak()


# 继承
class student(people):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构函
        people.__init__(self, n, a, w)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


oStudent = student('ken', 10, 60, 3)
oStudent.speak()


# 多重继承
class speaker():
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))


class sample(speaker, student):
    a = ''

    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)


test = sample("Tim", 25, 80, 4, "Python")
test.speak()  # 方法名同，默认调用的是在括号中排前地父类的方法


'''
类的专有方法：
__init__ :  构造函数，在生成对象时调用
__del__ :   析构函数，释放对象时使用
__repr__ :  打印，转换
__setitem__ : 按照索引赋值
__getitem__ : 按照索引获取值
__len__:    获得长度
__cmp__:    比较运算
__call__:   函数调用
__add__: 加运算
__sub__: 减运算
__mul__: 乘运算
__div__: 除运算
__mod__: 求余运算
__pow__: 乘方
'''