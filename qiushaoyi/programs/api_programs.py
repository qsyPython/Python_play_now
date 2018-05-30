import requests
from bs4 import BeautifulSoup
from http import cookies
import urllib
import http.cookiejar
# from ConnectionMysql.mySQL_con import con_mysql
import time
from pyquery import PyQuery as pq
from pip._vendor.requests import api
from pip._vendor.requests.api import get

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
    'Referer': 'url',
}

session = requests.Session()
session.headers.update(headers)
# username = '362330199811103775'
# password = '123456'
url = ''

def login(username, password, lt, _eventId='submit'):  # 模拟登入函数

    data = {  # 需要传去的数据
        '_eventId': _eventId,
        'lt': lt,
        'password': password,
        'submit': u'登录',
        'username': username,
    }
    html = session.post(url, data=data, headers=headers)


def get_lt(url):  # 解析登入界面_eventId
    html = session.get(url)
    # 获取 lt
    soup = BeautifulSoup(html.text, 'lxml', from_encoding="utf-8")
    lt = soup.find('input', type="hidden")['value']
    # print(soup.find_all('input'))
    return lt


# 连接登录方法
def con_login(username, password):
    lt = get_lt(url)
    login(username, password, lt)
    login_url = '网页地址'
    per_html = session.get(login_url)
    soup = BeautifulSoup(per_html.text, 'lxml', from_encoding="utf-8")
    sql = "INSERT INTO xue_xin_info VALUES((SELECT REPLACE(UUID(),'-','')),"
    for tag in soup.find_all('table', class_='mb-table'):
        print(tag)
        for tag1 in tag.find_all('td'):
            te = tag1.get_text();
            sql += "'" + te + "',"
        p = pq(tag)
        print(p.find('th').filter(lambda i, this: pq(this).text() == '证件号码：').parent().find(
            '.data-s2 ds2-yaxnunnrdt9n41ui-m8').text())
        # 拼接sql
    sql += "'')"
    print(sql)
    con_mysql(sql)