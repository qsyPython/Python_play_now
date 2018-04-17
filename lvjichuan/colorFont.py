# 获取标签内容(?<=<color\b[^>]*?>)[^<>]+(?=</color>)
# 获取标签 <(color.*?)>(.*?)</color>
# 获取属性 (?<=<color=)[^<>]+(?=>)
# \033[32;0m 开头
# \033[0m结尾。
import re
# 30（黑色）、31（红色）、32（绿色）、 33（黄色）、34（蓝色）、35（洋红）、36（青色）、37（白色）
colors={'black':30,'red':31,'green':32,'yellow':33,'blue':34,'carmine':35,'cyan':36,'white':37}
def colorPrintChar(str,color):
    print("\033[%d;0m%s\033[0m"%(colors[color],str))
    return
def colorPrint(str):
    strRe=r'(?<=<color\b[^>]>)*?[^<>]+(?=</color>)+'

    reObj = re.compile(strRe)
    searchObj=reObj.findall(str)

    print(searchObj)

    return