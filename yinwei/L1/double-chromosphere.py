#双色球
# 目标：在控制台打印符合要求的数字，输出7个数字即可，不需要带颜色
# 具体细节：
# 1.红球区6个，闭区间1-33,蓝色球1个，闭区间1-16，一共7个
# 2.需要满足条件：①能够随机输出7个在区间内的数字，6个红球1个蓝球，6个红球不能重复，蓝球可以和前面有重复
# 例如：在控制台上输出结果：[1,3,5,17,26,33 5]
# ②能够随机N注N倍，例如随机1注5倍，2注每注5倍
# 例如：在控制台输出结果：[1,3,5,17,26,33 5]*3
# [1,5,8,15,20,26  9]*5
# ③能够手动输入6个红球，1个蓝球，并且可以乘以倍数
# 例如：[1,5,8,15,20,26  9]*5
# 3.除了满足以上要求，还要能够做好边界检查，保证函数传入非法参数能够正常反应
# 例如：输入了不满足格式的，输入了非整数类型等等
# 4.会的多的可以用input，不会使用可以直接方法调用的形式，可传不同参数实现
