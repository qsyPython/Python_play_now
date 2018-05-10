#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re


def isIP(sIP):
    oCompileIP = re.compile(
        '^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$')
    if oCompileIP.match(sIP):
        return True
    else:
        return False
