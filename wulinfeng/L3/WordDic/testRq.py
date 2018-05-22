import requests # 导入requests 库
from bs4 import BeautifulSoup
from  AllCity import AllCityName
from  AQICity import AQICityClass
from  PyIOTools import PyIOToolClass
from AQModel import AQModel
from  SQLTools import SQliteAQIModel
#
sqlTools = SQliteAQIModel()
sqlTools.sqlConnect()
ll = sqlTools.getAllAQI()
#
if len(ll[0]) == 0 | len(ll[0]) < 300:
    url = 'http://pm25.in/'
    cityA = AllCityName()
    aqi = AQICityClass()
    allcitys = cityA.getCityName(url)
    print(len(allcitys))
    allCityAQIValue = []
    print(allcitys)
    for cityName in allcitys:
        aqiValue = aqi.cityAQI(url,cityName, cityA.headers())
        if aqiValue == 0:
            break
        aq = AQModel(cityName,aqiValue)
        sqlTools.insert_table_dict(aq)
        allCityAQIValue.append(aq)

    print('=======',len(allCityAQIValue))
else:
    print('-----',ll[0])
    print('+++++',ll[1])
    pp = PyIOToolClass()
    pp.drawChat(ll[1][0:50],ll[0][0:50])

# 不带参数
# r = requests.get('http://pm25.in/')
# resp = BeautifulSoup(r.text,'html.parser')
# # print(resp)
# all_li = []
# for tag in resp.find_all('div',class_='all'):
#     all_li = tag.findAll('li')
#
# name_city = []
# for li in all_li:
#     cityName =li.find('a').get('href')
#     name_city.append(cityName)

# print(name_city)
# print('-----',r.status_code)
# print(r.text)

#带参数
# r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
# print(r.url)
# print(r.encoding)

#requests的方便之处还在于，对于特定类型的响应，例如JSON，可以直接获取：
# r = requests.get(
#     'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
#
# print(r.json())

#需要传入HTTP Header时，我们传入一个dict作为headers参数：
# r = requests.get('https://www.douban.com/',
#                  headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
# print(r.text)

# 要发送POST请求，只需要把get()方法变成post()，然后传入data参数作为POST请求的数据：
# r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})
# print(r.text)


# requests默认使用application/x-www-form-urlencoded对POST数据编码。如果要传递JSON数据，可以直接传入json参数：
# url = 'https://accounts.douban.com/login'
# param = {'form_email': 'abc@example.com', 'form_password': '123456'}
# r = requests.post(url,json=param)
# print(r.text)