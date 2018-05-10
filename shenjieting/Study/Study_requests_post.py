

import requests
import json

#1、找到post的url 地址 和post数据
post_url = "http://fanyi.baidu.com/v2transapi"
post_data = {"from":'zh',
             "to":'en',
             "query":"人生",
             "transtype":"translang",
             "simple_means_flag":"3",
             "sign": "548627.834594",
             "token": "3f8f4c683a6359586642247aacba6ee0"
             }
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
#2、发送请求，获取响应

r = requests.post(post_url,headers=headers,data=post_data)
json_str=r.content.decode()
#3、提取数据，展示出来
dict_response = json.loads(json_str)

print(dict_response)


# print("翻译结果是:{}".format(result))