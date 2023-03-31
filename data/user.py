# -*- coding: UTF-8 -*-
"""
@Project: Python
@File: user.py
@Date: 2023/3/30 17:59
@Author: YaPotato
@version: python 3.11
@IDE: PyCharm 2023.1
"""
# from data.book import book

class user():
    def __init__(self):
        self.maximum = 15    # 最大书量

        self.url = "Your website URL of the douban"
        self.cookie = {
            "User-Agent": "",
            "Cookie": ''
        }

        self.Token = "You token of the Notion API"
        self.databaseID = "DatanaseID"

        self.star = "⭐️⭐️⭐️⭐️⭐️"    # 默认: 5星
        self.status = "读完"          # 书籍状态，默认：读完
        self.bookCategory = "纸质书"   # 阅读类型，默认：纸质书
        self.bookRemark = "不发布"     # 书评，默认：不发布
        self.bookExcerpt = "尚未整理"       # 书摘，默认：尚未整理

    """
    以下内容调试中
    """
    #
    # def properties(self):
    #     return {
    #         "状态": {
    #             "select": {
    #                 "name": self.status
    #             }
    #         },
    #         "评分": {
    #             "select": {
    #                 "name": self.star
    #             }
    #         },
    #         "来源": {
    #             "select": {
    #                 "name": self.bookCategory  # 默认: 纸质书
    #             }
    #         },
    #         "短评": {
    #             "rich_text": [
    #                 {
    #                     "text": {
    #                         "content": book().comment.peek()
    #                     }
    #                 }
    #             ]
    #         },
    #         "读完时间": {
    #             "date": {
    #                 "start": book().Date.peek()
    #             }
    #         },
    #         "出版社": {
    #             "select": {
    #                 "name": str(publishingCompany)
    #             }
    #         },
    #         "出版日期": {
    #             "date": {
    #                 "start": formatDate
    #             }
    #         },
    #         "作者": {
    #             "multi_select": author
    #
    #         },
    #         "类别": {
    #             "multi_select": categoryBook
    #         },
    #         "书评": {
    #             "select": {
    #                 "name": self.bookRemark
    #             }
    #         },
    #         "书摘": {
    #             "select": {
    #                 "name": self.bookExcerpt
    #             }
    #         }
    #     }
