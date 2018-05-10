#!/usr/bin/python

"""
Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。

什么是摘要算法呢？摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。

举个例子，你写了一篇文章，内容是一个字符串'how to use python hashlib - by Michael'，并附上这篇文章的摘要是
'2d73d4f15c0db7f5ecb321b6a65e5d6d'。如果有人篡改了你的文章，并发表为'how to use python hashlib - by Bob'，
你可以一下子指出Bob篡改了你的文章，因为根据'how to use python hashlib - by Bob'计算出的摘要不同于原始文章的摘要。

可见，摘要算法就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest，目的是为了发现原始数据是否被人篡改过。

摘要算法之所以能指出数据是否被篡改过，就是因为摘要函数是一个单向函数，计算f(data)很容易，但通过digest反推data却非常困难。
而且，对原始数据做一个bit的修改，都会导致计算出的摘要完全不同。

我们以常见的摘要算法MD5为例，计算出一个字符串的MD5值：


"""

import hashlib


def get_md5(url):
    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()


if __name__ =='__main__':
    print(get_md5("http://jobbole.com".encode("utf-8")))


# 如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的：
m = hashlib.md5()
m.update('how to use md5 in '.encode("utf-8"))
m.update('python hashlib?'.encode("utf-8"))
print (m.hexdigest())


"""
MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示。

另一种常见的摘要算法是SHA1，调用SHA1和调用MD5完全类似：
"""

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode("utf-8"))
sha1.update('python hashlib?'.encode("utf-8"))
print (sha1.hexdigest())

"""
SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。

比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法越慢，而且摘要长度更长。

有没有可能两个不同的数据通过某个摘要算法得到了相同的摘要？完全有可能，
因为任何摘要算法都是把无限多的数据集合映射到一个有限的集合中。这种情况称为碰撞，
比如Bob试图根据你的摘要反推出一篇文章'how to learn hashlib in python - by Bob'，
并且这篇文章的摘要恰好和你的文章完全一致，这种情况也并非不可能出现，但是非常非常困难。
"""

"""
Python自带的hmac模块实现了标准的Hmac算法

我们首先需要准备待计算的原始消息message，随机key，哈希算法，这里采用MD5，使用hmac的代码如下：
可见使用hmac和普通hash算法非常类似。hmac输出的长度和原始哈希算法的长度一致。需要注意传入的key和message都是bytes类型，
str类型需要首先编码为bytes。
"""

import hmac
message = b'Hello world'
key = b'secret'
h = hmac.new(key,message,digestmod='MD5')
print(h.hexdigest())

def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = hmac_md5(self.key, password)


