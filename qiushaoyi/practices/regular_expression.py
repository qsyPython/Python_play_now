'''
正则表达式是一个特殊的字符序列。它能帮助你方便的检查一个字符串是否与某种模式匹配
re.match(pattern, string, flags=0)
match 是绝对匹配，只匹配字符串的开始，若匹配失败，函数返回None；
search 是相对匹配，匹配整个字符串，有就ok

解释：
返回值：<_sre.SRE_Match object; span=(3, 5), match='12'>
span表示匹配到内容所在的位置；match表示匹配到的内容

参数：
1、pattern : 一个字符串形式的正则表达式
2、string: 要比较的字符串
3、正则表达式修饰符 - 可选标志:
flags : 可选，表示匹配模式，具体参数为：
re.I 忽略大小写
re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
re.M 多行模式
re.S 即为 . 并且包括换行符在内的任意字符（. 不包括换行符）
re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
re.X 为了增加可读性，忽略空格和 # 后面的注释

'''

'''
==========================practice 1: match初级使用==========================
'''
# import re
#
# print(re.match('www','www.runoob.com').span())
# print(re.match('com','ww.runoob.com'))


'''
==========================practice 2：match的高级使用==========================
r'(.*) are (.*?) .*'
解读：
r表示字符串为非转义(转义为：\字母)的原始字符串，让解释器忽略反斜杠/
(.*)表示第一个匹配分组，.*代表匹配除 换行符:\n 之外的所有字符
are 代表字符串are
(.*?)表示第二个匹配分组，.*?代表非贪婪模式下，只匹配符合条件的最少字符
.* 代表匹配除换行符之外的所有字符，但表示不是分组，不计入匹配group结果中
'''
# import re
# line = 'Cats cocoapods are smarter than dogs'
# matchObj = re.match(r'(.*) are (.*?) .*',line,re.M|re.I)#可多行匹配、大小写不敏感
# if matchObj:
#     print(matchObj.group())
#     print(matchObj.group(1))
#     print(matchObj.group(2))
# else:
#     print('No match')

'''
==========================practice 3：search的初级使用==========================
'''
# import re
# print(re.search('www','www.runoob.com').span())
# print(re.search('com','www.runoob.com').span())

'''
==========================practice 4：search的高级使用==========================
'''
# import re
# lines = 'Cats are smater than dogs'
# matchObj = re.search(r'(.*) are (.*?) .*',lines,re.M|re.I)
# if matchObj:
#     print(matchObj.group())
#     print(matchObj.group(1))
#     print(matchObj.group(2))
# else:
#     print('No search')

'''
==========================practice 5：sub的使用==========================
re.sub(pattern, repl, string, count=0, flags=0)
替换字符串中的匹配项
参数：
pattern : 正则中的模式字符串。
repl : 替换的字符串，也可为一个函数。
string : 要被查找替换的原始字符串。
count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
flags: 可选的标志

1、r'#.*$'：
r 表示字符串为非转义的原始字符串，让解释器忽略反斜杠/
# 表示#
.*: 表示匹配除换行符\n之外的所有字符
$: 表示匹配字符串的末尾

2、r'\D':
r: 表示字符串为非转义的原始字符串
\D：匹配任意非数字

3、'(?P<value>\d+)'：
(): 表示是group
？P<value>：表示一个命名参数value,它会捕获字符串中的这部分，然后将它赋值给value参数传递给字符串
\d：表示匹配的是整型
+: 表示多个
'''
# import re
# phone = '2004-959-559 # 这是一个国外电话号码'
# num = re.sub(r'#.*$','',phone)
# print('电话号码是：',num)
#
# num = re.sub(r'\D','',phone)
# print('电话号码是：',num)

# import re
# def double(matched):
#     value1 = int(matched.group('value'))
#     return str(value1*2)
# s = 'Ajkldjoteiog123+321'
# new_s = re.sub('(?P<value>\d+)',double,s)
# print(new_s)

'''
==========================practice 6：compile的初级使用==========================
re.compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象
供 match() 、 search()、 findall() 和finditer() 这两个函数使用。

r'\d+'：表示 至少匹配一个数字 的字符串！

r'([a-z]+) ([a-z]+)',re.I: 表示 匹配包含a到z的数字，忽略
'''

# import re
# pattern = re.compile(r'\d+')
# m = pattern.match('one12twothree34four')
# print(m)
# m = pattern.match('one12twothree34four', 2, 10)
# print(m)
# m = pattern.match('one12twothree34four',3,20) #从第3位的‘1’开始匹配
# print(m)

