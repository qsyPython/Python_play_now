#!/usr/bin/pyhon

"""
html.parser的核心是HTMLParser类。工作的流程是：当你feed给它一个类似HTML格式的字符串时，它会调用goahead方法向前迭代各个标签，
并调用对应的parse_xxxx方法提取start_tag,tag,data,comment和end_tag等等标签信息和数据，然后调用对应的方法对这些抽取出来的内容进行处理

handle_startendtag  #处理开始标签和结束标签
handle_starttag     #处理开始标签，比如<xx>
handle_endtag       #处理结束标签，比如</xx>或者<……/>
handle_charref      #处理特殊字符串，就是以&#开头的，一般是内码表示的字符
handle_entityref    #处理一些特殊字符，以&开头的，比如 &nbsp;
handle_data         #处理<xx>data</xx>中间的那些数据
handle_comment      #处理注释
handle_decl         #处理<!开头的，比如<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
handle_pi           #处理形如<?instruction>的

def handle_starttag(self, tag, attrs)  #处理开始标签，比如<xx>
def handle_data(self, data)            #处理<xx>data</xx>中间的那些数据
def handle_endtag(self, tag)           #处理结束标签，比如</xx>或者<……/>

"""

import html.parser as h

class MyHTMLParser(h.HTMLParser):

    a_t=False

    #处理开始标签，比如<xx>
    def handle_starttag(self, tag, attrs):
        print("开始一个标签:",tag)

        if str(tag).startswith("title"):
            self.a_t=True

        for attr in attrs:
            print("属性值：",attr)
       # print()

    #处理<xx>data</xx>中间的那些数据
    def handle_data(self, data):
        if self.a_t is True:
            print("得到的数据: ",data)

    #处理结束标签，比如</xx>或者<……/>
    def handle_endtag(self, tag):
        self.a_t=False
        print("结束一个标签:",tag)
        print()

p=MyHTMLParser()
mystr = '''<head>
    <meta charset="utf-8"/>
    <title>找找看 - 博客园</title>
    <link rel="shortcut icon" href="/Content/Images/favicon.ico" type="image/x-icon"/>
    <meta content="技术搜索,IT搜索,程序搜索,代码搜索,程序员搜索引擎" name="keywords" />
    <meta content="面向程序员的专业搜索引擎。遇到技术问题怎么办，到博客园找找看..." name="description" />
    <link type="text/css" href="/Content/Style.css" rel="stylesheet" />
    <script src="http://common.cnblogs.com/script/jquery.js" type="text/javascript"></script>
    <script src="/Scripts/Common.js" type="text/javascript"></script>
    <script src="/Scripts/Home.js" type="text/javascript"></script>
</head>'''
p.feed(mystr)
p.close()

import html.parser as h

class MyHTMLParser(h.HTMLParser):

    a_t=False

    #处理开始标签，比如<xx>
    def handle_starttag(self, tag, attrs):
        print("开始一个标签:",tag)

        if str(tag).startswith("title"):
            self.a_t=True

        for attr in attrs:
            print("属性值：",attr)
       # print()

    #处理<xx>data</xx>中间的那些数据
    def handle_data(self, data):
        if self.a_t is True:
            print("得到的数据: ",data)

    #处理结束标签，比如</xx>或者<……/>
    def handle_endtag(self, tag):
        self.a_t=False
        print("结束一个标签:",tag)
        print()



