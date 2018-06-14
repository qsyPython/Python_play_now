import urllib.request
import smtplib
from email.mime.text import MIMEText
import os
import wx

from songxin.L4.CityUrlParser import CityUrlParser
from songxin.L4.MySQLCreate import MySQLCreate

class WeatherSearchGUI(wx.Frame):

    def __init__(self, parent):
        self.info = ""
        self.max_width = 650
        self.max_height = 400
        self.city_url_parser = CityUrlParser()
        self.provinces = []
        self.citys = []
        self.my_sql = MySQLCreate()
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(self.max_width, self.max_height), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"天气查询", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        bSizer1.Add(self.m_staticText1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        gbSizer1 = wx.GridBagSizer(0, 0)
        gbSizer1.SetFlexibleDirection(wx.BOTH)
        gbSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"请选择查询的省/市：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        gbSizer1.Add(self.m_staticText2, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_province_choiceChoices = []
        self.m_province_choice = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           m_province_choiceChoices, 0)
        self.m_province_choice.SetSelection(0)
        gbSizer1.Add(self.m_province_choice, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_city_choiceChoices = []
        self.m_city_choice = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_city_choiceChoices, 0)
        self.m_city_choice.SetSelection(0)
        gbSizer1.Add(self.m_city_choice, wx.GBPosition(0, 2), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_search_button = wx.Button(self, wx.ID_ANY, u"搜索", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_search_button.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        gbSizer1.Add(self.m_search_button, wx.GBPosition(0, 3), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer1.Add(gbSizer1, 0, wx.EXPAND, 5)


        fgSizer1 = wx.FlexGridSizer(0, 3, 0, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        today_sb = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        today_sb.SetMinSize(wx.Size(200, 150))
        self.bitmap_today = wx.StaticBitmap(today_sb.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.bitmap_today.SetMinSize(wx.Size(40, 40))

        today_sb.Add(self.bitmap_today, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.city_name_today = wx.StaticText(today_sb.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.city_name_today.Wrap(-1)
        today_sb.Add(self.city_name_today, 0, wx.ALL, 5)

        self.m_date_today = wx.StaticText(today_sb.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.m_date_today.Wrap(-1)
        today_sb.Add(self.m_date_today, 0, wx.ALL, 5)

        self.m_weather_condition_today = wx.StaticText(today_sb.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                                       wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_weather_condition_today.Wrap(-1)
        today_sb.Add(self.m_weather_condition_today, 0, wx.ALL, 5)

        self.m_temperature_today = wx.StaticText(today_sb.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                 wx.DefaultSize, 0)
        self.m_temperature_today.Wrap(-1)
        today_sb.Add(self.m_temperature_today, 0, wx.ALL, 5)

        self.m_pm_today = wx.StaticText(today_sb.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.m_pm_today.Wrap(-1)
        today_sb.Add(self.m_pm_today, 0, wx.ALL, 5)

        fgSizer1.Add(today_sb, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND | wx.ALL, 5)

        tomorrow_sb = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        tomorrow_sb.SetMinSize(wx.Size(200, 150))
        self.bitmap_tomorrow = wx.StaticBitmap(tomorrow_sb.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        self.bitmap_tomorrow.SetMinSize(wx.Size(40, 40))

        tomorrow_sb.Add(self.bitmap_tomorrow, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.city_name_tomorrow = wx.StaticText(tomorrow_sb.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                                wx.DefaultPosition, wx.DefaultSize, 0)
        self.city_name_tomorrow.Wrap(-1)
        tomorrow_sb.Add(self.city_name_tomorrow, 0, wx.ALL, 5)

        self.m_date_tomorrow = wx.StaticText(tomorrow_sb.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_date_tomorrow.Wrap(-1)
        tomorrow_sb.Add(self.m_date_tomorrow, 0, wx.ALL, 5)

        self.m_weather_condition_tomorrow = wx.StaticText(tomorrow_sb.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                                          wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_weather_condition_tomorrow.Wrap(-1)
        tomorrow_sb.Add(self.m_weather_condition_tomorrow, 0, wx.ALL, 5)

        self.m_temperature_tomorrow = wx.StaticText(tomorrow_sb.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                                    wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_temperature_tomorrow.Wrap(-1)
        tomorrow_sb.Add(self.m_temperature_tomorrow, 0, wx.ALL, 5)

        self.m_pm_tomorrow = wx.StaticText(tomorrow_sb.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_pm_tomorrow.Wrap(-1)
        tomorrow_sb.Add(self.m_pm_tomorrow, 0, wx.ALL, 5)

        fgSizer1.Add(tomorrow_sb, 1, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        day_after_tomorrow_sb = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        day_after_tomorrow_sb.SetMinSize(wx.Size(200, 150))
        self.bitmap_after = wx.StaticBitmap(day_after_tomorrow_sb.GetStaticBox(), wx.ID_ANY, wx.NullBitmap,
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.bitmap_after.SetMinSize(wx.Size(40, 40))

        day_after_tomorrow_sb.Add(self.bitmap_after, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.city_name_after = wx.StaticText(day_after_tomorrow_sb.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                             wx.DefaultPosition, wx.DefaultSize, 0)
        self.city_name_after.Wrap(-1)
        day_after_tomorrow_sb.Add(self.city_name_after, 0, wx.ALL, 5)

        self.m_date_after = wx.StaticText(day_after_tomorrow_sb.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                          wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_date_after.Wrap(-1)
        day_after_tomorrow_sb.Add(self.m_date_after, 0, wx.ALL, 5)

        self.m_weather_condition_after = wx.StaticText(day_after_tomorrow_sb.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                                       wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_weather_condition_after.Wrap(-1)
        day_after_tomorrow_sb.Add(self.m_weather_condition_after, 0, wx.ALL, 5)

        self.m_temperature_after = wx.StaticText(day_after_tomorrow_sb.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                                 wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_temperature_after.Wrap(-1)
        day_after_tomorrow_sb.Add(self.m_temperature_after, 0, wx.ALL, 5)

        self.m_pm_after = wx.StaticText(day_after_tomorrow_sb.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                        wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_pm_after.Wrap(-1)
        day_after_tomorrow_sb.Add(self.m_pm_after, 0, wx.ALL, 5)

        fgSizer1.Add(day_after_tomorrow_sb, 1,
                     wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer1.Add(fgSizer1, 1, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        gbSizer2 = wx.GridBagSizer(0, 0)
        gbSizer2.SetFlexibleDirection(wx.BOTH)
        gbSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, u"请输入邮箱：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        gbSizer2.Add(self.m_staticText5, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_email_edit = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0)
        gbSizer2.Add(self.m_email_edit, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_send_button = wx.Button(self, wx.ID_ANY, u"发送", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer2.Add(self.m_send_button, wx.GBPosition(0, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        bSizer1.Add(gbSizer2, 0, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_province_choice.Bind(wx.EVT_CHOICE, self.m_province_choiceOnChoice)
        self.m_city_choice.Bind(wx.EVT_CHOICE, self.m_city_choiceOnChoice)
        self.m_search_button.Bind(wx.EVT_BUTTON, self.m_search_buttonOnButtonClick)
        self.m_send_button.Bind(wx.EVT_BUTTON, self.m_send_buttonOnButtonClick)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def m_search_buttonOnButtonClick(self, event):
        print("获取内容：", self.provinces[self.m_province_choice.GetSelection()],"-",self.citys[self.m_city_choice.GetSelection()])
        search_city = self.citys[self.m_city_choice.GetSelection()]
        city_url = self.my_sql.search_html(search_city)
        self.info = self.city_url_parser.city_url_parser(self.provinces[self.m_province_choice.GetSelection()]+"-"+self.citys[self.m_city_choice.GetSelection()],city_url)
        print(self.info)
        strs = self.info.split("|")
        print(strs)
        today_info = strs[0].split(",")
        self.city_name_today.SetLabel(' '+today_info[0])
        self.m_date_today.SetLabel(today_info[1])
        self.m_temperature_today.SetLabel(today_info[2])
        self.m_weather_condition_today.SetLabel(today_info[3])
        self.m_pm_today.SetLabel(today_info[4])
        self.show_image(today_info[5], 1)
        tomorrow_info = strs[1].split(",")
        self.city_name_tomorrow.SetLabel(' ' + tomorrow_info[0])
        self.m_date_tomorrow.SetLabel(tomorrow_info[1])
        self.m_temperature_tomorrow.SetLabel(tomorrow_info[2])
        self.m_weather_condition_tomorrow.SetLabel(tomorrow_info[3])
        self.m_pm_tomorrow.SetLabel(tomorrow_info[4])
        self.show_image(tomorrow_info[5], 2)
        after_info = strs[2].split(",")
        self.city_name_after.SetLabel(' ' + after_info[0])
        self.m_date_after.SetLabel(after_info[1])
        self.m_temperature_after.SetLabel(after_info[2])
        self.m_weather_condition_after.SetLabel(after_info[3])
        self.m_pm_after.SetLabel(after_info[4])
        self.show_image(after_info[5], 3)
        event.Skip()

    def m_send_buttonOnButtonClick(self, event):
        self.send_email(self.m_email_edit.GetValue(),self.info)
        event.Skip()

    def set_m_province_choice_content(self,provinces):
        self.provinces = provinces
        self.m_province_choice.SetItems(provinces)
        self.m_city_choice.SetSelection(0)
        WeatherSearchGUI.get_citys(self,self.provinces[0])

    def m_province_choiceOnChoice(self, event):
        WeatherSearchGUI.get_citys(self,self.provinces[self.m_province_choice.GetSelection()])
        event.Skip()

    @staticmethod
    def get_citys(self, search_key):
        citys = self.my_sql.rangion_search_city(search_key)
        print(citys)
        self.citys.clear()
        self.citys = str(citys).split(",")
        self.m_city_choice.SetItems(self.citys)
        self.m_city_choice.SetSelection(0)


    def m_city_choiceOnChoice(self, event):
        event.Skip()

    def show_image(self, url,switch):
        strs = url.split("/")
        file = urllib.request.urlopen(url).read()
        file_path = self.write_file(file,strs[len(strs) -1])
        print(file_path)
        image = wx.Image(file_path, wx.BITMAP_TYPE_PNG)
        bmp = image.ConvertToBitmap()
        size = self.get_size(bmp)
        bmp = image.Scale(size[0], size[1]).ConvertToBitmap()
        if switch == 1:
            self.bitmap_today.SetSize(size)
            self.bitmap_today.SetBitmap(bmp)
            self.Show()
        elif switch == 2:
            self.bitmap_tomorrow.SetSize(size)
            self.bitmap_tomorrow.SetBitmap(bmp)
            self.Show()
        else:
            self.bitmap_after.SetSize(size)
            self.bitmap_after.SetBitmap(bmp)
            self.Show()

    def get_size(self, bmp):
        width = bmp.GetWidth()
        height = bmp.GetHeight()
        if width > self.max_width:
            height = height * self.max_width / width
            width = self.max_width
        if height > self.max_height:
            width = width * self.max_height / height
            height = self.max_height
        size = width, height
        return size

    def write_file(self,pic_file,pic_name):
        folder = os.path.exists("Image")
        if not folder:
            os.makedirs("Image")
        file = open(os.path.abspath("Image") + '\\%s'%pic_name, 'wb')
        file.write(pic_file)
        file.close()
        return os.path.abspath("Image") + '\\%s'%pic_name


    def send_email(self, email_address, content):
        msg_from = 'sx_killer@126.com'  # 发送方邮箱
        passwd = 'T2m9v5y9'  # 填入发送方邮箱的授权码
        subject = "近三日天气"  # 主题
        content =  content# 正文
        msg = MIMEText(content)
        msg['Subject'] = subject
        msg['From'] = msg_from
        msg['To'] = email_address
        try:
            s = smtplib.SMTP_SSL("smtp.126.com") # 邮件服务器及端口号
            s.login(msg_from, passwd)
            s.sendmail(msg_from, email_address, msg.as_string())
            print("发送成功")
        except s.SMTPException as e:
            print("发送失败", e)
        finally:
            s.quit()