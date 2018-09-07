def fun():
    for i in range(20):
        x = yield i
        print('good', x)
    print('total: ',x)

if __name__ == '__main__':
    a=fun()
    print(a)

# for i in range(30):
#     x=a.__next__()
#     print(x)
