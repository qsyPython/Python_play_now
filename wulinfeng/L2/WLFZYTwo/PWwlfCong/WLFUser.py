#coding=utf-8

#用户名密码类，用户名为手机号，手机号需要正则

import re
import sys
import os




class WlfUsers (object): #定义一个用户对象
    #初始化init方法
    # def __init__(self):
    #
    #
    # def __init__(self,phoneNumber,passWord):
    #     self.phoneNumber = phoneNumber
    #     self.passWord = passWord

    def set_phoneNumber(self,phoneNumber):
        self.phoneNumber = phoneNumber

    def set_passWord(self,passWord):
        self.passWord = passWord

    def get_phoneNumber(self):
        return self.phoneNumber

    def get_passWord(self):
        return self.passWord


    def printContent(self):
        print(self.phoneNumber,self.passWord)

    def matchPhoneNumer(self):
        pp = re.compile('^0\d{2,3}\d{7,8}$|^1[358]\d{9}$|^147\d{8}')

        matchResult = pp.match(self.phoneNumber)

        if matchResult:
            print("手机号正确")
            return True
        else:
            print("手机号不正确")
            return False


    def matchPassWord(self):
        pp = re.compile('^(?!\d+$)(?![A-Za-z]+$)[a-zA-Z0-9]{6,8}$')
        matchResult = pp.match(self.passWord)

        if matchResult:
            print("密码输入正确")
            return True
        else:
            print("密码不正确")
            return False