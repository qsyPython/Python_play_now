'''
	作者：柴志勇
'''

import requests
from bs4 import BeautifulSoup
import csv
import selenium
import selenium.webdriver
import urllib
import time
import re
import random
import sys
import datetime
import threading
from random import choice
from util.file_manager import fileManager

professional_url_path = 'util/professional.csv'
professional_more_doctor_urls_path = 'util/professional_more_doctor_urls.csv'
professional_more_doctors_info_path = 'util/professional_more_doctors_info.csv'
# page = urllib.request.Request(url, headers=headers)
# page_info = urllib.request.urlopen(page).read().decode('gbk')  # 打开Url,获取HttpResponse返回对象并读取其ResposneBody
# driver = selenium.webdriver.Firefox(executable_path= '/Users/chaizhiyong/Downloads/geckodriver')
# driver.get('http://www.haodf.com/')
# html_text = driver.page_source

#通过三方库requests获取源码
def get_html_text(url):
	uas = [
		"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:17.0; Baiduspider-ads) Gecko/17.0 Firefox/17.0",
		"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9b4) Gecko/2008030317 Firefox/3.0b4",
		"Mozilla/5.0 (Windows; U; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; BIDUBrowser 7.6)",
		"Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",
		"Mozilla/5.0 (Windows NT 6.3; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
		"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.99 Safari/537.36",
		"Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; LCJB; rv:11.0) like Gecko",
	]
	headers = {"User-Agent": choice(uas)}
	r = requests.get(url, headers=headers, timeout=30)
	return r.text

#获取科室Url
def get_html_professional_url(url):
	print(url)
	html_office = get_html_text(url)
	soup = BeautifulSoup(html_office, 'html.parser')
	orange_list = soup.find_all('a', attrs={'class': 'orange'})
	print(orange_list)
	if len(orange_list) >= 2:
		orange_doctor_html_url = orange_list[1].get('href')#[<a class="orange" href="http://haoping.haodf.com/keshi/3017000/faculty_all_all.htm">查看更多好评科室&gt;&gt;</a>, <a class="orange" href="http://haoping.haodf.com/keshi/3017000/daifu_all.htm">查看更多好评大夫&gt;&gt;</a>, <a class="orange" href="http://www.haodf.com/keshi/DE4r0PiRvNoMvhpEy5skO978KXNMDo/zixun.htm">查看小儿外科更多咨询&gt;&gt;</a>, <a class="orange" href="http://www.haodf.com/keshi/DE4r0PiRvNoMvhpEy5skO978KXNMDo/zaixian.htm" target="_blank">向更多在线好大夫咨询&gt;&gt;</a>, <a class="orange" href="http://www.haodf.com/keshi/DE4r0PiRvNoMvhpEy5skO978KXNMDo/wenzhang.htm">更多文章&gt;&gt;</a>]
		return orange_doctor_html_url
	else:
		return None
		#get_doctor_inf(orange_doctor_html_url)

#获取科室的全部医生
def get_doctor_inf(url):
	html_doctor_list = get_html_text(url)
	soup = BeautifulSoup(html_doctor_list, 'html.parser')
	good_doctor_hospital_list = soup.find_all('ul', attrs={'class': 'yy_jb_df'})  # 医生职称
	good_doctors_info = []
	for i,good_doctor_professional in enumerate(good_doctor_hospital_list):
		good_doctor_urls = good_doctor_professional.find_all('a', attrs={'class': 'blue pernet'})
		for j in range(len(good_doctor_urls)):
			if j == 0:
				if len(good_doctor_urls[0].get('href')) > 0:
					good_doctors_info.append([str(i),good_doctor_urls[0].get('href')])

	return good_doctors_info

#业务模块,读取最多医生
def professional_more_doctor_url(professional_out_href):
	if professional_out_href != None:
			sleep_m = random.randint(5, 10)
			time.sleep(sleep_m)
			html_professional_url = get_html_professional_url(professional_out_href)
			return html_professional_url


#业务模块,读取最多医生
def professional_more_doctor(professional_out_href_list):
	professional_in_href_list = [] #取出的更多医生
	professional_no_href_list = [] #没有取出更多医生的url，继续取，直到取出为止
	if professional_out_href_list != None:
		for i, professional_href in enumerate(professional_out_href_list):
			# 	# t = threading.Thread(target=get_html_professional_url,args=(origin_a_url,))
			# 	# t.start()
			# 	# t.join()
			professional_href_in_url =	professional_more_doctor_url(professional_href[1])
			if professional_href_in_url != None:
				professional_in_href_list.append([professional_href[0],professional_href[1],professional_href_in_url])
			else:
				professional_no_href_list.append(professional_href)

		print(professional_no_href_list)
		if len(professional_in_href_list) > 0:
			file_csv_manager = fileManager()
			status = file_csv_manager.write_file_list(professional_more_doctor_urls_path, professional_in_href_list, 'a')
			if status:
				print("读取更多医生完成")
			else:
				print("读取更多医生失败")

		if len(professional_no_href_list) > 0:
			sleep_m = random.randint(30, 80)
			time.sleep(sleep_m)
			professional_more_doctor(professional_no_href_list)


