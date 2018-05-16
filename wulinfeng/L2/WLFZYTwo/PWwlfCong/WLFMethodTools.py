# -*- coding:utf-8 -*-

# 手机号码归属地查询

# 1、调用聚合数据手机号码归属地查询接口
# 2、若聚合数据API结果为null，调用360查询接口
# 3、否则为null

import sys, urllib, urllib.request, json
from PWwlfCong import WLFUser
# Python 3中 urllib.request 代替 urllib2


#http://apistore.baidu.com/astore/usercenter 进入此网站

class WLFMethodTools:

    #输入验证手机号 集齐 归属地查询
    def inputPhone(self):
        phoneNumer = input("请输入您的手机号")
        user = WLFUser.WlfUsers()
        user.set_phoneNumber(phoneNumer)
        flag = user.matchPhoneNumer()
        return (flag,phoneNumer)

    # 输入验证密码是否正确
    def inputPassWord(self):
        passWord = input("请输入6-8位字母数字组合密码")
        user = WLFUser.WlfUsers()
        user.set_passWord(passWord)
        flag = user.matchPassWord()
        return (flag,passWord)

    def doLoginAera(self):
            print("欢迎使用七乐康医生：\n")
            pro = ""
            cit = ""
            quh = ""
            company = ""
            password = ""
            temp = ()
            temp = self.inputPhone(self)
            flag = temp[0]
            phoneNumer = temp[1]
            while flag == False:
                temp = self.inputPhone(self)
                flag = temp[0]
                phoneNumer = temp[1]
            url = 'http://apis.juhe.cn/mobile/get?phone=%s&key=89baea64806cf2020fed945e44a65dd2' % phoneNumer
            req = urllib.request.Request(url)
            resp = urllib.request.urlopen(req)
            content = resp.read()
            if (content):
                messageDic = json.loads(content)
                err = messageDic['error_code']
                if(err == -1):
                    print("查询归属地失败")
                else:
                    pro = messageDic['result']['province'] #省份
                    cit = messageDic['result']['city'] #城市
                    quh = messageDic['result']['areacode']  # 区号
                    company = messageDic['result']['company']  # 服务商
                    temp = self.inputPassWord(self)
                    flag = temp[0]
                    password = temp[1]
                    while flag == False:
                        temp = self.inputPassWord(self)
                        flag = temp[0]
                        password = temp[1]
            print("欢迎进入七乐康医生，你的账号密码是",phoneNumer,password,"归属地是",pro,cit,"服务商",company,"区号",quh)






