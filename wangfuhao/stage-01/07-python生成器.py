#创建生成器的第一种方式
l = (i for i in range(1, 10000000) if i % 2 == 0)

print(next(l))
print(next(l))
print(l.__next__())

# for i in l:
#     print(i)

print("=========================方式二")
#创建生成器的第二种方式
# yied, 可以去阻断当前的函数执行, 然后, 当使用next()函数, 或者, __next__(),
# 都会让函数继续执行, 然后, 当执行到下一个 yield语句的时候, 又会被暂停
def test():
    print("xxx")
    yield 1
    print("a")

    yield 2
    print("b")

    yield 3
    print("c")

    yield 4
    print("d")

    yield 5
    print("e")

g = test()
print(g)

def test2():
    for i in range(1, 9):
        yield i
f = test2()
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))

print("=========================send方法")
def test():
    # print("xxx")
    res1 = yield 1 # "ooo"
    print(res1)

    res2 = yield 2
    print(res2)

g = test()

# print(g.__next__())
# print(g.__next__())
# print(g.send("ooo"))
print(g.send(None))
print(g.send(666))

print("=========================close方法")
def test():
    yield 1
    print("a")

    yield 2
    print("b")

    yield 3
    print("c")

    return 10


g = test()

print(g.__next__())
print(g.__next__())

g.close()

# print(g.__next__())
# # print(g.__next__())

####注意: 生成器只能遍历一次

print("=========================递归函数")
# 功能: 如果是不直接知道结果的数据, 就进行分解 9 9 * 8! 8 =
# 如果说, 直接知道结果的数据, 就直接返回 1! = 1
def jiecheng(n):
    if n == 1:
        return 1
    # n != 1
    return n * jiecheng(n - 1)

result = jiecheng(5)
print(result)


