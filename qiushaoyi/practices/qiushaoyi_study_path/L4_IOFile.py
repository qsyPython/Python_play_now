'''
磁盘上读写文件的功能都是由操作系统提供的,
现代操作系统不允许普通的程序直接操作磁盘,
读写文件就是请求操作系统打开一个文件对象,
通过操作系统提供的接口从这个文件对象中读取数据
1、文件读写 2、内存中读写
'''
from io import StringIO
from io import BytesIO
import os  # 系统和环境变量、文件目录操作
import pickle  # 序列化
import json


'''
==========================practice 1: 文件读写 ==========================
  文本文件 'r'; 二进制（视频、图片）文件 'rb'
'''
try:
    f1 = open('test.png', 'rb', )  # ,encoding = 'gbk',errors = 'ignore'
    print('读取到文件中的内容:%s' % f1.read())
finally:
    if f1:
        f1.close()

# 上述方法的简化方法: 常用
with open('test.png', 'rb') as f1:
    for line in f1.readlines():
        print(line.strip())
    print(f1.read())

# 写方法
with open('test.png', 'w', encoding='gbk') as f1:
    f1.write('邱少一这么写就废了')

'''
==========================practice 2: 内存读写 ==========================
  StringIO(只能是str) 和 BytesIO(二进制数据)
'''

f2 = StringIO()
f2.write('邱少依 hello')
f2.write(' ')
f2.write('world')
str2 = f2.getvalue()
print(str2)

f3 = StringIO('Hello!\n Hi!\n Goodbye!')
while True:
    s = f3.readline()
    if s == '':
        break
    print(s.strip())

f4 = BytesIO()
f4.write('中文'.encode('utf-8'))  # 写入的不是str，而是经过UTF-8编码的bytes
print(f4.getvalue())

f5 = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f5.read())

'''
==========================practice 3: 系统变量、操作文件和目录 ==========================
'''
print(os.name, os.uname(), os.environ, os.environ.get('PATH'),
      os.environ.get('x', 'default'))  # 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。获取详细的系统信息，可以调用uname()函数。

# print('查看当前文件目录的绝对路径:',os.path.abspath('.'),\
# 	'在某个目录下创建一个新目录，1、首先把新目录的完整路径拼接出来',os.path.join('/Users/qiushaoyi/Desktop/Python_Pro/qiushaoyi_study_path','testDir'),\
# 	'2、创建一个目录,记得判断是否存在',os.mkdir('/Users/qiushaoyi/Desktop/Python_Pro/qiushaoyi_study_path/testDir'),\
# 	'删除一个目录',os.rmdir('/Users/qiushaoyi/Desktop/Python_Pro/qiushaoyi_study_path/testDir'),\
# 	'路径拆分处理',os.path.split('/Users/qiushaoyi/Desktop/Python_Pro/qiushaoyi_study_path/TestAgain'))
# # print('修改某文件的名称',os.rename('/Users/qiushaoyi/Desktop/Python_Pro/qiushaoyi_study_path/hello.py','/Users/qiushaoyi/Desktop/Python_Pro/qiushaoyi_study_path/QsyHello.py'),\
# 	'移除某文件',os.remove('/Users/qiushaoyi/Desktop/Python_Pro/qiushaoyi_study_path/hello的副本.py'))

# 列出当前目录下的所有目录: [x for x in os.listdir('.') if os.path.isdir(x)]
# 列出所有的.py文件 
# [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']

'''
========================== practice 4: 序列化和反序列化 ==========================
序列化：变量从内存中变成可存储到磁盘或传输到别的机器上的过程。
反序列化：变量内容从序列化的对象重新读到内存
'''
d = dict(name='Bob', age=20, score=60)
pickle.dumps(d)  # 任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件

fd = open('dump.txt', 'wb')
pickle.dump(d, fd)  # 任意对象序列化成一个bytes，然后，就可以把这个bytes写入某个已知路径的文件
fd.close()
# 读取文件中的内容
fdo = open('dump.txt', 'rb')
od = pickle.load(fdo)
fdo.close()
print(od)

'''
只能用Pickle保存那些不重要的数据,可能不同版本的Python彼此都不兼容,而且只能用于python
不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML和JSON
更好的方法是序列化为JSON: 该字符串可以被所有计算机语言读取，相比XML更快速，直接在web页面读取！
'''
# JSON:可支持的对象为 {}、[]、string、int/float、true/false、null
pd = dict(name='woqu', age=20, score=80)
json_str = json.dumps(pd)
print(json_str)

json_str1 = '{"age":20,"score":80,"name":"woqu"}'
pd1 = json.loads(json_str1)
print(pd1)


class Student(object):
    """docstring for Student"""

    def __init__(self, name, age, score):
        super(Student, self).__init__()
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return 'Student object(%s,%s,%s)' % (self.name, self.age, self.score)


s = Student('Bob', 20, 100)
s_json_str = json.dumps(s, default=lambda obj: obj.__dict__)  # 把class模型转为dict形式,才能序列化为json
print(s_json_str)

s1 = json.loads(s_json_str, object_hook=lambda d: Student(d['name'], d['age'], d['score']))
print(s1)
