import random
from songxin.L4.MySQLCreate import MySQLCreate
import time
from bs4 import BeautifulSoup
import requests

class   ProvinceParser(object):

    def __init__(self):
        self.my_sql = MySQLCreate()
        # self.my_sql.create_form()
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
        self.base_url = 'https://tianqi.moji.com/weather/china/'
        self.province = ['安徽', '北京', '重庆', '福建', '甘肃', '广东',
                         '广西', '贵州', '海南', '河北', '河南', '湖北', '湖南', '黑龙江', '吉林', '江苏',
                         '江西', '辽宁', '内蒙古', '宁夏', '青海', '山东', '陕西', '山西', '上海', '四川',
                         '天津', '西藏', '新疆', '云南', '浙江']
        self.pinyin_province = ['anhui', 'beijing', 'chongqing', 'fujian', 'gansu', 'guangdong',
                         'guangxi', 'guizhou', 'hainan', 'hebei', 'henan', 'hubei', 'hunan', 'heilongjiang', 'jilin', 'jiangsu',
                         'jiangxi', 'liaoning', 'inner-mongolia', 'ningxia', 'qinghai', 'shandong', 'shanxi', 'shanxi', 'shanghai', 'sichuan',
                         'tianjin', 'tibet', 'xinjiang', 'yunnan', 'zhejiang']

    def province_parser(self):
        try:
            province_index = 0
            while province_index < len(self.pinyin_province):
                current_url = self.base_url + self.pinyin_province[province_index] + "/"
                print(current_url)
                request = requests.get(current_url, headers=self.header)
                request.encoding = request.apparent_encoding
                request.close()
                soup = BeautifulSoup(request.text, 'lxml')
                p = soup.find_all('a')
                index = 0
                strs = ""
                while index < len(p):
                    if current_url in p[index].get('href'):
                        current_href = p[index].get('href')
                        strs += p[index].string + ","
                        if "'" in p[index].get('href'):
                            current_href = current_href.replace("'","\\\'")
                            print("=========================")
                        print(current_href, p[index].string)
                        self.my_sql.city_insert_data(p[index].string, current_href)
                    index += 1
                strs = strs[:-1]
                self.my_sql.rangion_insert_data(self.province[province_index],strs)
                print(strs)
                province_index += 1
                time.sleep(random.randint(3, 6))
        except Exception as e:
            print(e)

# p = ProvinceParser()
# p.province_parser()