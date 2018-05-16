#requests
import requests

#get请求
# r = requests.get('https://api.github.com/events')
# print(r.status_code) #返回状态吗
# print(r.text) #返回内容
# print(r.encoding) #返回编码

#post请求
# r = requests.post('http://httpbin.org/post', params={'name':'lingdu'})
# print(r.url)#http://httpbin.org/post?name=lingdu

#解析json内容
# r = requests.get('https://api.github.com/events')
# print(r.json())

# 定制请求头
# url = 'https://api.github.com/some/endpoint'
# headers = {'user-agent': 'my-app/0.0.1'}
# r = requests.get(url, headers=headers)
# print(r.status_code) #404

#更加复杂的 POST 请求
#你想要发送一些编码为表单形式的数据——非常像一个 HTML 表单。要实现这个，
# 只需简单地传递一个字典给 data 参数。你的数据字典在发出请求时会自动编码为表单形式：

# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.post("http://httpbin.org/post", data=payload)
# print(r.text)
#{"args":{},"data":"","files":{},"form":{"key1":"value1","key2":"value2"},"headers":{"Accept":"*/*","Accept-Encoding":"gzip, deflate","Connection":"close","Content-Length":"23","Content-Type":"application/x-www-form-urlencoded","Host":"httpbin.org","User-Agent":"python-requests/2.18.4"},"json":null,"origin":"49.4.186.138","url":"http://httpbin.org/post"}
#你还可以为 data 参数传入一个元组列表。在表单中多个元素使用同一 key 的时候，这种方式尤其有效：
# payload = (('key1', 'value1'), ('key1', 'value2'))
# r = requests.post('http://httpbin.org/post', data=payload)
# print(r.text)
#{"args":{},"data":"","files":{},"form":{"key1":["value1","value2"]},"headers":{"Accept":"*/*","Accept-Encoding":"gzip, deflate","Connection":"close","Content-Length":"23","Content-Type":"application/x-www-form-urlencoded","Host":"httpbin.org","User-Agent":"python-requests/2.18.4"},"json":null,"origin":"49.4.186.138","url":"http://httpbin.org/post"}
#查看服务器响应头
# print(r.headers)
#{'Connection': 'keep-alive', 'Server': 'gunicorn/19.8.1', 'Date': 'Mon, 14 May 2018 08:15:07 GMT', 'Content-Type': 'application/json', 'Content-Length': '351', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true', 'Via': '1.1 vegur'}


# 如果某个响应中包含一些 cookie，你可以快速访问它们：
# url = 'http://example.com/some/cookie/setting/url'
# r = requests.get(url)
# print(r.cookies['example_cookie_name']) 这个不做演示  因为根本就是404

#自动重定向
# r = requests.get('http://github.com')
# print(r.url)
# r = requests.get('http://github.com', allow_redirects=False)禁止重定向
