# 第一期作业：双色球
# 目标：在控制台打印符合要求的数字，输出7个数字即可，不需要带颜色
# 具体细节：1.红球区6个，区间1-33,蓝色球1个，区间1-16，一共7个
#           2.需要满足条件：①能够随机输出7个在区间内的数字，6个红球1个蓝球，6个红球不能重复，蓝球可以和前面有重复
#                           例如：在控制台上输出结果：[1,3,5,17,26,33 5]
#                           ②能够随机N注N倍，例如随机1注5倍，2注每注5倍
#                           例如：在控制台输出结果：[1,3,5,17,26,33 5]*3
#                                                   [1,5,8,15,20,26  9]*5
#                           ③能够手动输入6个红球，1个蓝球，并且可以乘以倍数
#                           例如：[1,5,8,15,20,26  9]*5
#           3.除了满足以上要求，还要能够做好边界检查，保证函数传入非法参数能够正常反应
#             例如：输入了不满足格式的，输入了非整数类型等等
#           4.会的多的可以用input，不会使用可以直接方法调用的形式，传不同参数实现就好
#  完成后由组长抽查，随机选6个人来讲自己的代码，也可以让觉得自己写的好的来讲

import random
def randomCount(*value):
    # 判断len，如果长度是1，在判断是不是整型
    if value.__len__() == 1:
        # 判断第一个参数是不是为整型
        if isinstance(value[0], int):
            # 判断第一个参数是不是等于1
            if value[0] != 1:
                print("请输入正确的编码数字，第一个参数：1随机，2随机N倍，3手动输入")
                return
            # 随机1-33无重复，前6个数
            list1 = random.sample(range(1, 34), 6)
            list1.append(random.randint(1, 16))
            print(list1)
        else:
            print("第一个参数：1随机，2随机N倍，3手动输入")
            return
    # 判断len 是不是等于3
    elif value.__len__() == 3:
        if isinstance(value[0], int):
            if value[0] != 2:
                print("请输入正确的编码数字，第一个参数：1随机，2随机N倍，3手动输入")
                return
            # 判断第二个参数是不是整型
            elif isinstance(value[1], int):
                if isinstance(value[2], int):
                    for _ in range(value[1]):
                        list2 = random.sample(range(1, 34), 6)
                        list2.append(random.randint(1, 16))
                        print(list2, "*", value[2])
                else:
                    print("第三个参数：整型，倍数")
                    return
            elif isinstance(value[1], list):
                if isinstance(value[2], int):
                    if len(value[1]) == 7:
                        for x in value[1]:
                            if not isinstance(x, int):
                                print("列表中有非整数，请重新输入")
                                return
                        current_list = set(value[1][0:6])
                        if len(current_list) < 6:
                            print("列表中有重复，请重新输入")
                            return
                        for x in value[1][0:6]:
                            if x not in range(1, 34):
                                print("前6个数为红球，需要满足在1-33之间")
                                return
                        if (value[1])[6] not in range(1, 17):
                            print("第七位为蓝球，需要满足在1-16之间")
                            return
                        print(value[1], "*", value[2])
                    else:
                        print("第二个参数：输入数字代表随机多少倍，输入list是手动选号,list长度为7")
                        return
                else:
                    print("第三个参数：整型，倍数")
                    return
            else:
                print("第二个参数：输入数字代表随机多少倍，输入list是手动选号")
                return
        else:
            print("第一个参数：1随机，2随机N倍，3手动输入")
            return

    else:
        print("""请按规则输入:
                        第一个参数：1随机，2随机N倍，3手动输入
                        第二个参数：输入数字代表随机多少倍，输入list是手动选号
                        第三个参数：整型，倍数""")
        return

if __name__ == '__main__':
    randomCount(2,[],5)