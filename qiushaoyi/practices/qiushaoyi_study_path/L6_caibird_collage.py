import os, math, sys, re, socket, tkinter, json

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

import _thread, time, threading, queue, xml.sax

# 文件目录：
# 1、python    内置函数
# 2、静态方法无需实例化
# 3、等价比较
# 4、数学
# 5、文件
# 6、迭代
# 7、格式化print
# 8、全局变量：打印当前函数或文件内的全部局部变量
# 9、编码和变量
# 10、编译执行
# 11、属性判断
# 12、排序：元祖中第0个数据升序(False)、降序（True）
# 13、创建类: 类变量（empCount 和 empTest）、实例变量（方法中的变量：name、salary）、方法（如下面def的动态方法和@staticmethod的静态方法）
# 14、添加新的属性
# 15、对象销毁：垃圾回收和循环垃圾收集器（补充用于清除所有未被引用的循环）
# 16、类的继承
# 17、基础重载方法 和 运算符重载
# 18、__双下划线表示私有的，不能用实例变量在方法外调用，但可以在方法内调用
# 19、正则表达式
# 20、CGI编程：一段程序,运行在服务器上 暂未
# 21、数据库 暂未
# 22、Python 网络编程 暂未
# 23、邮件收发
# 24、为线程定义一个函数
# 25、解析XML实例
# 26、Python GUI编程: tkinter


# 1、python    内置函数
value = abs(-45)
tuple = divmod(7, 2)
inputStr = input('请输入你要说的话：')


class C(object):
    @staticmethod
    def f():
        print('类C里面有个定义名为f的静态函数')


# 2、静态方法无需实例化
C.f()

# 也可以实例化后调用
cobj = C()
cobj.f()

seq = ['one', 'two', 'three']
for i, element in enumerate(seq):
    print(i, seq[i])

t1 = all(seq)
t2 = any(seq)
convertValue = int(3.6)
a1 = ord('e')
a2 = str({'runoob': 'runoob.com', 'google': 'google.com'})
x = 8
a3 = eval('x*3')


# 3、等价比较
class A:
    pass


class B(A):
    pass


inheritA = isinstance(B(), A)
inheritB = isinstance('hello', str)
inheritC = issubclass(B, A)
allSame1 = type(A()) == A
allSame2 = type(B()) == A

b1 = type('runoob')
b2 = type([75, 293])

# 4、数学
a4 = math.pow(100, 2)
a5 = sum([1, 3, 5], 6)
test1 = bool(3)


class FooParent(object):
    def __init__(self):
        self.parent = 'I\'m the parent'
        print('Parent')

    def bar(self, message):
        print('%s from Parent' % message)


class FooChild(FooParent):
    def __init__(self):
        super(FooChild, self).__init__()
        print('Child')

    def bar(self, message):
        self.parent = 'I\'m the Child'
        super(FooChild, self).bar(message)
        print('Child bar Function')
        print(self.parent)


if __name__ == '__main__':
    fooChild = FooChild()
    fooChild.bar('我是邱少依')

a6 = bin(10)

# 5、文件
file1 = open('qsy.txt', 'w')
file1.write('我就是看看,你不用说话')

# 6、迭代
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in lst:
    print('测测不用迭代器：', i)

for i in iter(lst):
    print('用迭代器：', i)


class C(object):
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    # 添加了改行，才会执行setter和getter方法
    x = property(getx, setx, 'I\'m the \'x\' property')


c1 = C()
c1.x = 13


def is_qysSqr(x):
    return math.sqrt(x) % 1 == 0


newList1 = filter(is_qysSqr, range(1, 101))

a7 = len('wojiushiet880895')
a8 = range(10)
a9 = range(1, 10)

b3 = bytearray([13, 85, 39, 10, 105])
float(345)

b4 = list((234, 'shagj', 34))
b5 = callable(b4)

# 7、格式化print
print('网站名:{name},地址：{url}'.format(name='你是菜鸟', url='www.runoob.com'))

site = {'name': '菜鸟教程', 'url': 'www.runoob.com', 'author': '邱少依'}
print('网站名:{name},地址：{url}, 作者:{author}'.format(**site))

my_list = ['菜鸟教程', 'www.runoob.com']
print('网站名:{0[0]},地址：{0[1]}'.format(my_list))


# 8、全局变量：打印当前函数或文件内的全部局部变量
def runoob(arg):
    z = 1
    print(locals(), globals())


runoob(4)


def add(x, y):
    return x + y


b6 = chr(0x30)
b7 = frozenset(range(10))

# 9、编码和变量
b8 = sys.getdefaultencoding()
b9 = vars()


def squre(x):
    return x ** 2


b10 = map(squre, [1, 2, 45, 87])

b11 = max(-20, 100, 400)

aList = [123, 'xyz', 'zara', 'abc', 'xyz'];
aList.reverse()

