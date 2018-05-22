from roles import person,phoneOp

print("欢迎您进入注册页面")
name = input("请输入真实姓名：")
isSuccess = False
while isSuccess == False:
    phoneNumber = input("请输入电话号码：")
    phoneOpOne = phoneOp(phoneNumber);
    print(phoneOpOne)
    if phoneOpOne.checkPhoneNumber(phoneNumber):
        isSuccess = True
        print("恭喜您注册成功！")
    else:
        isSuccess = False

