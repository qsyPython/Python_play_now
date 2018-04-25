
import re
import sys
import os

def loadName(detailStr):
    user_name = ""
    while True:
        name = input(">>>请输入{}(长度不超过10个字)：".format(detailStr))
        if len(name)<=10 or len(name)>0:
            user_name= name;
            break;
        else:
            print("**请重新输入**")
    return user_name;


def loadAge():
    user_age = ""
    while True:
        age = input(">>>请输入用户年龄(不能大于100岁)：")
        if age.isdigit():
            ageNum = int(age);
            if ageNum>0 and ageNum <= 100:
                user_age = age
                break
            else:
                print("**请重新输入**")
        else:
            print("**请重新输入**")

    return user_age;

def loadJobNum():
    job_num = ""
    while True:
        num = input(">>>请输入用户工号：")
        if num.isdigit():
            jonNum = int(num);
            if jonNum > 0:
                job_num = num
                break
            else:
                print("**请重新输入**")
        else:
            print("**请重新输入**")

    return job_num;

def loadJobName():
    job_name = ""
    while True:
        name = input(">>>请输入用户工作名(长度不超过10个字)：")
        if len(name) <= 10 or len(name) > 0:
            job_name = name;
            break;
        else:
            print("**请重新输入**")
    return job_name;

def loadPhone():
    # 正则匹配电话号码
    user_phone=""
    while True:
        phone = input('请输入手机号:')
        p2 = re.compile('^(1[0-9]\\d{9})$')
        phonematch = p2.match(phone)
        if phonematch:
            user_phone = phone
            break
        else:
            print("**请重新输入手机号**")
    return user_phone


