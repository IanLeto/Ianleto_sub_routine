#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-29 19:19:38
# @Author  : IanLeto (ccssliu@163.com)
# @Link    : ccssliu@163.com
# @Version : $Id$

import os
# 装饰器==语法糖
# 装饰器 (1)
# 返回值 1
# param function


def decorator1(func_with_return=False):
    if func_with_return:
        a = func_with_return()
        return a
    else:
        return 'No Fuc Found'


@decorator1
def func1_decorator1(a=False):
    return a


def func1(a=False):
    return a


class d:

    def c(func):

        def cc(self, i):
            if i > 10:
                return i
            else:
                a = func(self, i)
                return a

        return cc

    @c
    def func1(self, i: int):
        return i * 2


def main():
    a1 = decorator1()
    # a2 = func1_decorator1()
    a3 = func1()
    print(a1)
    # print(a2)
    print(a3)
    dddd = d()
    print(dddd.func1(4))


if __name__ == '__main__':
    main()
