#!/usr/bin/python
# -*- coding: UTF-8 -*-

def sum(*Params):
    iSum = 0
    for Param in Params:
        iSum += Param
    return iSum


def avg(*Params):
    iSum = sum(*Params)
    iAmount = len(Params)

    iAvg = 0 if iAmount == 0 else iSum / iAmount
    return iAvg
