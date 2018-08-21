'''
	2.0新增功能：循环的终止 break
    3.0新增功能：保存密码及强度到文件中:mode  r ,w ,r+（读写）,a(在末尾添加附加内容，不会覆盖掉之前w写入的内容)
    4.0新增功能：读取文件中的密码：read()：返回整个内容的字符串。readline()返回文件中下一行内容的字符串。readlines()返回每段以\n结尾的字符串的整个文件list。
    文件可进行 for line in f:
    5.0新增功能：定义一个password工具class：把面向过程中的变量抽成一个class的属性来处理，然后把相关包含的变量的方法，抽成class的def
    6.0新增功能：定义一个文件工具类
'''


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
            print('密码长度要求至少8位!')

        # 规则2：包含数字
        if self.check_number_exist():
            self.strength_level += 1
        else:
            print('密码要求包含数字!')

        # 规则3：包含字母
        if self.check_letter_exist():
            self.strength_level += 1
        else:
            print('密码要求包含字母!')

    # 检查字符串中是否包含数字
    def check_number_exist(self):
        has_number = False

        for c in self.password:
            if c.isnumeric():
                has_number = True
                break
        return has_number

    # 检查字符串中是否包含字母
    def check_letter_exist(self):
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

    def write_to_file(self, line):  # 逐行添加到filepath
        f = open(self.filepath, 'a')
        f.write(line)
        f.close()

    def read_from_file(self):
        f = open(self.filepath, 'r')
        lines = f.readlines()
        f.close()
        return lines


def main():
    """
         主函数
    """
    try_times = 5  # 尝试密码的总次数
    filepath = 'password_6.0.txt'  # 新建文件的名称（默认是当前目录下）
    file_tool = FileTool(filepath)

    while try_times > 0:
        password = input('请输入密码: ')
        password_tool = PasswordTool(password)
        password_tool.process_password()

        line = '密码：{}, 强度：{}\n'.format(password, password_tool.strength_level)
        # 写的操作
        file_tool.write_to_file(line)

        if password_tool.strength_level == 3:
            print('恭喜！密码强度合格！')
            break
        else:
            print('密码强度不合格！')
            try_times -= 1

    if try_times <= 0:
        print('尝试次数过多，密码设置失败！')

    # 读操作
    lines = file_tool.read_from_file()
    print(lines)


if __name__ == '__main__':
    main()
