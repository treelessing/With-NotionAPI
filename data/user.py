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

class data():
    def __init__(self):
        self.maximum = 15    # 一页最大书量

        self.url = "https://book.douban.com/mine?status=collect"
        self.cookie = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.54",
            "Cookie": 'bid=1nEmG9g21ZM; viewed="33944838"; push_doumail_num=0; douban-fav-remind=1; ll="118296"; ct=y; loc-last-index-location-id="118296"; dbcl2="215871379:ad3LPL3tSTs"; ck=NAsM; ap_v=0,6.0; push_noty_num=0'
        }

        self.Token = "secret_9yAkBCPLd5rakqZgiTqxdtGCqJTCoPQXGsA08yI8fLs"
        self.databaseID = "c284686fbf50467898bf2c0cc224ba51"

        self.star = "⭐️⭐️⭐️⭐️⭐️"    # 默认: 5星
        self.status = "读完"          # 书籍状态，默认：读完
        self.bookCategory = "纸质书"   # 阅读类型，默认：纸质书
        self.bookRemark = "不发布"     # 书评，默认：不发布
        self.bookExcerpt = "尚未整理"       # 书摘，默认：尚未整理