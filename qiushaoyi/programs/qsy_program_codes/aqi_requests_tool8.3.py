'''
	作者：邱少一
	功能：网络爬虫：=============标签 BeautifulSoup形式看待整个网页，通过xml节点读取到数据
	            ==============借助 bs4 find抓取 标签 爬取所有城市的aqi
	日期：2017/12/12
	版本：1.0
	学习：OOP、IPO 、DOM。
	# 若lxml 库未安装，使用pip3 install lxml(装了5次啊，心累)

'''
import requests
from bs4 import BeautifulSoup


def get_all_cities_info(html_url):
    '''
        获取所有城市名称和拼音
    '''
    cities_list = []
    html_text = get_html_text(html_url)
    soup = BeautifulSoup(html_text, 'lxml')
    origin_div_list = soup.find_all('div', {'class': 'bottom'})[1]
    city_link_div_list = origin_div_list.find_all('a')  # 所有含有超链接的城市标签
    for city_link in city_link_div_list:
        city_name = city_link.text  # 标签中内容
        city_pinyin = city_link['href'][1:]  # 标签的href属性
        cities_list.append((city_name, city_pinyin))
    return cities_list


def get_html_text(url):
    '''
        获取html文本
    '''
    r = requests.get(url, timeout=30)
    # print('验证码：'r.status_code)
    return r.text


def get_city_index_info(html_text):
    '''
        获取某城市的index_info 内容
    '''
    soup = BeautifulSoup(html_text, 'lxml')
    div_list = soup.find_all('div', {'class': 'span1'})
    # print('获取某城市标签：',div_list)
    city_list_info = []
    for i in range(len(div_list) - 1):
        div_content = div_list[i]
        content = div_content.find('div', {'class': 'caption'}).text.strip()
        value = div_content.find('div', {'class': 'value'}).text.strip()
        city_list_info.append((content, value))
    return city_list_info


def main():
    html_url = 'http://pm25.in/'
    cities_list = get_all_cities_info(html_url)
    for city in cities_list:
        city_name = city[0]
        city_pinyin = city[1]
        html_text = get_html_text(html_url + city_pinyin)
        city_aqi = get_city_index_info(html_text)
        print('获取{}的aqi为：{}'.format(city_name, city_aqi[0][1]))


if __name__ == '__main__':
    main()
