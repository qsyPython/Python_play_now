"""
    作者：邱少一
    功能：根据设定的规则来判断密码强度,包括：文件写入和读取、工具类以及设定密码强度等级
    日期：2018/04/14
"""
import os,platform,socket

class PasswordTool:
    """
        密码工具类
    """
    def __init__(self, password):
        self.password = password
        self.strength_level = 0

    def process_password(self):
        # 规则1：密码长度大于8
        if len(self.password) >= 8:
            self.strength_level += 1
        else:
            print('密码长度要求至少8位！')

        # 规则2：包含数字
        if self.check_number_exist():
            self.strength_level += 1
        else:
            print('密码要求包含数字！')

        # 规则3：包含字母
        if self.check_letter_exist():
            self.strength_level += 1
        else:
            print('密码要求包含字母！')

    def check_number_exist(self):
        """
            判断字符串中是否含有数字
        """
        has_number = False

        for c in self.password:
            if c.isnumeric():
                has_number = True
                break

        return has_number

    def check_letter_exist(self):
        """
            判断字符串中是否含有字母
        """
        has_letter = False
        for c in self.password:
            if c.isalpha():
                has_letter = True
                break
        return has_letter

class FileTool:
    """
        文件工具类
    """
    def __init__(self, filepath):
        self.filepath = filepath

    def write_to_file(self, line):
        with open(self.filepath,'a',newline='') as f:
            f.write(line)

    def read_from_file(self):
        with open(self.filepath,'r',newline='') as f:
            lines = f.readlines()
            return lines


def main():
    """
        主函数
    """
    try_times = 5
    filepath = 'password_6.0.txt'
    file_tool = FileTool(filepath)

    while try_times > 0:
        password = input('请输入密码：')
        password_tool = PasswordTool(password)
        password_tool.process_password()

        hostname=socket.gethostname()
        ip = socket.gethostbyname(hostname)
        line = '操作人pc：{}, 操作人ip：{}, 密码：{}, 强度：{}\n'.format(hostname,ip,password, password_tool.strength_level)
        file_tool.write_to_file(line)

        if password_tool.strength_level == 3:
            print('恭喜！密码强度合格！')
            break
        else:
            print('密码强度不合格！')
            try_times -= 1

        print()

    if try_times <= 0:
        print('尝试次数过多，密码设置失败！')

    lines = file_tool.read_from_file()
    print(lines)

if __name__ == '__main__':
    main()
