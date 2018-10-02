#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-12 11:18:53
# @Author  : IanLeto (ccssliu@163.com)
# @Link    : ccssliu@163.com
# @Version : $Id$

import os
import collections

problemSize = 1000
for count in range(5):
    num = 0
    work = 1
    for j in range(problemSize):
        for k in range(problemSize):
            num += 1
            work += 1
            work -= 1

    print(problemSize, num)
    problemSize *= 2

from collections import Counter
