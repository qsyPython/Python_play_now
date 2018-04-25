ch='我'
print(ord(ch)) #编号
print(chr(25105))

ch='A'
print(chr(ord(ch)+1))

print("\u6211") #汉字统一码

#读取数据
import os
path = os.path.expanduser(r"~/Desktop/test1.html")
print(path)
with open(path) as f:
    content = f.read()
    for i in content.splitlines():
        print(i)