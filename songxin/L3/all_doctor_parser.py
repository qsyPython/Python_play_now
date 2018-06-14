import random
import re
import requests
from songxin.L3.proxys_list import ProxysList
from songxin.L3.url_manager import UrlManager
from songxin.L3.csv_operation import CSVOperation
from songxin.L3.header_list import HeaderList
from bs4 import BeautifulSoup
import time
import csv

class AllDoctorParser(object):

    def parser_doctor_html(self, url):
        print("=============开始解析医生列表=============")
        try:
            all_doctor_url_manager = UrlManager()
            csv_operation = CSVOperation()
            target_header = HeaderList()
            # proxys_list = ProxysList()
            request = requests.get(url, headers=target_header.header)
            request.encoding = request.apparent_encoding  # 设置编码 encoding 返回的是请求头编码  apparent_encoding 是从内容网页中分析出的响应内容编码方式
            request.close()
            soup = BeautifulSoup(request.text, 'lxml')
            # print(soup.text)
            page_num = soup.find_all('div', {'class': 'p_bar'})
            # print(page_num)
            for p in page_num:
                z = p.find('a', {'class': 'p_text'})
                total = re.sub("\D", "", str(z))
            titles = soup.find_all('a', attrs={'href':re.compile('^http')})
            current_doctors = set()
            for title in titles:
                try:
                     if 'http://www.haodf.com/doctor/' in title.get('href'):
                         if 'jingyan' not in title.get('href'):
                            all_doctor_url_manager.add_new_url(title.get('href'))
                            current_doctors.add(title.get('href'))
                            print(title.get('href'))
                except:
                    pass
                x = 1
            print("total====>",total)
            while x <= int(total):
                print("total====>", str(x))
                try:
                    x += 1
                    strs = url.split('.htm')
                    new_str = strs[0] + '_' + str(x) + '.htm'
                    print("解析网页地址：", new_str)
                    request = requests.get(new_str, headers=target_header.header)
                    request.encoding = request.apparent_encoding
                    request.close()
                    soup = BeautifulSoup(request.text, 'lxml')
                    if soup is None or request.text is None:
                        continue
                    titles = soup.find_all('a', attrs={'href': re.compile('^http')})
                    for title in titles:
                        if 'http://www.haodf.com/doctor/' in title.get('href'):
                            if 'jingyan' not in title.get('href'):
                                all_doctor_url_manager.add_new_url(title.get('href'))
                                current_doctors.add(title.get('href'))
                                print(title.get('href'))
                    current_all_doctor = [current_doctors]
                    csv_operation.process_cvs_w_file("all_doctor_csv",current_all_doctor)

                    print("医生链接set大小为：", len(all_doctor_url_manager.new_urls))
                    print("=======================睡醒了接着干,第{}回了=======================".format(x))
                    time.sleep(random.randint(3, 6))
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)

# all_doctor_parser = AllDoctorParser()
# all_doctor_parser.parser_doctor_html("http://haoping.haodf.com/keshi/7000000/daifu_all.htm")