
from SJTHomeWorkTwo_user import *

class User_System:
    def __init__(self):  #初始化信息
        self.user_list=[{"name":"SJT","age":"25","jobNum":1,"jobName":"iOS","phone":15801345534}]

    #操作编号
    def print_input(self):
        print("❤️️"*10)
        print("输入1 显示所有信息\n输入2 增加用户信息\n输入3 删除用户信息\n输入4 更新用户信息\n输入5 查找用户信息\n输入6 退出当前系统")
        print("❤️"*10)
        number_input =input(">>>请输入您要选择的编号：")
        return  number_input;

    #显示所有信息
    def show_all(self):
        for user in self.user_list:
            print(user)

    #增加用户信息
    def add_user(self):
        name = loadName("用户名字")
        age = loadAge()
        jobNum = loadJobNum()
        jobName = loadJobName()
        phone = loadPhone()
        userInfo = {"name":name,"age":age,"jobNum":jobNum,"jobName":jobName,"phone":phone}
        self.user_list.append(userInfo)
        print("⭐️⭐️⭐{}️添加成功⭐️⭐️⭐️".format(name))

    #删除用户信息
    def delect_user(self):
        name = loadName("要删除的用户名字")
        isCunzai = False
        for user in self.user_list:
            if user["name"] == name:
                isCunzai=True
                self.user_list.remove(user)
                print("⭐️⭐️⭐️删除{}成功⭐️⭐️⭐️".format(name))
        if not isCunzai:
            print("❗️❗️❗️{}不存在本系统❗️❗️❗️".format(name))

    #修改用户信息
    def updata_user(self):
        name = loadName("要修改的用户名字")
        isCunzai = False
        for user in self.user_list:
            if user["name"] == name:
                isCunzai=True
                user["age"] = loadAge()
                user["jobName"]= loadJobName()
                user["jobNum"]= loadJobNum()
                user["phone"] = loadPhone()
        if not isCunzai:
            print("❗️❗️❗️{}不存在本系统❗️❗️❗️".format(name))

    def search_user(self):
        name = loadName("要查找的用户名字")
        isCunzai = False
        for user in self.user_list:
            if user["name"] == name:
                isCunzai=True
                print(user)
        if not isCunzai:
            print("❗️❗️❗️{}不存在本系统❗️❗️❗️".format(name))

    def main(self):
        while True:
            select_input = self.print_input()
            if select_input in ["1","2","3","4","5","6"]:
                if select_input == "1":
                    self.show_all()
                elif select_input == "2":
                    self.add_user()
                elif select_input == "3":
                    self.delect_user()
                elif select_input == "4":
                    self.updata_user()
                elif select_input == "5":
                    self.search_user()
                elif select_input == "6":
                    print("退出成功~")
                    break
            else:
                print("❗️❗️❗请输入正确的编号❗️❗️❗")

