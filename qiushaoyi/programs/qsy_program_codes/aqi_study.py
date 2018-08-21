import requests, csv
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib as plt


def get_html_text(url):
    '''
        获取html文本
    '''
    r = requests.get(url, timeout=30)
    # print('验证码：'r.status_code)
    return r.text


def process_cvs_w_file(filepath, file_list):
    '''
        把数据写成csv文件
    '''
    with open(filepath, mode='w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for line in file_list:
            writer.writerow(line)


def main():
    html_url = 'https://www.aqistudy.cn/historydata/daydata.php?city=北京&month=2018-05'
    aqi_list = []
    html_text = get_html_text(html_url)
    soup = BeautifulSoup(html_text, 'lxml')
    origin_div_list = soup.find_all('div', {'class': 'col-lg-9 col-md-8 col-sm-8 col-xs-12'})[0]
    origin_div_list_table = origin_div_list.find_all('table', {
        'class': 'table table-condensed table-bordered table-striped table-hover table-responsive'})
    print(origin_div_list_table)


if __name__ == '__main__':
    main()