a = [1, 3, 5]
b = [4, 75, 93]
c = [45, 893, 202]
zipped1 = zip(a, b)
zipped2 = zip(a, c)
zipped3 = zip(a, b, c)

# 10、编译执行
str333 = '3*4 + 5'
c2 = compile(str333, '', 'eval')


# 11、属性判断
class Coordinate:
    x = 10
    y = -5
    z = 0


point1 = Coordinate()
delattr(Coordinate, 'x')
c4 = round(23.75785, 3)
c5 = hash('test')
c6 = set('runoobbyyuu')
dict()
arrs = range(10)
arrs[slice(5)]
c7 = id(point1)
c8 = [5, 76, 9, 23, 10]
c9 = sorted(c8)

# 12、排序：元祖中第0个数据升序(False)、降序（True）
c10 = [('b', 3), ('a', 20), ('c', 9), ('d', 30)]
c10 = sorted(c10, key=lambda x: x[0], reverse=True)


# 13、创建类: 类变量（empCount 和 empTest）、实例变量（方法中的变量：name、salary）、方法（如下面def的动态方法和@staticmethod的静态方法）
class Employee:
    empCount = 0
    empTest = 'justTest'

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print('Total Employee:{num}'.format(num=Employee.empCount))

    def displayEmployee(self):
        print('Name:{name},Salary:{salary}'.format(name=self.name, salary=self.salary))

    @staticmethod
    def staticFunction():
        print('类Employee里面有个定义名为f的静态函数')


emp2 = Employee('张三', 133)
emp2.displayCount()
emp2.displayEmployee()
# 14、添加新的属性
emp2.age = 13
emp2.age = 5
Employee.staticFunction()
emp2.staticFunction()
print('测试实例变量属性走一波', hasattr(emp2, 'age'), getattr(emp2, 'age'), setattr(emp2, 'age', 89), getattr(emp2, 'age'),
      delattr(emp2, 'age'))
print('测试内置类属性走一波', Employee.__doc__, Employee.__name__, Employee.__module__, Employee.__bases__, Employee.__dict__)

# 15、对象销毁：垃圾回收和循环垃圾收集器（补充用于清除所有未被引用的循环）
a = 40  # 创建对象  <40>
b = a  # 增加引用， <40> 的计数
c = [b]  # 增加引用.  <40> 的计数

del a  # 减少引用 <40> 的计数
b = 100  # 减少引用 <40> 的计数
c[0] = -1  # 减少引用 <40> 的计数


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, '销毁')


pt1 = Point()
pt2 = pt1
pt3 = pt1

print('测一测该Point的示例对象是否是同一个', id(pt1), id(pt2), id(pt3))
del pt1, pt2, pt3


# 16、类的继承
class Parent:
    parentAttr = 100

    def __init__(self):
        print('调用父类构造函数')

    def parentMethod(self):
        print('调用父类方法')

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print('父类属性:', Parent.parentAttr)

    def myMethod(self):
        print('父类方法')


class Child(Parent):
    def __init__(self):
        print('调用子类构造函数')

    def childMethod(self):
        print('调用子类方法')

    def myMethod(self):
        print('重写父类方法，仅调用子类')


c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()


# 17、基础重载方法 和 运算符重载
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __del__(self):
        print('删除当前的实例变量')

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 5)
v2 = Vector(5, -2)
print('我就是测测而已:{name}'.format(name=v1 + v2))


# 18、__双下划线表示私有的，不能用实例变量在方法外调用，但可以在方法内调用
class JustCounter:
    __secretCount = 0
    publicCount = 0

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print('测试私有属性: ', self.__secretCount)


counter = JustCounter()
counter.count()
counter.count()
print('测试走一波哈哈哈：', counter.publicCount)  # 无法执行counter.__secretCount

# 19、正则表达式
print('我就是测测匹配re.match:', re.match('com', 'www.runloob.com'), re.match('www', 'www.runloob.com').span())

line = 'Cats are smarter than dogs'
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)
if matchObj:
    print('matchObj.group() :', matchObj.group(), matchObj.group(1), matchObj.group(2))
else:
    print('No match!')

matchObjct = re.match(r'dogs', line, re.M | re.I)
searchObjct = re.search(r'dogs', line, re.M | re.I)
if matchObjct:
    print(matchObjct.group())
else:
    print('No Match!')

if searchObjct:
    print(searchObjct.group())
else:
    print('No Search!')

phone = '2004-959-559'

numPhone = re.sub(r'#.*$', '9', phone)
numPhoneAllNum = re.sub(r'\D', '', phone)
print('电话号码是：', numPhone, numPhoneAllNum)


def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)


s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))

