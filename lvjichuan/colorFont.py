# 获取标签内容(?<=<color\b[^>]*?>)[^<>]+(?=</color>)
# 获取标签 <(color.*?)>(.*?)</color>
# 获取属性 (?<=<color=)[^<>]+(?=>)
# 获取标签 <(.*?)>[^<>]+</(.*?)>
# \033[32;0m 开头
# \033[0m结尾。
import re
# 30（黑色）、31（红色）、32（绿色）、 33（黄色）、34（蓝色）、35（洋红）、36（青色）、37（白色）
colors={'black':30,'red':31,'green':32,'yellow':33,'blue':34,'carmine':35,'cyan':36,'white':37}
def colorList():
    print(colors.keys())
def colorPrintChar(mystr,color):
    print("\033[%d;0m%s\033[0m"%(colors[color],mystr))
    return
def colorPrint(mystr):
    #获取所有标签
    strRe=r'<(.*?)>[^<>]+</(.*?)>'
    reObj = re.compile(strRe, re.I)
    searchObj=reObj.findall(mystr)
    # print(searchObj)
    # print(searchObj[0])
    # print(searchObj[0][0])

    # 替换颜色代码
    mstr=mystr
    for color in searchObj:
        # print(color[0])
        # print(colors[color[0]])
        mstr=mstr.replace("<"+color[0]+">", '\033['+str(colors[color[0]])+';0m')
        mstr=mstr.replace("</"+color[0]+">",'\033[0m')
    print(mstr)
    #num=re.sub(r'<[^/](.*?)>',"or",str)
    #print(num)
    # strRe2=r'<(color.*?)>(.*?)</color>+'
    # reObj2 = re.compile(strRe2, re.I)
    # searchObj2 = reObj2.findall(str)
    # print(searchObj2)
    #
    # strRe3= r'(?<=<color=)[^<>]+(?=>)'
    # reObj3 = re.compile(strRe3, re.I)
    # searchObj3 = reObj3.findall(str)
    # print(searchObj3)
    return