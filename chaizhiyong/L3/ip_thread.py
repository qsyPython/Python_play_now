import time
import requests
import threading
from bs4 import BeautifulSoup
from util.iptools import headers, dict2proxy

baseFormat = 'http://www.xicidaili.com/nt/%d'



class agentIPThread(threading.Thread):

    def __init__(self,args):
        threading.Thread.__init__(self,args=args)
        self.good_proxies = []

    def run(self):
        url = baseFormat % self._args[0]
        # 发起网络访问
        r = requests.get(url, headers=headers)
        r.encoding = r.apparent_encoding
        r.raise_for_status()
        soup = BeautifulSoup(r.text, 'lxml')
        # 第一个是显示最上方的信息的，需要丢掉
        items = soup.find_all('tr')[1:]
        ips = self.parse_items(items)
        threads = []
        for ip in ips:
            # 开启多线程
            t = threading.Thread(target=self.check_ip, args=[ip, self.good_proxies])
            t.start()
            time.sleep(0.1)
            threads.append(t)
        [t.join() for t in threads]  # 线程加入当前线程

    def get_result(self):
        return self.good_proxies

    # 解析器解析字典
    def parse_items(items):
        # 存放ip信息字典的列表
        ips = []
        for item in items:
            tds = item.find_all('td')
            # 从对应位置获取ip，端口，类型
            ip, port, _type = tds[1].text, int(tds[2].text), tds[5].text
            ips.append({'ip': ip, 'port': port, 'type': _type})
        return ips

    # 检查ip是否可用，可用的入队列
    def check_ip(ip, good_proxies):
        try:
            pro = dict2proxy(ip)
            url = 'https://www.ipip.net/'
            r = requests.get(url, headers=headers, proxies=pro, timeout=5)
            r.raise_for_status()
        except Exception as e:
            pass
        else:
            good_proxies.append(ip)

    @staticmethod
    def check_ip(ip):
        try:
            pro = dict2proxy(ip)
            url = 'https://www.ipip.net/'
            r = requests.get(url, headers=headers, proxies=pro, timeout=5)
            r.raise_for_status()
        except Exception as e:
            return False
        else:
            return True