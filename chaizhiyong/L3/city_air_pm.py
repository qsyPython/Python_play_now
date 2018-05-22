import requests
import time
from bs4 import BeautifulSoup
import csv
from random import choice
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from util.file_manager import fileManager
from util.mysql_manager import mySQLManager
from util.iptools import headers, dict2proxy
from ip_thread import agentIPThread
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import operator
city_info_path = 'util/city_info.csv'
check_ip_url = 'https://www.ipip.net/'#检查IP是否可用

def draw_bar(labels,quants):

    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    matplotlib.rcParams['font.family'] = 'sans-serif'
    matplotlib.rcParams['axes.unicode_minus'] = False
    plt.xlabel("城市")
    plt.ylabel("AQI")
    plt.yticks(np.arange(0, 500, 5),fontsize=8)
    plt.bar(range(len(quants)),quants,tick_label = labels,color="#87CEFA")
    plt.xticks(range(len(quants)), rotation=90, fontsize=8)
    plt.tight_layout()
    plt.show()


class cityPm(object):
    #构造函数
    def __init__(self):
        self._proxyList = []
        self.installcof()

    #初始化函数，先读取
    def installcof(self):
        mysqlDB = mySQLManager()
        db_ips = mysqlDB.select_all()
        if db_ips != None and len(db_ips) > 0:
            self._proxyList = db_ips
        else:
            threads = []
            for i in range(1, 2):
                threadHandler = agentIPThread(args=[i])
                threadHandler.start()
                time.sleep(10)
                threads.append(threadHandler)
                [t.join() for t in threads]  # 线程加入当前线程
            mySQL = mySQLManager()
            for t in threads:
                proxies = t.get_result()
                for proxie in proxies:
                    mySQL.insert_ip_table(proxie)

            db_ips = mysqlDB.select_all()
            if db_ips != None and len(db_ips) > 0:
                self._proxyList = db_ips


    # 通过三方库requests获取源码
    def get_html_text(self,url):
        proxies = choice(self._proxyList)
        r = requests.get(url, headers=headers,proxies = proxies, timeout=30)
        return r.text


    def getIP(self):
        ip_info = choice(self._proxyList)
        return ip_info


    def getCitiesPm(self):

        city_list = []
        city_value_list = []
        file_csv_manager = fileManager()
        city_list = city_list + file_csv_manager.read_file_column_list(city_info_path,0)
        city_value_list = city_value_list + file_csv_manager.read_file_column_list(city_info_path,1)
        if len(city_list) <= 0 and len(city_list) <= 0:
            city_url = 'http://pm25.in/'
            city_html = self.get_html_text(city_url)
            soup = BeautifulSoup(city_html, 'html.parser')
            city_all = soup.find('div', attrs={'class': 'all'})
            city_all_info = city_all.find_all('ul', attrs={'class': 'unstyled'})


            for city in city_all_info:

                city_style_url = city.find_all('a', href=True)

                for city_section_url in city_style_url:
                    print(city_section_url)
                    city_list.append(city_section_url.get_text().strip())
                    city_info_html = self.get_html_text(city_url[:-1] + city_section_url.get('href'))

                    city_info_soup = BeautifulSoup(city_info_html, 'html.parser')
                    city_info_pan = city_info_soup.find_all('div', attrs={'class': 'span1'})

                    for city_info in city_info_pan:
                        city_caption = city_info.find('div', attrs={'class': 'caption'})
                        if city_caption is not None:
                            if city_caption.get_text().strip() == 'AQI':
                                city_value = city_info.find('div', attrs={'class': 'value'})
                                if city_value is not None and (int(city_value.get_text().strip()) > 0):
                                    city_value_list.append(city_value.get_text().strip())
                                break
                        else:
                            break
            file_csv_manager = fileManager()
            status = file_csv_manager.write_file_list(city_info_path,
                                                      list(zip(city_list, city_value_list)), 'w')
            if status:
                print("写入完成")
            else:
                print("写入失败")

        cities_info = list(zip(city_list[:50], city_value_list[:50]))
        cities_info = sorted(cities_info, key=lambda city:int(city[1]),reverse=False)
        print(cities_info)
        city_list_sort = []
        city_value_list_sort = []

        for citie_info in cities_info:
            city_list_sort.append(citie_info[0])
            city_value_list_sort.append(citie_info[1])

        print(cities_info)
        draw_bar(city_list_sort, city_value_list_sort)

def main():

    cityPmManager = cityPm()
    cityPmManager.getCitiesPm()


if __name__ == '__main__':
	main()