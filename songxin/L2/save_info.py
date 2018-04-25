import os
from songxin.L2.user_info import UserInfo


class SaveInfo:
    def __init__(self, path, username, password):
        self.path = path
        self.username = username
        self.password = password


    def set_user_info(self):
        folder = os.path.exists(self.path)
        if not folder:
            os.makedirs(self.path)
        file = open(os.path.abspath(self.path) + '\\save_info.txt', 'w', encoding='utf8')
        file.write(self.username + "," + self.password)
        file.close()

    def get_user_info(self):
        folder = os.path.exists(self.path)
        if not folder:
            os.makedirs(self.path)
        file = open(os.path.abspath(self.path) + '\\save_info.txt', 'r', encoding='utf8')
        str = file.read()
        if "," in str:
            str_array = str.split(",")
            user = UserInfo(str_array[0], str_array[1])
            print(user.get_username())
            print(user.get_password())

