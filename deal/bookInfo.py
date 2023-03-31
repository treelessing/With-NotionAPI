# -*- coding: UTF-8 -*-
"""
@Project: Python
@File: bookInfo.py
@Date: 2023/3/30 20:31
@Author: YaPotato
@version: python 3.11
@IDE: PyCharm 2023.1
"""
from data.book import book
from data.user import user
"""
本文件调试中
"""
class info():
    def __init__(self):
        self.list = []
        self.user = user()

    def renew(self):
        self.list = []

    # 作者
    def author(self):
        for i in range(self.user.maximum):
            AuthorContent = book().author.peek()
            authorPerson = AuthorContent[0].split("、")  # 作者
            print(authorPerson)
            for j in range(len(authorPerson)):
                self.list.append(dict(name=authorPerson[j]))
            book().author.pop()
        return self.list


if __name__ == '__main__':
    print(info().author())
    # print(type(info().author()))
    # print(type(info().author()[0]))


