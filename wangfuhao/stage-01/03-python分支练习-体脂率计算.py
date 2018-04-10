# 输入
# 	身高
personHeight = input("请输入身高(m):")
personHeight = float(personHeight)

# 	体重
personWeight = input("请输入体重(kg):")
personWeight = float(personWeight)

# 	年龄
personAge = input("请输入年龄:")
personAge = int(personAge)

# 	性别
personSex = input("请输入性别（男：1 女：0）:")
personSex = int(personSex)

# 容错处理, 数据有效性的验证
if not (0 < personHeight < 3 and 0 < personWeight < 300 and 0 < personAge < 150 and (personSex == 1 or personSex == 0)):
    # 退出程序
    print("数据不符合标准, 程序退出")
    exit()

# 处理数据
# 	计算体脂率
# BMI = 体重（kg） / （身高 * 身高）（米）
# 体脂率 = 1.2 * BMI + 0.23 * 年龄 - 5.4 - 10.8*性别
BMI = personWeight / (personHeight * personHeight)
TZL = 1.2 * BMI + 0.23 * personAge - 5.4 - 18.8 * personSex
TZL /= 100

# 区分男女
if personSex == 1:
    # 判定男性标准的代码
    result = 0.15 < TZL < 0.18
elif personSex == 0:
    # 判定女性标准的代码
    result = 0.25 < TZL < 0.28

# 问好
if personSex == 1:
    wenhao = "先生你好:"
    minNum = 0.15
    maxNum = 0.18
elif personSex == 0:
    wenhao = "女士你好:"
    minNum = 0.25
    maxNum = 0.28

# 提示部分
if result:
    notice = "恭喜您, 身体非常健康, 请继续保持"
else:
    if TZL > maxNum:
        notice = "请注意, 您的身体不正常, 偏胖"
    else:
        notice = "请注意, 您的身体不正常, 偏瘦"

print(wenhao, notice)