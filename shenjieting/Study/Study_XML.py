'''

操作XML有两种方法：DOM和SAX。DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。

正常情况下，优先考虑SAX，因为DOM实在太占内存。

在Python中使用SAX解析XML非常简洁，通常我们关心的事件是start_element，end_element和char_data，准备好这3个函数，然后就可以解析xml了。

举个例子，当SAX解析器读到一个节点时：
会产生3个事件：

start_element事件，在读取<a href="/">时；

char_data事件，在读取python时；

end_element事件，在读取</a>时。

'''
from xml.parsers.expat import ParserCreate
from urllib import request

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


# 需要注意的是读取一大段字符串时，CharacterDataHandler可能被多次调用，所以需要自己保存起来，在EndElementHandler里面再合并。
# 除了解析XML外，如何生成XML呢？99%的情况下需要生成的XML结构都是非常简单的，因此，最简单也是最有效的生成XML的方法是拼接字符串：
L = []
L.append(r'<?xml version="1.0"?>')
L.append(r'<root>')
# L.append(encode('some & data'))
L.append(r'</root>')
print(''.join(L))

# 如果要生成复杂的XML呢？建议你不要用XML，改成JSON。
# 解析XML时，注意找出自己感兴趣的节点，响应事件时，把节点数据保存起来。解析完毕后，就可以处理数据。


# 练习
# def parseXml(xml_str):
#     print(xml_str)
#     return {
#         'city': '?',
#         'forecast': [
#             {
#                 'date': '2017-11-17',
#                 'high': 43,
#                 'low' : 26
#             },
#             {
#                 'date': '2017-11-18',
#                 'high': 41,
#                 'low' : 20
#             },
#             {
#                 'date': '2017-11-19',
#                 'high': 43,
#                 'low' : 19
#             }
#         ]
#     }

# URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'
#
# with request.urlopen(URL, timeout=4) as f:
#     data = f.read()
#
# result = parseXml(data.decode('utf-8'))
# assert result['city'] == 'Beijing'