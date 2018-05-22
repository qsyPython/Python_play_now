import urllib3,lxml
import requests
from bs4 import BeautifulSoup
import html5lib
from  pypinyin import lazy_pinyin


r = requests.get("http://www.air-level.com/")
# print(r.text)
sourceData = r
soup = BeautifulSoup(sourceData.text,features="lxml")

findCitys = soup.find_all("div",attrs={"id":"citylist"})#获取城市名

cityNames = []


for Tag in findCitys:
    #获取多有城市名
    liList = Tag.find_all('div',{"class":"citynames"})
    for li in liList:
        city_sublist = li.find_all('a')
        for city_detail in city_sublist:
            if cityNames.__contains__(city_detail.text):
                # print("过滤重复:%s" %city_detail.text)
                pass
            else:
                cityNames.append(city_detail.text)

subdata_dic = {}

imagetitle = ''
def request_city_data(str):
    tempstr = ""
    for string in lazy_pinyin(str):
        tempstr =  tempstr + string
    requestSingle = requests.get("http://www.air-level.com/air/%s/" %tempstr)
    soup1 = BeautifulSoup(requestSingle.text, features="lxml")
    findTitle = soup1.find_all("li", attrs={"class": "active"})

    findtime = ""# 时间
    for string in soup1.find_all("span", {"class": "label label-info"}):
        if findtime.__len__() == 0 :
            findtime = string.text.strip()


    findSubtitle = soup1.find_all('table', attrs={'class': 'table text-center'})
    for title in findTitle:  # 标题
        if len(title.text.strip()) != 0:
            imagetitle = title.text.strip()


    subtitle_list = []
    subdata_list = []
    for subtitle in findSubtitle:  # 子标题
        temp_subtitle_list = subtitle.find_all("th")
        temp_subdata_list = subtitle.find_all("td")
        for th in temp_subtitle_list:
            subtitle_list.append(th.text.strip())
        for td in temp_subdata_list:
            subdata_list.append(td.text.strip())
    subdata_list = subtitle_list + subdata_list#组合list 存放在元组中

    temp_list = []
    for i in range(len(subdata_list)):
        if i%6 == 0:
            a = tuple(subdata_list[i:5+i])
            temp_list.append(a)
    sorted(temp_list,key=lambda a:a[1])#根据aqi排序
    subdata_dic[str] = temp_list


for i in range(1,10):
    request_city_data(cityNames[i-1])


# print(subdata_dic)

import csv

with open("numpy.csv","w") as  f:

    # f_csv_header = subdata_dic.keys()
    # f_csv = csv.DictWriter(f,f_csv_header)
    # f_csv.writeheader()
    f_csv = csv.writer(f)
    f_csv.writerows(subdata_dic.values())



with open("numpy.csv") as  f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        pass

#导入需要的模块
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.ticker as ticker
import pandas as pd


# data = pd.read_csv("numpy.csv",names =subdata_dic['北京'][0])

a = subdata_dic['北京']

def by_aqi(t):
    return int(t[1])

b = sorted(a[1:len(a)-1],key=by_aqi)#根据aqi排序

listAQI  = [];
listArea = [];
for element in b:
    listAQI.append(element[1])
    listArea.append(element[0])


data = pd.DataFrame(listAQI, columns=["AQI"], index=listArea)

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签


plt.title("%s" %a[0][0])
plt.bar(listArea[1:listArea.__len__()-1],listAQI[1:listAQI.__len__() - 1],width = 0.35,facecolor = 'lightskyblue',edgecolor = 'white')
plt.show()
