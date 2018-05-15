# encoding: utf-8

""" ScoreSystem module. """

__author__ = 'xie dong'

import os

class ScoreSystem():
    def __init__(self,password):
        self._password = password

    def get_password(self):
        return self._password

    def imput_score(self,student):
        folder = os.path.exists("score.txt")
        list = []
        if not folder:
            list.append(student.get_name()+","+student.get_score())
        else:
            with open("score.txt", "r") as f:
                for line in f.readlines():
                    strs = line.split(",")
                    if student.get_name() == strs[0]:
                        strs[1] = student.get_score()
                    list.append(strs[0]+ "," +strs[1])

        with open("score.txt", "w") as f1:
            f1.writelines(list)


    def get_score(self,name):
        score = ""
        with open("score.txt","r") as f:
            for line in f.readlines():
                strs = line.split(",")
                if name == strs[0]:
                    score = strs[1]
        return score

class Student():
    def __init__(self,name):
        self._name = name
        self._score = 0

    def set_name(self,name):
        self._name = name

    def get_name(self):
        return self._name

    def set_score(self,score):
        self._score = score

    def get_score(self):
        return self._score