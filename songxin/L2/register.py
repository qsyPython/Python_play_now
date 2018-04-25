from songxin.L2.save_info import SaveInfo
class Register:
    def register(self):
        input("欢迎注册本软件,点击回车继续")
        flag = True
        input_text = "请输入手机号:"
        while flag:
            phone_number = input(input_text)
            if phone_number == ":exit":
                return
            if phone_number.isdigit() is False or len(phone_number) > 11 or phone_number[0] is not "1":
                flag = True
                input_text = "请确认后，重新输入手机号："
            else:
                flag = False
        flag = True
        while flag:
            input_text = "请输入密码:"
            phone_number = input(input_text)
            if phone_number == ":exit":
                return
            password = input(input_text)
            if len(password) < 6:
                flag = True
                print("密码不能少于6位")
            else:
                flag = False
        save_info = SaveInfo("save_info", phone_number, password)
        save_info.set_user_info()
        save_info.get_user_info()
        print("注册完成")

r = Register()
r.register()
