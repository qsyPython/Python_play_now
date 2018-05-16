import threading

import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


net_uri = 'http://pm25.in/'
r = requests.get(net_uri)
html = r.content
soup = BeautifulSoup(html, 'lxml')

a_list = []
text_list = []
div_list = soup.find_all('div', attrs={'class': 'bottom'})
for a_text in div_list:
    # 遍历所有的a  提取链接和城市名
    for a_uri in a_text.find_all('a'):
        a_list.append(net_uri + a_uri['href'])
        text_list.append(a_uri.get_text())


 # 挨个遍历所有城市的链接 解析
city_name = []
city_data = []
city_n = []
city_d = []
for city_uri in a_list:
    r2 = requests.get(city_uri)
    html2 = r2.content
    soup2 = BeautifulSoup(html2, 'lxml')
    city_data.append(soup2.find_all('div', attrs='value'))
    city_name.append(soup2.find_all('div', attrs='caption'))



city_name2 = []
city_data2 = []
for i in range(len(city_name)):
    if i<50:
        city_name2.append(city_name[i][0].get_text().strip())


for value in range(len(city_data)):
    if value < 50:
        if city_data[value][0].get_text().strip() != '其他城市':
            city_data2.append(city_data[value][0].get_text().strip())

print(city_data2)
print(city_name2)



# total_width, n = 0.8, 2
# width = total_width / n
# nums_list = [1.5,2.5,3,6]
# nums_list2 = [1,2,3,4]
# name_list = ['Monday','Tuesday','Friday','Sunday']
# plt.bar(range(len(nums_list)),width=width,color='r')
# for i in range(len(nums_list)):
#     nums_list[i]  = nums_list[i]+width
#
plt.bar(range(len(text_list[0:50])),city_data2,color='y',tick_label = text_list[0:50])
plt.show()


# name_list = ['Monday', 'Tuesday', 'Friday', 'Sunday']
# num_list = [1.5, 0.6, 7.8, 6]
# num_list1 = [1, 2, 3, 1]
# num_list2 = [2, 3, 5, 7]
# x = list(range(len(num_list)))
# total_width, n = 0.8, 2
# width = total_width / n


# plt.bar(x, num_list, width=width, label='boy', fc='y')
# for i in range(len(x)):
#     x[i] = x[i] + width
# plt.bar(x, num_list1, width=width, label='girl', tick_label=name_list, fc='r')
# for i in range(len(x)):
#     x[i] = x[i] + width
# plt.bar(x, num_list2, width=width, label='girls', tick_label=name_list, fc='g')
# plt.legend()
# plt.show()

