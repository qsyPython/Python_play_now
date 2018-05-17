import requests
from bs4 import BeautifulSoup
from operator import itemgetter, attrgetter
import traceback
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import operator


coding="GBK"
"""
url 是地址
param 是参数  类型字典
"""

def getURLHtml(url,param):
    res= requests.get(url,param)
    if res.status_code == 200:
        return  res.content.decode(coding)
    else:
        return None


"""
解析内容
element 文档流
tag     标签
param   接收的格式是字典  class、id、name
"""
def getElementByFindFirst(element,tag,param=None):
    if param == None:
        return  element.find(tag)
    else:
        return  element.find(tag,param)

def getElementByFind(element,tag,param=None):
    if param == None:
        return  element.findAll(tag)
    else:
        return  element.findAll(tag,param)

"""
解析属性
element 解析后的文档流
attName 属性名
"""
def getElementByAtt(element,attName):
    return element.get(attName)


def httpRequestTag(url):
    res= requests.get(url,None)
    try:
        soup = BeautifulSoup(res.text, 'html.parser')
    except:
        print("请求失败")
        return
    containers = getElementByFindFirst(soup, 'div', {'class': 'all'})
    unstyleds = getElementByFind(containers , 'ul' ,{'class':'unstyled'})
    # 遍历all
    i = 0
    shuzu =[]
    for element in unstyleds:
        childs = getElementByFind(element,'a')
        for child in childs:
            dic = {} 
            # 标签名称
            dic["title"] = child.text
            href = getElementByAtt(child, 'href')
            href =href[1:]
            dic["href"] =href
            childUrl = url + href
            # print("jiekouUrl:",childUrl)
            try:
                childRes = requests.get(childUrl,None)
                childSoup =BeautifulSoup(childRes.text,'html.parser')
            except:
                print("请求失败")
                return
            data = getElementByFindFirst(childSoup, 'div', {'class': 'data'})
            span11s = getElementByFind(data, 'div', {'class': 'span1'})
            for some in span11s:
                key = getElementByFindFirst(some,'div',{'class': 'caption'})
                if hasattr(key, 'text'):
                    key =key.text
                value = getElementByFindFirst(some,'div',{"class":"value"})
                if hasattr(value, "text"):
                    value=value.text
                if (key !=None) and (value != None):
                    key=key.strip()
                    key=key.replace('\n', '')
                    value=value.strip()
                    value=value.replace('\n', '')
                    dic[key]=value
            shuzu.append(dic)
    print("shuzu:",shuzu)
    print("个数",len(shuzu))
    #根据AQI排序
    # dataAll =  sorted(shuzu.items(), key=lambda item:item(2))
    dataAll = sorted(shuzu, key=operator.itemgetter('AQI'))
    # shuzu.sort(key=operator.itemgetter(’AQI‘), reverse = True)  # 默认为升序， reverse=True为降序
    dataAllCount = len(shuzu)

    if dataAllCount >= 30:
        dataAll=dataAll[:30]
        print("dataAllall:",dataAll)
    print("dataAll30:",dataAll)
    return dataAll


def drawRect(datalist):
    if len(datalist)>0:
        pass
    else:
        return

    shuList = []
    bottomList = []

    for contentDic in datalist:
        AQI = contentDic["AQI"]
        title = contentDic["href"]
        shuList.append(AQI)
        bottomList.append(title)
    width = 0.4
    ind = np.arange(len(shuList))
    fig = plt.figure(1)
    1ax = fig.add_subplot(111)
    ax.set_xticks(ind)
    ax.set_xticklabels(bottomList)
    rects=plt.bar(range(len(shuList)), shuList, color='rgby')

    plt.title("Air quality in the best 30 cities")
    plt.xlabel("city")
    plt.ylabel("AQI")
    plt.xticks(rotation=90)
    plt.show()





if __name__ == '__main__':
    url ="http://pm25.in/"
    list = httpRequestTag(url)
    drawRect(list)

