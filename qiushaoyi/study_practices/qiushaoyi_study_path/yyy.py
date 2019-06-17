'''
	作者：邱少一
	日期：2018/ / 
	功能：
	
    
'''
# /usr/bin/env python
# -*- coding: utf-8 -*-

import logging, os


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)


main()
print('END')
