'''
目前有15种Tkinter的部件; 标准属性有7个；状态几何管理：pack()、grid()、place()
'''
# 创建一个GUI程序
# 1、导入 tkinter 模块(3.0以后tk为小写)
# 2、创建窗口对象和控件
# 3、指定这个控件的 master， 即这个控件属于哪一个
# 4、告诉 GM(geometry manager) 有一个控件产生了。

'''
==========================practice 1: 窗口对象==========================
'''

# import tkinter
# top_object = tkinter.Tk()# 创建窗口对象
# top_object.mainloop() # 进入消息循环

'''
==========================practice 2：添加列表==========================
'''
# from tkinter import *
# root = Tk()
# li = ['C','python','php','html','SQL','java']
# movie = ['css','jQuery','Bootstrap']
# listb1 = Listbox(root)#  创建1个列表组件
# listb2 = Listbox(root)#  创建1个列表组件
#
# for item in li:
#     listb1.insert(0,item)
#
# for item in movie:
#     listb2.insert(0,item)
# listb1.pack()
# listb2.pack()
# root.mainloop()


'''
==========================practice 3：label、button、entry、messagebox（弹框）==========================
'''
# from tkinter import  *
# import tkinter.messagebox as messagebox
#
# class ApplicationGUI(Frame):# Frame 是所有Widget的父容器
#     def __init__(self,master=None):
#         Frame.__init__(self,master)
#         self.pack()
#         self.creatWidgets()
#
#     def creatWidgets(self):
#         self.helloLabel = Label(self,text='wo leigecaca')
#         self.helloLabel.pack()
#
#         self.quitButton = Button(self,text='Quit',command=self.quit)
#         self.quitButton.pack()
#
#         self.nameInput = Entry(self)
#         self.nameInput.pack()
#
#         self.alertButton = Button(self,text='Hello',command=self.hello)
#         self.alertButton.pack()
#
#     def hello(self):
#         name = self.nameInput.get() or 'world'
#         messagebox.showinfo('弹框标题','Hello,%s,%s'%(name,'邱少一'))
#
# gui_app = ApplicationGUI()
# gui_app.master.title('Hello world')
# gui_app.mainloop()


'''
==========================practice 4：作业 -> 天气的界面：label、输入框、button==========================
'''
# from tkinter import *
#
#
# root = Tk()
# root.title('天气情况')
# root.geometry('500x400')
# root.resizable(width=True,height=False)
#
# # label Label(根对象,【属性】)
# label1 = Label(root, text='我就是看看不说话',bg='red',bd=10,font=('Arial',12),width=30,height=4)
# label1.pack(side=TOP)# 这里的side可以赋值为: LEFT  RTGHT TOP  BOTTOM
#
# #Frame: 容器
# frm = Frame(root)
# frm_L = Frame(frm)#left
# Label(frm_L,text='左上',bg='pink',font=('Arial',12)).pack(side=TOP)
# Label(frm_L, text="左下", bg="green", font=("Arial",12)).pack(side=TOP)
# frm_L.pack(side=LEFT)
#
# frm_R = Frame(frm)#right
# Label(frm_R,text='右上',bg='yellow',font=('Arial',12)).pack(side=TOP)
# Label(frm_R,text='右下',bg='purple',font=('Arial',12)).pack(side=TOP)
# frm_R.pack(side=RIGHT)
# frm.pack()
#
# #Entry :输入框，先绑定一个text的变量，用于set和get内容
# var = Variable()
# e = Entry(root,textvariable=var)
# var.set('初始化输入框')
# var.get()
# e.pack()
#
# #Text：文本。mark可以是行号,或者特殊标识,例如：
# # INSERT:光标的插入点CURRENT:鼠标的当前位置所对应的字符位置；
# # END:这个Textbuffer的最后一个字符；
# # SEL_FIRST:选中文本域的第一个字符，如果没有选中区域则会引发异常；
# # SEL_LAST：选中文本域的最后一个字符，如果没有选中区域则会引发异常
#
# t = Text(root,bg='yellow',width=30,height=5)
# t.insert('1.0','text1\n')
# t.insert(END,'text2\n')
# t.insert('1.0','text3\n')
# # t.delete('1.0','2.0')
# t.pack(side=TOP)
#
# #btn
# def print_hello():
#     t.insert(END,'hello\n')
# Button(root,text='点击btn',command=print_hello).pack()
#
# #Listbox
# var = StringVar()
# lb = Listbox(root,listvariable=var)
# list_item = [1,2,3,4]
# for item in list_item:
#     lb.insert(END,item)
# lb.delete(2,3) # 从 first para 到 second para 包括 边界！
# def click_listbox(event):# 点击事件
#     print(lb.get(lb.curselection()))
# lb.bind('<ButtonRelease-1>',click_listbox)
# lb.pack(side=TOP)
#
#
# root.mainloop()

#Scrollbar

from tkinter import  *
root = Tk()
root.title('滚动条')
root.geometry('300x200')
root.resizable(width=False,height=TRUE)

def print_item(event):
    print(lb.get(lb.curselection()))
var = StringVar()
lb =Listbox(root,height=5,selectmode=BROWSE,listvariable=var)
lb.bind('<ButtonRelease-1>',print_item)
list_item = [1,2,3,4,5,6,7,8,9]
for item in list_item:
    lb.insert(END,item)

scrl =Scrollbar(root)
scrl.pack(side=RIGHT,fill=Y)
lb.configure(yscrollcommand=scrl.set)
lb.pack(side=LEFT,fill=BOTH)
scrl['command'] = lb.yview()


root.mainloop()