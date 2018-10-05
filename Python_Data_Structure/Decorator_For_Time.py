from time import time


def IanTimeCalc(func):
    start = time()
    result = func()
    stop = time()
    run_time = str(stop - start)

    return run_time


@IanTimeCalc
def main():
    Ian_test = []
    for i in range(1, 999999):
        Ian_test.append(i)
    return Ian_test

# 闭包


def outer():
    b = 10
    c = []

    def inner():
        d = b
        return d
    return inner


def outer2():
    b = 10

    def inner():
        return '1'
    return inner


def outer3():
    b = 10

    def inner():
        b = 1
        return '1'
    return inner


# def outer4():
#     b = 10
#
#     def inner():
#         b += 1
#         return '1'
#     return inner


def outer5():
    b = 10

    def inner():
        # 把b 标记为自由变量
        # 即便 b = b+1 在正常情况下会被认为是创建了局部变量
        nonlocal b
        b += 1
        return b
    return inner


def outer6():
    b = []

    def inner():
        # 这里利用的是b 的可变性
        # 你的b 还是你的b
        b.append(1)
        return b
    return inner


import time


def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        res = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ','.join(repr(i) for i in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, res))
        return res
    return clocked


import functools


def clock2(func):
    """

    :param func:接收测试的函数
    :return:
    """
    def clocked(*args, **kwargs):
        t0 = time.time()
        res = func(*args)
        elapsed = time.time() - t0
        name = func.__name__
        arg_list = []
        if args:
            arg_list.append(','.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, v) for k, v in sorted(kwargs.items())]
            arg_list.append(', '.join(pairs))
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_list, res))
        return res
    return clocked


@clock2
def snooze(seconds):
    time.sleep(seconds)


@clock2
def func():
    count = 0
    for i in range(10000):
        count += 1
    return count

@clock2
def func3(i:int):
    return i*2

@clock2
@functools.lru_cache()
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


# import html

# python 重载

from functools import singledispatch


# @singledispatch
# def htmlize(obj):
#     content = html.escape(repr(obj))
#     return '<p>{}<p>'.format(content)
#
#
# @htmlize.register(str)
# def _(text):
#     content = html.escape(text).replace('\n', '<br>\n')
#     return '<h1>{0}<h1>'.format(content)


def a(func):
    return 1


@a
def b():  # b = a(b)
    pass


if __name__ == '__main__':
    # print(main)
    # print(outer()())
    # print(outer2()())
    # print(outer5()())
    # snooze(1)
    # func()
    print(fibonacci(10))
    print(func3(100))
    # print(htmlize('asfd'))
