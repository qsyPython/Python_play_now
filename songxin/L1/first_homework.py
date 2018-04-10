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