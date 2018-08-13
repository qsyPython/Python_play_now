'''
	借助 bs4 find/find_all抓取 标签 爬取所有城市的aqi：可用
	并保存到csv中
'''
import requests
from bs4 import BeautifulSoup
import csv


def process_w_csv_file(filepath, file_list):
    with open(filepath, mode='w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for row_list in file_list:
            writer.writerow(row_list)


def get_html_text(url):
    r = requests.get(url, timeout=30)
    # print('获取状态code:',r.status_code)
    return r.text


def get_all_cities(html_url):
    html_text = get_html_text(html_url)
    soup = BeautifulSoup(html_text, 'lxml')
    origin_cities_list = soup.find_all('div', {'class': 'bottom'})[1]
    cities_list = origin_cities_list.find_all('a')

    citys = []
    for city_div in cities_list:
        city_name = city_div.text
        city_pinyin = city_div['href'][1:]
        citys.append((city_name, city_pinyin))
    # print('获取城市的所有信息：', citys)
    return citys


def get_city_air_info(contain_city_url):
    '''
        获取某个城市的空气情况
    '''
    city_html_text = get_html_text(contain_city_url)
    soup = BeautifulSoup(city_html_text, 'lxml')
    city_all_info = soup.find_all('div', {'class': 'span1'})
    city_air_list = []
    for i in range(len(city_all_info) - 1):
        div_content = city_all_info[i]
        caption = div_content.find('div', {'class': 'caption'}).text.strip()
        value = div_content.find('div', {'class': 'value'}).text.strip()
        city_air_list.append((caption, value))
    return city_air_list


def main():
    html_url = 'http://pm25.in'
    cities_list = get_all_cities(html_url)
    cities_csv_list = []
    for i, city_tuple in enumerate(cities_list):
        city_name = city_tuple[0]
        city_pinyin = city_tuple[1]
        city_html_url = html_url + '/' + city_pinyin
        city_air_info = get_city_air_info(city_html_url)

        aqi_list = []
        aqi_list.append(city_name)
        for row_tuple in city_air_info:
            aqi_list.append(row_tuple[1])

        cities_csv_list.append(aqi_list)
        if i % 10 == 0:
            print('已经写入了{}条数据,共计{}数据'.format(i, len(cities_list) + 1))

    header_list = ['City', 'AQI', 'PM2.5/1h', 'PM10/1h', 'CO/1h', 'NO2/1h', 'O3/1h', 'O3/8h', 'SO2/1h', ]
    cities_csv_list.insert(0, header_list)
    process_w_csv_file('_cities_aqi.csv', cities_csv_list)


if __name__ == '__main__':
    main()
