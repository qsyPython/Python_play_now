

def add_fun(x,y):
    try:
        sum= x + y
        print("结果是:",sum)
    # except Exception as e:
    #     print(e)
    except:
        print("输入有误，请重新输入")

if __name__ == '__main__':


    add_fun("123",2)
    add_fun(3, 2)