import logging

logging.basicConfig(level=logging.INFO)


# logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(level=logging.WARNING)
# logging.basicConfig(level=logging.ERROR)
# 错误、调试和测试：跟踪程序的执行，查看变量的值是否正确; 捕获错误、记录错误、抛出错误
# 1、错误：当我们认为某些代码可能会出错时，就可以用try来运行这段代码: except语句和后面的else语句是2选1执行
# Python所有的错误都是从BaseException类派生的，Except是BaseException的子类
def foo():
    try:
        print('try...')
        r = 10 / 0
        print('result:', r)
    # except Exception as e:
    # 	raise print('except:',e)
    except ValueError as e:
        print('ValueError:', e)
    except ZeroDivisionError as e:
        print('ZeroDivisionError:', e)
    else:
        print('else...')
    finally:
        print('finally...')

    print('END')


# foo()

def right():
    try:
        print('try...')
        r = 10 / 2
        print('result:', r)
    except Exception as e:
        raise e
    else:
        print('else...')
    finally:
        print('finally...')
    print('END')


# right()


# 不需要在具体的某个func中判断，在合适的层次中捕获即可使用
def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)  # logging 可以记录错误内容
        print('Exception Main Test:', e)
    finally:
        print('finally...')


# main()

# 抛出错误：创建错误class
class FooError(ValueError):
    pass


def foo3(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value:%s', s)

    return 10 / n


# foo3('0')

# 2、调试:核心是logging
# print（打印，启动Python解释器时必须手动删除print）、
# assert（断言：启动Python解释器时可以用-O参数来关闭assert。那时的assert相当于pass）
# logging()：有debug，info，warning，error等几个级别，当我们指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了。这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息
# pdb.set_trace(): 断点调试
def testFoo(s):
    n = int(s)
    assert n != 0, '若你为0，打印我的这儿信息：n is zero!'
    return 10 / n


def testMain():
    return testFoo('0')


# testMain()

# s = '0'
s = '5'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

# s = '0'
s = '3'
m = int(s)
# pdb.set_trace() # 运行到这里会自动暂停
print(10 / n)

# 3、单元测试（一个模块、一个函数或者一个类来进行正确性检验的测试工作）： TDD测试驱动开发
# 如一个函数单元测试的 4个 测试用例：输入正数、输入负数、输入0、输入非数值类型
abs(1)
abs(-1.3)
abs(0)


# abs([]) 若不符合要求的参数,会报typeError

class Dict(object):
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr(self, key, value):
        self[key] = value
