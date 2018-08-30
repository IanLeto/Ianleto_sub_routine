#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-30 08:53:09
# @Author  : IanLeto (ccssliu@163.com)
# @Link    : ccssliu@163.com
# @Version : $Id$
# hash

# 元组列表
from operator import itemgetter
# gdp : billion  population: person , per GDP
nation_data = [
    ('China', 13173.585, 1391200000, 8643),
    ('USA', 19555.874, 328250000, 59501),
    ('Japan', 4342.16, 126490000, 38440),
]
# 按gdp 排行
# key = itemgetter(1) 代替lambda

print(sorted(nation_data, key=itemgetter(1), reverse=True))

# 注释语法


def fuc1(text: str, max_len: 'int > 0' = 100) -> str:
    return 'xx'

a = [{'k': 'v'}]
