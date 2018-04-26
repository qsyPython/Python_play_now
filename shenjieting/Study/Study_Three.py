# （模块3：
# 常用内建模块（time、calendar、datetime、collections、base64、struct、hashlib、hmac、itertools、contextlib、urllib、XML、HTMLParser等）

# Python时间time详解
'''
1、datetime：Python处理日期和时间的标准库
引入方法： from datetime import datetime。
第一个datetime是模块，第二个datetime是类。 如果仅导入import datetime，则必须引用全名datetime.datetime。
获取当前日期和时间：datetime.now()
加减当前时间：now + timedelta(days=2, hours=12)
datetime->timestamp：
'''

from datetime import datetime
from collections import namedtuple
from collections import deque
from collections import OrderedDict
from collections import Counter
from xml.parsers.expat import ParserCreate
from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request
from urllib import parse
import hashlib
import struct
import itertools


dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
dt.timestamp() # 把timestamp转换为datetime1429417200.0
# Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。 某些编程语言（如Java和JavaScript）的timestamp使用整数表示毫秒数，这种情况下只需要把timestamp除以1000就得到Python的浮点表示方法。
# datetime->str
# datetime->UTC时间
# 时区转化
# 存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。

# 2、collections： Python内建的一个集合模块，提供了许多有用的集合类。
# namedtuple： 创建一个自定义的tuple对象

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)

# deque： 为了高效实现插入和删除操作的双向列表，适合用于队列和栈

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)
q.pop()
print(q)
q.popleft()
print(q)

# defaultdict： 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1']) # key1存在'abc'
print(dd['key2']) # key2不存在，返回默认值'N/A'

# OrderedDict： 保持Key的顺序，可以用OrderedDict(按插入序)。 OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key

d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d) # dict的Key是无序的
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od) # OrderedDict的Key是有序的

# Counter：Counter计数器，也是dict的子类，如统计字母出现的次数，类似于Wordcount

c=Counter
print(c('Programming'))

# 3、base64 : 用64个字符来表示任意二进制数据. Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据。
# 4、struct： 解决bytes和其他二进制数据类型的转换。
'''
Windows的位图文件（.bmp）是一种非常简单的文件格式，可以用struct分析出其文件头结构。
两个字节：'BM'表示Windows位图，'BA'表示OS/2位图；
一个4字节整数：表示位图大小；
一个4字节整数：保留位，始终为0；
一个4字节整数：实际图像的偏移量；
一个4字节整数：Header的字节数；
一个4字节整数：图像宽度；
一个4字节整数：图像高度；
一个2字节整数：始终为1；
一个2字节整数：颜色数。
通过分析位图文件的文件头结构，可以检查任意文件是否是位图文件
'''
s = '\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
print(struct.unpack('<ccIIIIIIHH', s))

# 5、hashlib：提供常见的摘要算法，MD5,SHA1,SHA256,SHA512等
# 摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。 目的是为了发现原始数据是否被人篡改过 。摘要算法之所以能指出数据是否被篡改过，就是因为摘要函数是一个单向函数，计算f(data)很容易，但通过digest反推data却非常困难。而且，对原始数据做一个bit的修改，都会导致计算出的摘要完全不同。也可以看成加密算法。


md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())
# 注意：在pycharm上测试运行时，新建的.py文件名称不要取hashlib，因为代码中需要import hashlib，如果文件名也是hashlib就会引入当前文件(模块)，从导致出现错误。
# 6、itertools: 提供用于操作迭代对象的函数
# count()会创建一个无限的迭代器，count(1)从1开始的迭代器
# for n in itertools.count(1):
#     print(n)
#     if n==10:
#         break
# cycle()会把传入的一个序列无限重复下去

# for c in itertools.cycle('abc'):
#     print(c)
#     i+=1
#     if i==10:
#         break
# repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数

for n in itertools.repeat('a',3):
    print(n)
# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：

for c in itertools.chain('ABC', 'XYZ'):
       print(c)    # 迭代效果：'A' 'B' 'C' 'X' 'Y' 'Z'

# groupby()把迭代器中相邻的重复元素挑出来放在一起：
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))

# 小结： itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，而是Iterator，只有用for循环迭代的时候才真正计算。
# 7、XML：Python解析XML
# （DOM和SAX）
# DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。正常情况下，优先考虑SAX，因为DOM实在太占内存。

# Python利用SAX解析XML（关心的事件：start_element，end_element和char_data）：


class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)

# 生成XML：拼接字符串、JSON
L = []   #list
L.append(r'<?xml version="1.0"?>')
L.append(r'<root>')
L.append(r'</root>')
print(''.join(L))#str
# 8、HTMLParser
# 编写一个搜索引擎：
# 用爬虫吧目标网站页面抓下来
# 解析该HTML页面


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name): #特殊字符
        print('&%s;' % name)

    def handle_charref(self, name): #特殊字符
        print('&#%s;' % name)

parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')

# 9、urllib: 提供一系列用于操作URL的功能
# Get（下载）
#模拟iPhone 6去请求豆瓣首页


req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25') #不添加该header时，表示对以上页面进行抓取（查看该页面打开时返回的值），添加了该header，表示 模拟iPhone 6去请求豆瓣首页
with request.urlopen(req) as f:  #用request方式打开URL，将返回值标记为f
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))

# Post（上传）： 如果要以POST发送一个请求，只需要把参数data以bytes形式传入。
#模拟微博登录


print('Login to weibo.cn...')
email = input('Email: ')
passwd = input('Password: ')
login_data = parse.urlencode([
    ('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8')) #en加de解
# Handler： 通过一个Proxy去访问网站，我们需要利用ProxyHandler来处理

