
import requests

r = requests.get("http://github.com/timeline.json")

l = requests.get("http://www.baidu.com")

e = requests.post("http://httpbin.org/post")

q = requests.put("http://httpbin.org/put")

u = requests.delete("http://httpbin.org/delete")

s = requests.head("http://httpbin.org/get")

t = requests.options("http://httpbin.org/get")

#查看两者   l会有乱码
print(r.text)
print(l.text)
#查看编码方式
print(r.encoding)
print(l.encoding)

#将l编码转为utf-8
l.encoding = 'utf-8' #指定l.text的编解码方式
print(l.encoding)
#l.content 是一个bytes类型的字符串(二进制类型) 没有任何更改的  推荐~
print(r.content.decode())
print(l.content.decode())


r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
print(r.json())