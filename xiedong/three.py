# -*- coding: utf-8 -*-
# 模块3
# 常用内建模块（time、calendar、datetime、collections、base64、struct、hashlib、
# hmac、itertools、contextlib、urllib、XML、HTMLParser）

# Time 模块包含既有时间处理的，也有转换时间格式的：
# time.altzone
# time.sleep(secs)
# time.clock()
# time.time()
# time.tzset()等等

#datetime是Python处理日期和时间的标准库
# 获取当前时间 获取指定日期和时间 datetime转换为timestamp timestamp转换为datetime
# datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。
# 如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关
from datetime import datetime
now = datetime.now()
print(now)

dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
print(dt)#2015-04-19 12:20:00

# dt.timestamp() # 把datetime转换为timestamp
#datetime.fromtimestamp(t)
# datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
#now.strftime('%a, %b %d %H:%M')
# 一个datetime类型有一个时区属性tzinfo，但是默认为None，所以无法区分这个datetime到底是哪个时区，除非强行给datetime设置一个时区

# calendar模块，即日历模块，提供了对日期的一些操作方法，和生成日历的方法。
# calendar模块中提供了三大类：
# 一、calendar.Calendar(firstweekday=0)
# 该类提供了许多生成器，如星期的生成器，某月日历生成器
# 二、calendar.TextCalendar(firstweekday=0)
# 该类提供了按月、按年生成日历字符串的方法。
# 三、calendar.HTMLCalendar(firstweekday=0)
# 类似TextCalendar，不过生成的是HTML格式日历

#collections是Python内建的一个集合模块，提供了许多有用的集合类
#namedtuple是一个函数，它用来创建一个自定义的tuple对象
#deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
# defaultdict OrderedDict Counter
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')

#Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据。
# base64.b64encode(s, altchars=None)
# base64.b64decode(s, altchars=None, validate=False)
# base64.standard_b64encode(s)
# base64.standard_b64decode(s)
# base64.urlsafe_b64encode(s)
# base64.urlsafe_b64decode(s)

#Python提供了一个struct模块来解决bytes和其他二进制数据类型的转换

# Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等
# Python内置的hmac模块实现了标准的Hmac算法，它利用一个key对message计算“杂凑”后的hash，
# 使用hmac算法比标准hash算法更安全，因为针对相同的message，不同的key会产生不同的hash。

# Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数
# count()会创建一个无限的迭代器
# cycle() 会把传入的序列无限重复下去
# repeat()负责把一个元素无限重复下去

# urllib提供了一系列用于操作URL的功能。
# urllib提供的功能就是利用程序去执行各种HTTP请求。如果要模拟浏览器完成特定功能
# 需要把请求伪装成浏览器。伪装的方法是先监控浏览器发出的请求，再根据浏览器的请求头来伪装
# User-Agent头就是用来标识浏览器的
from urllib import request

with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))

# 操作XML有两种方法：DOM和SAX。DOM会把整个XML读入内存，解析为树，
# 因此占用内存大，解析慢，优点是可以任意遍历树的节点。
# SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。
# 正常情况下，优先考虑SAX，因为DOM实在太占内存
from xml.parsers.expat import ParserCreate

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

# Python提供了HTMLParser来非常方便地解析HTML
from html.parser import HTMLParser
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

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')