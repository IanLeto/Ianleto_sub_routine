# -*- coding: utf-8 -*-
# @Time    : 2018/9/25 11:02
# @Author  : Ian Leto
# @File    : Coroutine_Test.py
# 干啥的    : 学习协程

from Fluent_Python import data_usage
from functools import wraps
from collections import namedtuple

data = data_usage.Data()


def coroutine(func):
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        # 激活生成器协程
        next(gen)
        # 返回已经激活的生成器协程
        return gen
    return primer


class L_conroutine:

    Result = namedtuple('Result', 'count average')

    @coroutine
    def get_calc_average(self):
        total = 0.0
        count = 0
        average = 0
        while True:
            term = yield average
            total += term
            count += 1
            average = total / count

    # 经典的生成器函数举例
    @coroutine
    def simple_coro(self, a):
        print('a={}'.format(a))
        b = yield a
        print('b={},实参a={}'.format(b, a))
        c = yield a + b
        print('c={}, b={}, 实参a={}'.format(c, b, a))
        d = yield c + 2000
        yield d

    # 存在返回值得协程
    @coroutine
    def averager_with_return(self):
        total = 0.0
        count = 0
        average = None
        while True:
            term = yield
            if term is None:
                break
            total += term
            count += 1
            average = total/count
        return average


if __name__ == '__main__':
    # a 实例
    a = L_conroutine()
    # gen 拿到刚刚定义好的生成器
    # 注意yield 关键字的特殊性
    gen = a.get_calc_average()
    for i in range(1, 4):
        # sb错误
        # print(a.get_calc_average(i))
        # 使用send 发送数据给生成器
        print(gen.send(i))

    gen2 = a.simple_coro(100)
    gen2.send(10)
    gen2.send(20)
    gen3 = a.averager_with_return()
    print(gen3.send(100))
    print(gen3.send(100))

