#与  and 或  or  取反

isma1 = 1 > 2
isma2 = 1 > 3
isma3 = 1 <= 3

if isma1 and isma2 and isma3:
    print("你是个傻瓜")
else :
    print("我只是尊重你")

if isma1 or isma2 or isma3:
    print("你是个傻瓜")
else :
    print("我只是尊重你")

if not isma1:
   print("我不是个傻瓜")
else:
   print("你把我当成了傻瓜")

num1 = 3
num2 = 4
print(id(num1),id(num2))
if num1 is num2:
    print("同一个地址")

if num1 is not num2:
    print("不是同一个地址")