#  r'(.*) are (.*?) .*' 解析：
# 这是一个字符串，前面的一个 r 表示字符串为非转义的原始字符串，让编译器忽略反斜杠，也就是忽略转义字符。但是这个字符串里没有反斜杠，所以这个 r 可有可无。
# (.*) 第一个匹配分组，.* 代表匹配除换行符之外的所有字符。
# (.*?) 第二个匹配分组，.*? 后面多个问号，代表非贪婪模式，也就是说只匹配符合条件的最少字符
# 后面的一个 .* 没有括号包围，所以不是分组，匹配效果和第一个一样，但是不计入匹配结果中。
# matchObj.group() 等同于 matchObj.group(0)，表示匹配到的完整文本字符
# matchObj.group(1) 得到第一组匹配结果，也就是(.*)匹配到的
# matchObj.group(2) 得到第二组匹配结果，也就是(.*?)匹配到的, 因为只有匹配结果中只有两组，所以如果填 3 时会报错。


# 20、CGI编程：一段程序,运行在服务器上
print('Content-type:text/html')
print  # 空行，告诉服务器结束头部
print('<html>')
print('<head>')
print('<meta charset="utf-8">')
print('<title> Hello World -- 我的第一个CGI程序</title>')
print('</head>')
print('<body>')
print('<h2>Hello Word! 我是来自菜鸟教程的第一CGI程序</h2>')
print('</body>')
print('</html>')

# 保存上述代码为 hello.py，修改文件权限为 755：chmod 755 hello.py


# 21、数据库

# # 打开数据库连接
# db = MySQLdb.connect('localhost','testuser','test123','TESTDB')
# # 使用cursor()方法获取操作游标
# cursor = db.cursor()
# # 创建数据表SQL语句
# existTabSql = 'DROP TABLE IF EXISTS EMPLOYEE'
# # 如果数据表已经存在使用 execute() 方法删除表
# cursor.execute(existTabSql)
# # 使用 fetchone() 方法获取一条数据库
# data = cursor.fetchone()
# # 创建数据表SQL语句
# sql = '"CREATE TABLE EMPLOYEE(FIRST_NAME  CHAR(20) NOT NULL,LAST_NAME  CHAR(20),AGE INT,  SEX CHAR(1),INCOME FLOAT)"'
# cursor.execute(sql)
#
# # SQL 插入语句
# insertSql = """INSERT INTO EMPLOYEE(FIRST_NAME,
#          LAST_NAME, AGE, SEX, INCOME)
#          VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
#
# try:
#     cursor.execute(insertSql)
#     db.commit() # 提交到数据库执行
# except:
#     db.rollback()# 执行回滚
#
# # SQL 更新语句
# updateSql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
# try:
#     cursor.execute(updateSql)
#     db.commit()
# except:
#     db.rollback()  # 发生错误时回滚
#
# # SQL 查询语句
# checkSql = "SELECT * FROM EMPLOYEE \
#        WHERE INCOME > '%d'" % (1000)"
# try:
#     cursor.execute(checkSql)
#     results = cursor.fetchall()
#     for row in results:
#         fname = row[0]
#         lname = row[1]
#         age = row[2]
#         sex = row[3]
#         income = row[4]
#         # 打印结果
#         print
#         ("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
#         (fname, lname, age, sex, income))
# except:
#     print('Error: unable to fecth data')
#
# # SQL 删除语句
# delSql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)"
# try:
#     cursor.execute(delSql)
#     db.commit()
# except:
#     db.rollback()
#
# # 关闭数据库连接
# db.close()

# 22、Python 网络编程 暂未

# s = socket.socket()# 创建 socket 对象
# host = socket.gethostname() # 获取本地主机名
# port = 80                # 设置端口
# s.bind((host, port))        # 绑定端口
# s.listen(5) # 等待客户端连接
# while True:
#     c, addr = s.accept() # 建立客户端连接
#     print('链接地址：',addr)
#     c.send('欢迎访问菜鸟教程')
#     c.close() # 关闭连接


# 23、邮件收发
# sender = 'from@runoob.com'
# receivers = ['1129331905@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
#
# # 创建一个带附件的实例
# message = MIMEMultipart()
# message['From'] = Header("菜鸟教程", 'utf-8')
# message['To'] = Header("测试", 'utf-8')
# subject = 'Python SMTP 邮件测试'
# message['Subject'] = Header(subject, 'utf-8')
#
# # 邮件正文内容
# message.attach(MIMEText('这是菜鸟教程Python 邮件发送测试……', 'plain', 'utf-8'))
# # 构造附件1，传送当前目录下的 test.txt 文件
# att1 = MIMEText(open('test.txt', 'rb').read(), 'base64', 'utf-8')
# att1["Content-Type"] = 'application/octet-stream'
# # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
# att1["Content-Disposition"] = 'attachment; filename="test.txt"'
# message.attach(att1)
#
# # 构造附件2，传送当前目录下的 runoob.txt 文件
# att2 = MIMEText(open('runoob.txt', 'rb').read(), 'base64', 'utf-8')
# att2["Content-Type"] = 'application/octet-stream'
# att2["Content-Disposition"] = 'attachment; filename="runoob.txt"'
# message.attach(att2)
#
# try:
#     smtpObj = smtplib.SMTP('localhost')
#     smtpObj.sendmail(sender, receivers, message.as_string())
#     print("邮件发送成功")
# except smtplib.SMTPException:
#     print("Error: 无法发送邮件")


