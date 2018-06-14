from songxin.L3.keshi_parser import KeShiParser
from songxin.L3.look_for_more_doctor_parser import LookForMoreDoctorParser
from songxin.L3.url_manager import UrlManager
from songxin.L3.all_doctor_parser import AllDoctorParser
import time
import random
class Main(object):

    if __name__ == '__main__':
        keshi_perser = KeShiParser()
        more_doctor_parser = LookForMoreDoctorParser()
        soup = keshi_perser.keshi_parser("http://www.haodf.com/")
        keshi_url_manager = UrlManager()
        more_doctor_url_manager = UrlManager()
        all_doctor_parser = AllDoctorParser()
        titles = soup.find_all('div', {'class': 'menu_con_bg ask-pad-bottom'})
        if len(titles) > 0:
            for title in titles:
                a = title.find_all('a')
                for x in a:
                    try:
                        if 'href' in x.attrs:
                            l = x.get('href')
                            if 'keshi' in l:
                                keshi_url_manager.add_new_url(l)
                    except Exception as e:
                        print(e)
        print(len(keshi_url_manager.new_urls))
        while keshi_url_manager.has_new_url():
            print("还剩下{}更多 大夫页面没有解析".format(len(keshi_url_manager.new_urls)))
            more_url = more_doctor_parser.look_for_more_doctor_parser(keshi_url_manager.get_new_url())
            print(more_url)
            more_doctor_url_manager.add_new_url(more_url)
            time.sleep(random.randint(3, 5))
        print(len(more_doctor_url_manager.new_urls))
        while more_doctor_url_manager.has_new_url():
            all_doctor_parser.parser_doctor_html(more_doctor_url_manager.get_new_url())
            time.sleep(random.randint(3, 5))