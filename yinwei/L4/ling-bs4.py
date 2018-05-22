# from bs4 import BeautifulSoup
# import requests
# data = requests.get('https://www.zhihu.com/question/39004511/answer/381478282')
# soup = BeautifulSoup(data.text, 'lxml')
# print(soup)

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

#print(soup.prettify())
## <html>
#  <head>
#   <title>
#    The Dormouse's story
#   </title>
#  </head>
#  <body>
#   <p class="title">
#    <b>
#     The Dormouse's story
#    </b>
#   </p>
#   <p class="story">
#    Once upon a time there were three little sisters; and their names were
#    <a class="sister" href="http://example.com/elsie" id="link1">
#     Elsie
#    </a>
#    ,
#    <a class="sister" href="http://example.com/lacie" id="link2">
#     Lacie
#    </a>
#    and
#    <a class="sister" href="http://example.com/tillie" id="link2">
#     Tillie
#    </a>
#    ; and they lived at the bottom of a well.
#   </p>
#   <p class="story">
#    ...
#   </p>
#  </body>
# </html>

#print(soup.title)
#  <title>The Dormouse's story</title>

#soup.title.name
#  u'title'

#soup.title.string
#  u'The Dormouse's story'

#soup.title.parent.name
#  u'head'

#soup.p
#  <p class="title"><b>The Dormouse's story</b></p>

#soup.p['class']
# u'title'

#soup.a
#  <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
#soup.find_all('a')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

#soup.find(id="link3")
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

#从文档中找到所有<a>标签的链接:
# for link in soup.find_all('a'):
#     print(link.get('href'))

    # http://example.com/elsie
    # http://example.com/lacie
    # http://example.com/tillie

# 从文档中获取所有文字内容:

#print(soup.get_text())
# The Dormouse's story
#
# The Dormouse's story
#
# Once upon a time there were three little sisters; and their names were
# Elsie,
# Lacie and
# Tillie;
# and they lived at the bottom of a well.
#
# ...


# 安装解析器
# Beautiful Soup支持Python标准库中的HTML解析器,还支持一些第三方的解析器,其中一个是 lxml .根据操作系统不同,可以选择下列方法来安装lxml:
#
# $ apt-get install Python-lxml
#
# $ easy_install lxml
#
# $ pip install lxml

# 另一个可供选择的解析器是纯Python实现的 html5lib , html5lib的解析方式与浏览器相同,可以选择下列方法来安装html5lib:
#
# $ apt-get install Python-html5lib
#
# $ easy_install html5lib
#
# $ pip install html5lib

# Tag 对象与XML或HTML原生文档中的tag相同:
# soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
# tag = soup.b
# type(tag)
# <class 'bs4.element.Tag'>

# 每个tag都有自己的名字,通过 .name 来获取:

# tag.name
# u'b'

# 一个tag可能有很多个属性. tag <b class="boldest"> 有一个 “class” 的属性,值为 “boldest” . tag的属性的操作方法与字典相同:
# tag['class']
# u'boldest'

# 也可以直接”点”取属性, 比如: .attrs :

# tag.attrs
# {u'class': u'boldest'}

# tag的属性可以被添加,删除或修改. 再说一次, tag的属性操作方法与字典一样

# tag['class'] = 'verybold'
# tag['id'] = 1
# tag
# # <blockquote class="verybold" id="1">Extremely bold</blockquote>
#
# del tag['class']
# del tag['id']
# tag
# # <blockquote>Extremely bold</blockquote>
#
# tag['class']
# # KeyError: 'class'
# print(tag.get('class'))
# # None

# 多值属性
# css_soup = BeautifulSoup('<p class="body strikeout"></p>')
# css_soup.p['class']
# # ["body", "strikeout"]
#
# css_soup = BeautifulSoup('<p class="body"></p>')
# css_soup.p['class']
# ["body"]

#按CSS搜索
# soup.find_all("a", class_="sister")

# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

# CSS选择器

# soup.select("title")
# # [<title>The Dormouse's story</title>]
#
# soup.select("p:nth-of-type(3)")
# # [<p class="story">...</p>]


# soup.select("body a")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie"  id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]


# 等等等等详情请点击:
# http://beautifulsoup.readthedocs.io/zh_CN/latest/











