
class StudentSystem:

    def __init__(self):
        self.student_list=[{"name":"xiaohong","age":20,"stu_num":1000}]


    def print_info(self):
        print("*" * 20)
        print("输入1查看所有学生信息")
        print("输入2搜索学生信息")
        print("输入3增加学生信息")
        print("输入4删除学生信息")
        print("输入5修改学生信息")
        print("输入6退出程序")
        print("*"*20)
        user_input= input(">>>>请选择序号:")
        return  user_input

    def show_all_student_info(self):
        for stu in self.student_list:
            print(stu)

    def search_student(self):
        search_student_name = input("请输入要搜索的学生姓名:")
        stu_exist = False
        for stu in  self.student_list:
            if stu["name"] == search_student_name:
                stu_exist = True
                print(stu)
        if not  stu_exist:
            print(">>>>您要查找的学生不存在")

    def add_student_info(self):
        name = input("请输入要增加的学生姓名：")
        age = input("请输入要增加的学生年龄：")
        stu_num = input("请输入要增加的学生学号：")
        new_student= {"name":name,"age":age,"stu_num":stu_num}
        self.student_list.append(new_student)
        print("增加成功")

    def delect_stundent_info(self):
        name = input("请输入要删除的学生名字：")
        stu_exit = False
        for stu in self.student_list:
            if stu["name"] == name:
                stu_exist=True
                self.student_list.remove(stu)
                print("删除成功")
        if not stu_exist:
            print("您要删除的学生不存在")
    def update_student_info(self):
        name = input("请输入要修改的学生名字：")
        stu_exit = False
        for stu in self.student_list:
            if stu["name"] ==  name:
                stu_exit=True
                stu.age = input("请输入要修改学生的年龄:")
                stu.num = input("请输入要修改学生的学号：")
        if not stu_exit:
            print("您要修改的{}不存在".format(name))

    def main(self):
        while True:
            #1、提示信息，让用户输入
            user_input = self.print_info()
            #2、判断用户输入
            if user_input in ["1","2","3","4","5","6"]:
                if user_input == "1":
                #2.1 用户选择查看所有
                    self.show_all_student_info()
                elif user_input == "2":
                #2.2 用户选择搜索学生
                    self.search_student()
                elif user_input == "3":
                #2.3 用户选择增加学生
                    self.add_student_info()
                elif user_input == "4":
                #2.4 用户选择删除学生
                    self.delect_stundent_info()
                elif user_input == "5":
                #2.5 用户选择修改学生
                    self.update_student_info()
                elif user_input == "6":
                #2.6
                    print("欢迎下次再来！")
                    break;

            else:
                print("请重新输入")

if __name__ == '__main__':
    student_sys = StudentSystem()
    student_sys.main()
