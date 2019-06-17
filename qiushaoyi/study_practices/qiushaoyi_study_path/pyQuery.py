'''
       pyquery 的爬虫工具 基本使用
'''

'''
==========================practice 1:html字符串 处理==========================
'''

# from pyquery import PyQuery as pd
#
# html_str = '''
# <div>
#     <ul id= 'hehe'>
#          <li class="item-0">first item</li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#          <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a></li>
#      </ul>
# </div
# '''
# doc = pd(html_str)
# print(doc, '\n', type(doc), '\n', doc('li'),
#       '\n', doc('#hehe .item-0 a span')) 若是item0 active 则为.item0.active
# id等于hehe下面的class等于item-0下的a标签下的span标签（注意层级关系以 空格 隔开）


'''
==========================practice 2: html文件 处理==========================
'''

# from pyquery import PyQuery as pd
#
# doc = pd(filename='pyQuery_index.html')
# print(doc,'\n',type(doc),'\n',doc('head'))


'''
==========================practice 3: url 处理==========================
'''

# from pyquery import PyQuery as pd
# baidu_url = 'https://www.baidu.com'
# doc = pd(url=baidu_url)
# print(doc,'\n',type(doc))

'''
==========================practice 4: html_str、html文件和url内容中 标签处理 小结==========================
'''
from pyquery import PyQuery as pd

html_str = '''
<div class=‘content’>
    <ul id = 'haha'>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
         <li > sixth item </li>
     </ul>
</div>'''
doc = pd(html_str)
item = doc('div ul')

# 根据已查找到的标签，查找这个标签下的 子标签或者父标签
print(item,'\n',item.parent(),'\n',item.children(),'\n')

#'[class]'表示获取含有class属性的 所有标签
print(item.children('[class]'),'\n')

# 处理含空格的class : 用.代替空格; id的用#
item1 = doc('.item-0.active a')

# 获取标签的属性值用attr
print(item1,'\n',item1.attr('href','class'))

# 获取标签中的文本
item2 = doc('a').text().strip()
print(item2)


'''
==========================practice 5: Dom操作 ==========================
'''
# from pyquery import PyQuery as pd
#
# html = '''
# <div class=‘content’>
#     <ul id = 'haha'>
#          <li class="item-0">first item</li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#          <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a></li>
#     </ul>
# </div>'''
#
# doc = pd(html)
# li = doc('.item-0.active')
# print(li)
# #删除和增加某标签的class属性
# print(li.remove_class('active'))
# print(li.add_class('hahahahaha'))
# #增加id属性
# print(li.attr('id','id-test369'))
# #增加css和删除该css的style
# print(li.css('font-size','20px'))
# print(li.remove_attr('style'))
# print()


