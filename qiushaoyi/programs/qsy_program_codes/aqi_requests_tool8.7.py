'''
	作者：邱少一
	功能：网络爬虫：=============标签 BeautifulSoup形式看待整个网页，通过xml节点读取到数据
	            ==============借助 BeautifulSoup 抓取 标签 爬取所有城市的aqi
	            ==============写成 csv文件
	日期：2017/12/12
	版本：1.0
	学习：OOP、IPO 、DOM
	# 若lxml 库未安装，使用pip3 install lxml(装了5次啊，心累)

'''
import requests, csv
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def process_cvs_w_file(filepath, file_list):
    '''
        把数据写成csv文件
    '''
    with open(filepath, mode='w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for line in file_list:
            writer.writerow(line)


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
    data = {'name': 'Tom', 'age': 20}
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 ' \
                            '(Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 ' \
                            '(KHTML, like Gecko) Version/5.1 Safari/534.50'
    r = requests.get(url, timeout=30, headers=headers, params=data)
    print('验证码：%s,%s,%s,%s,%s,%s' % (r.status_code, r.url, r.headers, r.cookies, r.text, r.content))  # content以字节流形式打印
    return r.text


def get_city_index_info(html_text):
    '''
        获取某城市的index_info 内容
    '''
    soup = BeautifulSoup(html_text, 'lxml')
    current_update_time_data = soup.find('div', {'class': 'live_data_time'}).text.strip()
    current_update_time = current_update_time_data.split('：')[1]
    div_list = soup.find_all('div', {'class': 'span1'})  # 标签list
    city_list_info = []
    for i in range(len(div_list) - 1):
        div_content = div_list[i]
        content = div_content.find('div', {'class': 'caption'}).text.strip()
        value = div_content.find('div', {'class': 'value'}).text.strip()
        city_list_info.append((content, value))
    return (city_list_info, current_update_time)


def main():
    html_url = 'http://pm25.in/'
    cities_list = get_all_cities_info(html_url)
    china_city_aqi = []  # 存放cvs数据的list
    live_data_time = ''
    for i, city in enumerate(cities_list):
        city_name = city[0]
        city_pinyin = city[1]
        html_text = get_html_text(html_url + city_pinyin)
        city_air_data = get_city_index_info(html_text)
        # print('获取{}的aqi为：{}'.format(city_name, city_aqi))

        # 单个城市的9个天气指数数据,并存入china_city_aqi
        city_index_info = []
        city_index_info.append(city_name)
        live_data_time = city_air_data[1]
        for value in city_air_data[0]:
            city_index_info.append(value[1])
        if i % 10 == 0:
            print('已处理{}条数据，总共{}条数据'.format(i, len(cities_list) + 1))
        china_city_aqi.append(city_index_info)

    header_list = ['City', 'AQI', 'PM2.5/1h', 'PM10/1h', 'CO/1h', 'NO2/1h', 'O3/1h', 'O3/8h', 'SO2/1h']
    china_city_aqi.insert(0, header_list)

    print('获取中国所有城市的空气信息：{}'.format(china_city_aqi))
    process_cvs_w_file('china_qsy_aqi.csv', china_city_aqi)

    # 数据处理
    aqi_data = pd.read_csv('china_qsy_aqi.csv')
    print('基本信息汇总：', aqi_data)
    print('数据概览：', aqi_data.head())

    # 数据清洗只保留aqi大于0的数据 condition：aqi_data['AQI']>0
    clean_aqi_data = aqi_data[aqi_data['AQI'] > 0]
    # 基本统计
    print('AQI最大值：', clean_aqi_data['AQI'].max())
    print('AQI最小值：', clean_aqi_data['AQI'].min())
    print('AQI均值：', clean_aqi_data['AQI'].mean())

    # top 50
    top50_cities = clean_aqi_data.sort_values(by=['AQI']).head(50)
    top50_cities.plot(kind='bar', x='City', y='AQI', title='空气质量最好的50个城市' + '( 当前时间:{t} )'.format(t=live_data_time),
                      figsize=(20, 10))  # kind统计的类型（bar为柱状图),figsize图像尺寸
    plt.savefig('top50_aqi_bar.png')
    plt.show()


if __name__ == '__main__':
    main()
