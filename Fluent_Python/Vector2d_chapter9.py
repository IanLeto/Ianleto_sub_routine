# -*- coding: utf-8 -*-
# @Time    : 2018/9/21 13:39
# @Author  : Ian Leto
# @File    : Vector2d_chapter9.py
# 干啥的    : 向量,这个经常被拿来举例

from array import array
import math


class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    # 使该变量不能随意更改
    # 以只读特性公开
    @property
    def x(self):
        return self.__x

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r} {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __hash__(self):
        return hash(self.x) ^ hash(self.x)

    def __eq__(self, other):
        return tuple(self) == tuple(other)


class Father():
    pass


class Son(Father):
    pass


