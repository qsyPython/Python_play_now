

import base64

#Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据。
'''
base64模块提供了6个函数用于Base64的编码和解码，可以将他们分为三组。

base64.b64encode(s, altchars=None) 
base64.b64decode(s, altchars=None, validate=False)
参数s代表需要编码/解码的数据。其中b64encode的参数s的类型必须是字节包（bytes）。b64decode的参数s可以是字节包（bytes），也可以是字符串（str）。

由于Base64编码后的数据中可能会含有’+’或者’/’两个符号，如果编码后的数据用于url或者文件系统的路径中，就可能会导致Bug。所以base64模块提供了将编码后的数据中’+’和’/’进行替换的方法。

参数altchars必须是长度为2的字节包，这两个符号会用于替换编码后数据中的’+’和’/’。这个参数默认是None。

参数validate默认为False。如果它为True时，base64模块在进行解码前会先检查s中是否有非base64字母表中的字符，如果有的话则抛出错误binascii.Error: Non-base64 digit found。

如果数据的长度不正确则会抛出错误binascii.Error: Incorrect padding。

base64.standard_b64encode(s) 
base64.standard_b64decode(s)

这组函数会直接将参数s传到上一组函数中。

base64.urlsafe_b64encode(s) 
base64.urlsafe_b64decode(s)

这组函数同样基于第一组函数，但进行编码后会将输出数据中的’+’和’/’替换为’-‘和’_’。解码前则将数据中的’-‘和’_’替换为’+’和’/’。

另，Base64编码还会产生一个符号’=’，这个符号用于将数据长度填充到4的倍数。
'''
s = "abcr34r344r="
a = base64.b64decode(s.encode('utf-8'))
print(a)



aaa= "我怕摔"
b = aaa.encode()
print(b)

ssss= b.decode()
print(ssss)





