# Filename: P2.py
def print_p2():
    print("Hello P2")


#  Python两种输出值的方式: 表达式语句和 print() 函数。
#  第三种方式是使用文件对象的 write() 方法，标准输出文件可以用 sys.stdout 引用。
#  如果你希望输出的形式更加多样，可以使用 str.format() 函数来格式化输出值。
#  如果你希望将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现。
s = 12331
str(s)
repr(s)
print(s)
print('{0} 和 {1}'.format('Google', 'Runoob'))

# str = input("请输入：");
# print("你输入的内容是: ", str)
f = open("dd.txt", "r+", encoding="utf8")
# f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")
# r = f.read()
# print(r)
# st = f.readline()
# print(st)
s = f.readlines()
print(s)
# 关闭打开的文件
f.close()

# file.close()
# 关闭文件。关闭后文件不能再进行读写操作。
# file.flush()
# 刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。
# file.fileno()
# 返回一个整型的文件描述符(file descriptor FD 整型), 可以用在如os模块的read方法等一些底层操作上。
# file.isatty()
# 如果文件连接到一个终端设备返回 True，否则返回 False。
# file.next()
# 返回文件下一行。
# file.read([size])
# 从文件读取指定的字节数，如果未给定或为负则读取所有。
# file.readline([size])
# 读取整行，包括 "\n" 字符。
# file.readlines([sizeint])
# 读取所有行并返回列表，若给定sizeint>0，返回总和大约为sizeint字节的行, 实际读取值可能比 sizeint 较大, 因为需要填充缓冲区。
# file.seek(offset[, whence])
# 设置文件当前位置
# file.tell()
# 返回文件当前位置。
# file.truncate([size])
# 从文件的首行首字符开始截断，截断文件为 size 个字符，无 size 表示从当前位置截断；
# 截断之后 V 后面的所有字符被删除，其中 Widnows 系统下的换行代表2个字符大小。
# file.write(str)
# 将字符串写入文件，没有返回值。
# file.writelines(sequence)
#向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。