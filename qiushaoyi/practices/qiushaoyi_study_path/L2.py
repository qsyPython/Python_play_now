'''
	作者：邱少一
	日期：2018/ / 
	功能：

	模块和文件处理（系统模块和第3方模块使用，文件I/O和序列化）；
    类和实例（创建、使用、面向对象的特性详解、枚举类；多重继承和元类）
    异常处理和代码测试（python的异常处理，函数和类的测试）；
'''
# /usr/bin/env python
# -*- coding: utf-8 -*-

模块、包；
作用域；
环境变量；用pythonPath设置
绑定；封装；私有变量的
访问与修改
get和set
或者
可以通过_Student__name来访问__name变量
继承：免费全部财产获取
多态：重名def覆盖；好处：父类instance作为形参，可传入任意子类的实参，调用该子类的def。
动态语言再拓展：形参在赋值实参之前，可以在def中用形参做任何操作，实现任意绑定。

# 4个类
class Student():
    def grade(self):
        print('哇要考试啦！')


class goodStudent(Student):
    def grade(self):
        print('哇满分！')


class badStudent(Student):
    def grade(self):
        print('哇零分')


class Pig():
    def grade(self):
        print('精品猪肉！')


# 一个函数: 形参在赋值实参之前，可以用形参做任何操作
def kind(sth):
    sth.grade()


student = Student()
good = goodStudent()
bad = badStudent()
pig = Pig()

kind(student)
kind(good)
kind(bad)
kind(pig)

类属性：在class中不用self，直接用变量名进行的赋值；注意：实例和类名都可以调用；
若单独给某个实例绑定属性，由于属性优先级比类属性高，所以，仅仅是该实例会拥有了该属性；s.name = 'woca'
若再删除实例属性，则该类属性就又回来了。del s.name；

__slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称，限制该class实例能添加的属性
有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量？
get和set的def可以下岗了，因为有了 @ property。

@property
def score(self):  # getter
    return self._score


@score.setter
def score(self, value):  # setter
    if not isinstance(value, int):
        raise ValueError('score must be an integer!')
    if value < 0 or value > 100:
        raise ValueError('score must between 0 ~ 100!')
    self._score = value


多重继承，这个比较吊！

定制类：说白了就是重写class里面的私有def, 如：__init__;
__str__;
__iter__

type()
Class类型;
isinstance
issubclass
bool判断；
dir(o)
获得一个
对象
的所有属性和方法;
len(o)

metaclass
先定义类，然后创建实例;
创建类：先创建元类，然后创建类；
全部其实是综合：先定义metaclass，就可以创建类，最后创建实例。

# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):  # 元类
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):  # 类
    pass


mylist = MyList()  # 实例
mylist.add(1)
print(mylist)

metaclass使用：ORM框架
对象关系映射。

try...except...finally...的错误处理机制：finally可不要，但有的话一定会执行。
记录错误：logging模块, 打印错误后
可以继续执行
并退出
try:
    bar('0')
except Exception as e:
    logging.exception(e)

抛出错误：raise ValueError('某个问题：%s' % s)

调试：print
小学；assert （如：assert n != 0, 'n is zero!'）小学
pdb：逐行，小范围调试。

import logging

logging.basicConfig(level=logging.INFO)  # 记录信息的级别
loggin：好用（logging.info('n = %d' % n)
或者
logging.debug('n = %d' % n)）
IDE
最6可断点

单元测试：unittest模块.如：编写
mydict_test.py
模块

import unittest
from mydict import Dict


class TestDict(unittest.TestCase):
    # 每个测试方法调用前后是否会打印出setUp...和tearDown...。
    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

    def test_init(self):  # test开头的方法都是测试方法
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):  # test开头的方法都是测试方法
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):  # test开头的方法都是测试方法
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):  # test开头的方法都是测试方法
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):  # test开头的方法都是测试方法
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty


if __name__ == '__main__':
    unittest.main()

终端：python
mydict_test.py
即可当做脚本执行了
或者
python - m
unittest
mydict_test

文档测试doctest：直接提取注释中的代码并执行测试
if __name__ == '__main__':
    import doctest

    doctest.testmod()

文件处理：
try:
    f = open('/path/to/file', 'r')
    print(f.read())
finally:
    if f:
        f.close()

等效于
with open(filepath, mode='r', encoding='utf-8') as f:

from io import stringIO / BytesIO
fileIO：文件的输入输出
stringIO: 字符串的输入输出
BytesIO：二进制的输入输出
注意：中文需要encode一下

文件处理和目录：os模块
# 查看当前目录的绝对路径:
>> > os.path.abspath('.')
'/Users/michael'

# 分2步：在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
>> > os.path.join('/Users/michael', 'testdir')
'/Users/michael/testdir'
# 然后创建一个目录:
>> > os.mkdir('/Users/michael/testdir')

# 删掉一个目录:
>> > os.rmdir('/Users/michael/testdir')

序列化：pickle模块（只能用于Python，并且可能不同版本的Python彼此都不兼容） 和json
序列化->写入磁盘
f = open('dump.txt', 'wb')
>> > pickle.dump(d, f)
>> > f.close()
反序列化->重新读到内存
>> > f = open('dump.txt', 'rb')
>> > d = pickle.load(f)
>> > f.close()
>> > d
{'age': 20, 'score': 88, 'name': 'Bob'}

json具体的方法如下：
dumps
和
loads