# 24、为线程定义一个函数


# ===================线程同步执行===================
exitFlag1 = 0
threadLock = threading.Lock()  # 创建线程锁和线程数组
threads = []


class myThread(threading.Thread):  # 继承父类threading.Thread

    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name)
        # 获得锁，成功获得锁定后返回True
        threadLock.acquire()
        print_time(self.name, self.counter, 5)
        # 释放锁
        threadLock.release()
        print("Exiting " + self.name)


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag1:
            threading.Thread.exit()
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for t in threads:
    t.join()
print("Exiting Main Thread")

# ===================线程优先级队列（ Queue）===================
exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    def run(self):
        print("Starting " + self.name)
        process_data(self.name, self.q)
        print("Exiting " + self.name)


def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print("%s processing %s" % (threadName, data))
        else:
            queueLock.release()
        time.sleep(1)


threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

# 创建新线程
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# 填充队列
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()
print("Exiting Main Thread")

# 25、解析XML实例
# class MovieHandler(xml.sax.ContentHandler):
#     def __init__(self):
#         self.CurrentData = ""
#         self.type = ""
#         self.format = ""
#         self.year = ""
#         self.rating = ""
#         self.stars = ""
#         self.description = ""
#
#     def startElement(self, tag, attrs):
#         self.CurrentData = tag
#         if tag == "movie":
#             print('*****Movie*****')
#             title = attrs['title']
#             print('Title:',title)
#             # 元素结束事件处理
#
#
# def endElement(self, tag):
#     if self.CurrentData == "type":
#         print("Type:", self.type)
#     elif self.CurrentData == "format":
#         print("Format:", self.format)
#     elif self.CurrentData == "year":
#         print("Year:", self.year)
#     elif self.CurrentData == "rating":
#         print("Rating:", self.rating)
#     elif self.CurrentData == "stars":
#         print("Stars:", self.stars)
#     elif self.CurrentData == "description":
#         print("Description:", self.description)
#     self.CurrentData = ""
#
#     # 内容事件处理
# def characters(self, content):
#     if self.CurrentData == "type":
#         self.type = content
#     elif self.CurrentData == "format":
#         self.format = content
#     elif self.CurrentData == "year":
#         self.year = content
#     elif self.CurrentData == "rating":
#         self.rating = content
#     elif self.CurrentData == "stars":
#         self.stars = content
#     elif self.CurrentData == "description":
#         self.description = content
#
#
# if (__name__ == "__main__"):
#     # 创建一个 XMLReader
#     parser = xml.sax.make_parser()
#     # turn off namepsaces
#     parser.setFeature(xml.sax.handler.feature_namespaces, 0)
#
#     # 重写 ContextHandler
#     Handler = MovieHandler()
#     parser.setContentHandler(Handler)
#     parser.parse("movies.xml")

# 26、Python GUI编程: tkinter
# 创建一个GUI程序
# 1、导入 tkinter 模块
# 2、创建控件
# 3、指定这个控件的 master， 即这个控件属于哪一个
# 4、告诉 GM(geometry manager) 有一个控件产生了。
rootTkinter = tkinter.Tk()
li = ['C', 'python', 'php', 'html', 'SQL', 'java']
movie = ['CSS', 'jQuery', 'Bootstrap']

# listb = list(rootTkinter)
# listb2 = list(rootTkinter)
#
# for item in li:
#     listb.insert(0,item)
#
# for item in movie:
#     listb2.insert(0,item)
#
# listb.pack()
# listb2.pack()

rootTkinter.mainloop()

# 27、json

data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
jsonStr = json.dumps(data)
jsonData = json.loads(jsonStr)
print('测一测jsonString和jsonData', jsonStr, jsonData)

print(value, tuple, inputStr, t1, t2, \
      convertValue, a1, a2, a3, \
      inheritA, inheritB, \
      inheritC, allSame1, allSame2, \
      a4, a5, a6, c1.x, test1, newList1, \
      a7, a8, a9, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, \
      aList, zipped1, zipped2, zipped3, \
      eval(c2), hasattr(point1, 'x'), hasattr(point1, 'b'), c4, c5, c6, getattr(point1, 'y'),
      setattr(point1, 'y', '100'), arrs, c7, c8, c9, c10, \
 \
      )
