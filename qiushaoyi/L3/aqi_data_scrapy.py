'''
	作者：邱少一
	日期：2018/4/3
	功能：
	第三期作业：
        做一个简单的网络爬虫demo，爬取一下空气质量指数的网站(http://pm25.in/)的数据
        然后处理数据做成如下的图表（x坐标为城市名称，y坐标为对应城市的AQI，title为：空气质量最好的50个城市，对应的更新时间为网页的 数据更新时间）
'''
import requests,csv
from requests.exceptions import ReadTimeout,HTTPError,RequestException
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def process_cvs_w_file(filepath,file_list):
	'''
		把数据写成csv文件
	'''
	with open(filepath,mode='w',encoding='utf-8',newline='') as f:
		writer = csv.writer(f)
		for line in file_list:
			writer.writerow(line)


def get_all_cities_info(html_url):
	'''
		获取所有城市名称和拼音
	'''
	cities_list = []
	html_text= get_html_text(html_url)
	soup = BeautifulSoup(html_text,'lxml')
	origin_div_list = soup.find_all('div',{'class':'bottom'})[1]
	city_link_div_list = origin_div_list.find_all('a')
	for city_link in city_link_div_list:
		city_name = city_link.text
		city_pinyin = city_link['href'][1:]
		cities_list.append((city_name,city_pinyin))
	return  cities_list

def get_html_text(url):
	'''
		获取html文本
	'''
	try:
		r = requests.get(url, timeout=30)
		print(r.status_code)
		return r.text
	except ReadTimeout:
		print('timeout')
	except HTTPError:
		print('httperror')
	except RequestException:
		print('reqerror')


def get_city_index_info(html_text):
	'''
		获取某城市的index_info 内容
	'''
	soup = BeautifulSoup(html_text,'lxml')
	current_update_time_data = soup.find('div',{'class':'live_data_time'}).text.strip()
	current_update_time = current_update_time_data.split('：')[1]
	div_list = soup.find_all('div',{'class':'span1'})
	city_list_info = []
	for i in range(len(div_list)-1):
		div_content = div_list[i]
		content = div_content.find('div',{'class':'caption'}).text.strip()
		value = div_content.find('div',{'class':'value'}).text.strip()
		city_list_info.append((content,value))
	return (city_list_info,current_update_time)


def main():
	html_url = 'http://pm25.in/'
	cities_list = get_all_cities_info(html_url)
	china_city_aqi = [] #存放cvs数据的list
	live_data_time = ''
	for i,city in enumerate(cities_list):
		city_name = city[0]
		city_pinyin = city[1]
		html_text = get_html_text(html_url+city_pinyin)
		city_air_data = get_city_index_info(html_text)
		# print('获取{}的aqi为：{}'.format(city_name, city_aqi))

		city_index_info = []
		city_index_info.append(city_name)
		live_data_time = city_air_data[1]
		for value in city_air_data[0]:
			city_index_info.append(value[1])
		if i % 10 == 0:
			print('已处理{}条数据，总共{}条数据'.format(i, len(cities_list) + 1))
		china_city_aqi.append(city_index_info)

	header_list = ['City','AQI','PM2.5/1h','PM10/1h','CO/1h','NO2/1h','O3/1h','O3/8h','SO2/1h']
	china_city_aqi.insert(0,header_list)

	# print('获取中国所有城市的空气信息：{}'.format(china_city_aqi))
	process_cvs_w_file('china_qsy_aqi.csv',china_city_aqi)

	# 数据处理
	aqi_data = pd.read_csv('china_qsy_aqi.csv')
	print('基本信息汇总：',aqi_data.info())
	print('数据概览：', aqi_data.head())

	# 数据清洗只保留aqi大于0的数据 condition：aqi_data['AQI']>0
	clean_aqi_data = aqi_data[aqi_data['AQI'] > 0]
	# 基本统计
	# print('AQI最大值：', clean_aqi_data['AQI'].max())
	# print('AQI最小值：', clean_aqi_data['AQI'].min())
	# print('AQI均值：', clean_aqi_data['AQI'].mean())

	# top 50
	top50_cities = clean_aqi_data.sort_values(by=['AQI']).head(50)
	top50_cities.plot(kind='bar', x='City', y='AQI', title='空气质量最好的50个城市'+'( 当前时间:{t} )'.format(t=live_data_time),
					  figsize=(20, 10))
	plt.savefig('top50_aqi_bar.png')
	plt.show()


if __name__ == '__main__':
	main()