def main():

	# html_url = 'http://www.haodf.com/'
    # #获取科室列表
	# html_text = get_html_text(html_url)
	# soup = BeautifulSoup(html_text, 'html.parser')
	# origin_div_j_list = soup.find_all('div', {'class': 'menu_con J_content'})[1]
	# origin_div_list = origin_div_j_list.find_all('div')
	# origin_href_list = []
	# origin_href_list_dic = []
	# for origin_div_pro_list in origin_div_list:
	# 	origin_ul_professional_list = origin_div_pro_list.find_all('ul')
	# 	if len(origin_ul_professional_list) > 0:
	# 		origin_professional_list = origin_ul_professional_list[0]
	# 		print(origin_professional_list)
	# 		for link in origin_professional_list.find_all('a'):
	# 			origin_a_url = link.get('href')
	# 			content = [link.get_text(),origin_a_url]
	# 			origin_href_list.append(origin_a_url)
	# 			origin_href_list_dic.append(content)
	# #科室url写入csv文件中
	# file_csv_manager = fileManager()
	# file_csv_manager.write_file_list(professional_url_path, origin_href_list_dic)

	# 区csv中第二列的值，因为第二列是Url
	# file_csv_manager = fileManager()
	# professional_out_href_list = file_csv_manager.read_file_all_list(professional_url_path)
	# print(professional_out_href_list)
	# professional_more_doctor(professional_out_href_list)

	# file_csv_manager = fileManager()
	# professional_more_doctor_urls = file_csv_manager.read_file_column_list(professional_more_doctor_urls_path,2)
	# for professional_more_doctor_page_url in professional_more_doctor_urls:
	# 	professional_more_doctor_page_url = "http://haoping.haodf.com/keshi/7000000/daifu_all.htm"
	# 	html_doctor_list = get_html_text(professional_more_doctor_page_url)
	# 	soup = BeautifulSoup(html_doctor_list, 'html.parser')
	# 	good_doctor_p_num_list = soup.find_all('a', attrs={'rel': 'true', 'class': 'p_text'})
	# 	count = 2
	# 	if len(good_doctor_p_num_list) > 0:
	# 		page_text = good_doctor_p_num_list[0].get_text().replace(' ', '')
	# 		page_count = re.findall(re.compile(r'共(\d+)页'), page_text)
	# 		if len(page_count) > 0:
	# 			count = int(page_count[0]) + 1
    #
	# 	print(str(count))
	# 	professional_more_doctor_page_base_url = professional_more_doctor_page_url[:-4]
	# 	print(professional_more_doctor_page_base_url)
	# 	for i in range(1, count):
	# 		professional_more_doctor_page_num_url = professional_more_doctor_page_url
    #
	# 		if i > 1:
	# 			professional_more_doctor_page_num_url = professional_more_doctor_page_base_url + '_' + str(
	# 				i) + '.htm'
	# 		print(professional_more_doctor_page_num_url)
	# 		professional_more_doctor_page_info = get_doctor_inf(professional_more_doctor_page_num_url)
	# 		print(professional_more_doctor_page_info)
	# 		sleep_m = random.randint(2, 5)
	# 		time.sleep(sleep_m)
	# 		file_csv_manager = fileManager()
	# 		status = file_csv_manager.write_file_list(professional_more_doctors_info_path,
	# 												  professional_more_doctor_page_info, 'a')
	# 		if status:
	# 			print("医生写入完成")
	# 		else:
	# 			print("医生写入失败")

	file_csv_manager = fileManager()
	doctor_web_url_list = file_csv_manager.read_file_column_list(professional_more_doctors_info_path,1)
	doctor_web_url_list = list(set(doctor_web_url_list))
	doctor_web_url = doctor_web_url_list[0]
	print(doctor_web_url)
	doctor_web_url_text = get_html_text(doctor_web_url)
	soup = BeautifulSoup(doctor_web_url_text, 'html.parser')
	doctor_info = []
	#医生简介
	doctor_brief_name =	soup.find('h3', attrs={'class': 'doc_name f22 fl'})
	doctor_brief_hospital = soup.find('div', attrs={'class': 'fl pr'}).find_all('a')
	doctor_info.append(doctor_brief_name.get_text().replace('  ', ''))
	if len(doctor_brief_hospital) > 0:
		for doctor_brief_sub in doctor_brief_hospital:
			doctor_info.append(doctor_brief_sub.get_text())


	#医生个人网站
	good_doctor_web_statistics_dic = soup.find('ul', attrs={'class': 'space_statistics'})
	good_doctor_web_statistics_list = good_doctor_web_statistics_dic.find_all('li')
	for good_doctor_web_statistics in  good_doctor_web_statistics_list:
		doctor_info.append(good_doctor_web_statistics.get_text())
	print(doctor_info)

	# patient_consulting = soup.find('a', attrs={'class': 'show_all pt10'})
	# if patient_consulting == None:
     #
	# else:
	# 	patient_all_consulting = patient_consulting.get('href')
	# 	patient_all_consulting = doctor_web_url[:-1] + patient_all_consulting



if __name__ == '__main__':
	main()