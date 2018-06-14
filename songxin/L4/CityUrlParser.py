import random

import requests
from bs4 import BeautifulSoup

from songxin.L4.WeatherInfo import WeatherInfo


class CityUrlParser(object):

    def __init__(self):
        self.user_agent = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        ]
        self.header = {'Upgrade-Insecure-Requests': '1',
                       'User-Agent': random.choice(self.user_agent),
                       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                       'Referer': 'http://www.xicidaili.com/nn/',
                       'Accept-Encoding': 'gzip, deflate, sdch',
                       'Accept-Language': 'zh-CN,zh;q=0.8',
                       }

    def city_url_parser(self,city_name,city_url):
        try:
            request = requests.get(city_url, headers=self.header)
            request.encoding = request.apparent_encoding
            request.close()
            soup = BeautifulSoup(request.text, 'lxml')
            p = soup.find_all('ul', attrs={"class":"days clearfix"})
            print("大小",len(p))
            weather_info_list = []
            strs = ""
            index = 0
            while index < len(p):
                weather_info = WeatherInfo()
                weather_info.set_city_name(city_name)
                if index == 0:
                    weather_info.set_date("今天")
                elif index == 1:
                    weather_info.set_date("明天")
                else:
                    weather_info.set_date("后天")
                weather_info.set_temperature(((p[index].find_all('li'))[2]).string.strip())
                weather_info.set_pm((p[index].find('strong')).string.strip())
                weather_info.set_wind((p[index].find('em')).string.strip() + (p[index].find('b')).string.strip())
                weather_info.set_weather_condition((p[index].find('img')).get('alt').strip())
                weather_info.set_pic_url((p[index].find('img')).get('src').strip())
                weather_info_list.append(weather_info)
                index += 1
                strs = strs + "位置：%s, 时间：%s, 温度：%s ,天气：%s, PM2.5：%s,%s"%(weather_info.get_city_name(),weather_info.get_date(),weather_info.get_temperature(),(weather_info.get_weather_condition()+weather_info.get_wind()),weather_info.get_pm(),weather_info.get_pic_url()) +"|"
            return strs[:-1]
        except Exception as e:
            print(e)

# city_url_parser = CityUrlParser()
# city_url_parser.city_url_parser("繁昌县,安徽省","https://tianqi.moji.com/weather/china/anhui/fanchang-county")