# import re
# pattern = re.compile(r'([a-z]+) ([a-z]+)',re.I)
# m = pattern.match('Hello World Wide Web')
# print(m)

'''
==========================practice 7：compile中的高级使用==========================
r'\d+': 至字少匹配一个数的字符串
'''
# import re
# pattern = re.compile(r'\d+')
# result1 = pattern.findall('runoob 123 google 456')
# result2 = pattern.findall('run88oob123google456',0,10)
# print(result1)
# print(result2)

# import re
# str = '12a32bc43jf3'
# it = re.finditer(r'\d+',str)
# for match in it:
#     print(match.group())


'''
==========================practice 8：split拆分数据成新的list==========================
\W+ :至少匹配一个非字母数字及下划线
'''
import re
split_str = re.split('\W+','runoob, runoob, runoob.')
print(split_str)


'''
正则表达式模式:
^	匹配字符串的开头
$	匹配字符串的末尾。
.	匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。
[...]	用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'
[^...]	不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符。
re*	匹配0个或多个的表达式。
re+	匹配1个或多个的表达式。
re?	匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
re{ n}	精确匹配 n 个前面表达式。例如， o{2} 不能匹配 "Bob" 中的 "o"，但是能匹配 "food" 中的两个 o。
re{ n,}	匹配 n 个前面表达式。例如， o{2,} 不能匹配"Bob"中的"o"，但能匹配 "foooood"中的所有 o。"o{1,}" 等价于 "o+"。"o{0,}" 则等价于 "o*"。
re{ n, m}	匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式
a| b	匹配a或b
(re)	匹配括号内的表达式，也表示一个组
(?imx)	正则表达式包含三种可选标志：i, m, 或 x 。只影响括号中的区域。
(?-imx)	正则表达式关闭 i, m, 或 x 可选标志。只影响括号中的区域。
(?: re)	类似 (...), 但是不表示一个组
(?imx: re)	在括号中使用i, m, 或 x 可选标志
(?-imx: re)	在括号中不使用i, m, 或 x 可选标志
(?#...)	注释.
(?= re)	前向肯定界定符。如果所含正则表达式，以 ... 表示，在当前位置成功匹配时成功，否则失败。但一旦所含表达式已经尝试，匹配引擎根本没有提高；模式的剩余部分还要尝试界定符的右边。
(?! re)	前向否定界定符。与肯定界定符相反；当所含表达式不能在字符串当前位置匹配时成功
(?> re)	匹配的独立模式，省去回溯。
\w	匹配字母数字及下划线
\W	匹配非字母数字及下划线
\s	匹配任意空白字符，等价于 [\t\n\r\f].
\S	匹配任意非空字符
\d	匹配任意数字，等价于 [0-9].
\D	匹配任意非数字
\A	匹配字符串开始
\Z	匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串。
\z	匹配字符串结束
\G	匹配最后匹配完成的位置。
\b	匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。
\B	匹配非单词边界。'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'。
\n, \t, 等.	匹配一个换行符。匹配一个制表符。等
\1...\9	匹配第n个分组的内容。
\10	匹配第n个分组的内容，如果它经匹配。否则指的是八进制字符码的表达式。

正则表达式实例:
python	匹配 "python".
[Pp]ython	匹配 "Python" 或 "python"
rub[ye]	匹配 "ruby" 或 "rube"
[aeiou]	匹配中括号内的任意一个字母
[0-9]	匹配任何数字。类似于 [0123456789]
[a-z]	匹配任何小写字母
[A-Z]	匹配任何大写字母
[a-zA-Z0-9]	匹配任何字母及数字
[^aeiou]	除了aeiou字母以外的所有字符
[^0-9]	匹配除了数字外的字符

特殊字符类：
.   匹配除 "\n" 之外的任何单个字符。要匹配包括 '\n' 在内的任何字符，请使用象 '[.\n]' 的模式。
[.\n]   匹配包括"\n" 在内的任何字符
\d	匹配一个数字字符。等价于 [0-9]。
\D	匹配一个非数字字符。等价于 [^0-9]。
\s	匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [ \f\n\r\t\v]。
\S	匹配任何非空白字符。等价于 [^ \f\n\r\t\v]。
\w	匹配包括下划线的任何单词字符。等价于'[A-Za-z0-9_]'。
\W	匹配任何非单词字符。等价于 '[^A-Za-z0-9_]'。
'''