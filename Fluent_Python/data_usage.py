# -*- coding: utf-8 -*-
# @Time    : 2018/9/25 11:03
# @Author  : Ian Leto
# @File    : data_usage.py
# 干啥的    :


class Data:

    def __init__(self,):
        self.data_dict1 = dict.fromkeys(['a', 'b', 'c'], 'AAA')
        self.data_dict2 = zip(('a', 'b', 'c'), range(1, 4))
