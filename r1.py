#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-26 22:38:51
# @Author  : IanLeto (ccssliu@163.com)
# @Link    : ccssliu@163.com
# @Version : $Id$

from collections import Counter

def fib(n, counter):
	counter.increment()
	if n < 3:
		return 1
	else:
		return fib(n-1,counter) + fib(n-2, counter)
Size = 2
print('%s,%s' %("Size", "Counter"))
for i in range(1,5):
	count = Counter()
	fib(i, count)
	print ('%d,%d' % (i,count))


