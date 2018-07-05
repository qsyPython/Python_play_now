import requests
from bs4 import BeautifulSoup
import re
from songxin.L3.csv_operation import CSVOperation
from songxin.L3.header_list import HeaderList
from songxin.L3.url_manager import UrlManager


class LookForMoreDoctorParser(object):

    def look_for_more_doctor_parser(self,url):
        print("=============开始解析更多医生链接=============")
        csv_operation = CSVOperation()
        target_header = HeaderList()
        request = requests.get(url, headers=target_header.header)
        request.encoding = request.apparent_encoding
        request.close()
        soup = BeautifulSoup(request.text, 'lxml')
        more_doctor_urls = soup.find_all('a', attrs={'href': re.compile('^http://haoping.haodf.com/keshi/'), 'class': 'orange'})
        # print(more_doctor_urls)
        for u in more_doctor_urls:
            if 'daifu_all' in u.get('href'):
                # print(u.get('href'))
                return u.get('href')


# more_doctor_parser = LookForMoreDoctorParser()
# more_doctor_parser.look_for_more_doctor_parser("http://www.haodf.com/keshi/1010000.htm")