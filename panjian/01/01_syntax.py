#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 将整个模块
import sys, os

# 从某个模块中导入某个函数
from keyword import kwlist

'''
先了解下基本语法
'''


# 函数名 'main'
def main():
    print(os.getcwd())

    # 解释器自动查找所需模块的路径的列表
    print(sys.path)
    print('命令行参数如下:')
    for V in sys.argv:
        print(V, '', end='')
    else:
        print('\n\n')

    print("双引号\"")
    print('单引号\'')

    sDes = '''定义一个比较长的注视，
    第二行
    print默认是在行尾部加换行的'''
    print(sDes)

    # 列表类型 （可以包含不同类型数据）
    aChar = ['a', 'b', 'c', 'd', 'e']
    aChar[3:5] = [13, 14]
    print('输出第一个 ' + aChar[0])
    print(aChar + aChar[1:])

    iA = input('please enter: ')

    # 定义变量 & 赋值
    # type 查询变量所指的对象类型
    sAType = type(iA)

    # 多个变量赋值
    iB = iC = 100

    iX, iY, sZ = 1, 2, "abcdefg"

    # 删除对象引用
    del iX, iY

    print('输入的是：' + iA)
    print(sAType)

    print('\nif elif else ->')
    if iA.isdigit():
        print('是数字')

        # 函数调用
        iSum = sum(iA, iB)
        print(' {0} + {1} = {2}'.format(iA, iB, iSum))
    elif iA.isspace():
        print('是空格')
    else:
        print('不是数字')

    # 循环列表 & 输出内容
    print('\nfor ->')
    for sChar in aChar:
        print(sChar, end='')
        if (sChar == 'd'):
            print('\nbreak for end')
            break
        if (sChar == 'c'):
            continue
        iC += 1
    else:
        print('\nfor end')

    print('\nwhile ->')
    iI = 0
    while (iI < 10):
        print(iI, end=',')
        iI += 1
    else:
        print('\niI=', iI, '不小于10～结束')

    print('\nC = ' + str(iC))

    print('\npython保留字 ->')
    # print(keyword.kwlist)
    print(kwlist, '\n')

    sys.stdout.write('测试' + '\n');
    sys.stdout.write('一行多条语句执行；\';\'分割' + '\n')

    print('\nend')

    sRes = iC if iC >= iI else iI
    print('三元运算 ', sRes)


def sum(iA, iB):
    return int(iA) + int(iB)


# 最小的类
class Calculator:
    # pass是空语句，是为了保持程序结构的完整性
    # pass不做任何事情
    pass


'''
当直接运行当前脚本时，__name__ 的值为 __main__
当作为模块导入时并不运行 main()
'''
if __name__ == '__main__':
    main()
