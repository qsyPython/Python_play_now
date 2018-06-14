# 第4期作业：
# 用python实现一个ui页面，如下图。页面中有一个输入框，实现输入城市名称（全拼或者汉字）
# 点击搜索，展示这个城市7天之内的天气情况。
# 包括天气、温度、风向 、污染指数、限号等。
# 在展示列表的最下方可输入邮箱地址 点击发送按钮可将上面获取到的城市天气信息发送到邮箱中。
# Tips：
#  1、邮箱地址需要验证
#  2、做好输入内容异常的处理
#  3、参考网站：http://www.weather.com.cn/  （注：要温柔，别玩坏了）
#
# 例子：
# 城市：北京  日期：05.20 天气状况：多云 温度：21度  风向：西南风三到四级  污染指数：217  限号：7
# 城市：北京  日期：05.21 天气状况：阴了 温度：11度  风向：东南风三到四级  污染指数：247  限号：9
# 城市：北京  日期：05.22 天气状况：阳了 温度：31度  风向：东南风三到四级  污染指数：217  限号：4

import wx
from songxin.L4.WeatherSearchGUI import WeatherSearchGUI

province = ['安徽', '北京', '重庆', '福建', '甘肃', '广东',
                         '广西', '贵州', '海南', '河北', '河南', '湖北', '湖南', '黑龙江', '吉林', '江苏',
                         '江西', '辽宁', '内蒙古', '宁夏', '青海', '山东', '陕西', '山西', '上海', '四川',
                         '天津', '西藏', '新疆', '云南', '浙江']
app = wx.App(False)
window = WeatherSearchGUI(None)
window.set_m_province_choice_content(province)
window.m_province_choice.SetSelection(0)
window.Show(True)
app.MainLoop()