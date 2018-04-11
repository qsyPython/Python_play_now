
##python中间的空格起到代码块分割作用
name = "小岳岳"
if  name == "小岳岳":
    print("小岳岳")
    print("郭德纲")
    print("郭德纲他老婆")
print("hello world")
#if处理逻辑表达式
import  os
cmd = input("cmd")
isrun = (cmd == "notepad")
if isrun:
    os.system("notepad")

mystr = input("他的名字")
if  mystr == "java":
    print("java")
elif mystr == "ios":
    print("ios")
elif mystr == "php":
    print("php")
else:
    print("C++")