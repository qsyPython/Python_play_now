'''
	作者：邱少一
	功能：网络爬虫：==========字符串 形式看待整个网页,通过index找到对应的位置(弃用)
	日期：2017/12/12
	版本：1.0
	学习：OOP、IPO 、DOM。

'''
import requests


def get_html_text(url):
    r = requests.get(url, timeout=30)
    print('获取返回状态:{}'.format(r.status_code))
    return r.text


def main():
    city_name = input('请输入城市拼音：')
    url = 'http://pm25.in/' + city_name
    url_text = get_html_text(url)

    # 粘贴时：从div开始 到 要取数据的前一位
    aqi_div = '''<div class="span12 data">
        <div class="span1">
          <div class="value">
            '''
    index = url_text.find(aqi_div)
    begin_index = index + len(aqi_div)  # 找到的起始位置
    end_index = begin_index + 2  # 找到的结束位置
    aqi_val = url_text[begin_index:end_index]
    print('空气质量为：{}'.format(aqi_val))


if __name__ == '__main__':
    main()
