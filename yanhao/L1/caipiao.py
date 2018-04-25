import  re
import random

#num = str(input("请输入注数和倍数，用+号链接："))

def randMath():
    redList = random.sample(range(1, 33), 6)  # 生成红球
    redList.sort()
    blueList = random.randint(1, 16)
    redList.append(blueList)
    return redList;


def getCaipiao(multiple=0):
    result = []
    num = int(multiple)
    for i in range(num):
        result.append(randMath())
    return result

if __name__ == '__main__':
    num = str(input("请输入注数和倍数，用空格号分开："))
    while True:
        if num.isdigit():
            k = int(num)
            if k >10:
                print("一张彩票不能大于10注")
                break
            re = getCaipiao(num)
            for i in range(len(re)):
                print(re[i])
            break
        else:
            pattern = re.compile(r'\d+')
            result = pattern.findall(num)

            #print(len(result))
            if len(result) == 2:
               res =getCaipiao(result[0])
               for i in range(len(res)):
                   print(str(res[i]) + "*" + (result[1]))

            break


