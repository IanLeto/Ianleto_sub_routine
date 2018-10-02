# -*- coding: utf-8 -*-
# @Time    : 2018/9/21 16:07
# @Author  : Ian Leto
# @File    : abc_class.py
# 干啥的    : 自定义一个抽象基类
import abc
import random
from collections import UserDict


class Tombola(abc.ABC):

    @abc.abstractmethod
    def load(self, iterable):
        """
        :param iterable:
        :return:
        """

    @abc.abstractmethod
    def pick(self):
        """
        :return:
        """

    def loaded(self):
        return bool(self.inspect())

    # 在基类中的具体方法,只能使用抽象基类中的其他方法or特性
    def inspect(self):
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))

    def __setitem__(self, key, value):
        pass


class BingCage(Tombola):

    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        # 委托load方法进行初始加载
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingCage')

    def __call__(self):
        self.pick()

    def __setitem__(self, key, value):
        pass


class DoppelDict(dict):

    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)


class A():

    def __init__(self):
        self.a = '1'

    def __setitem__(self, key, value):
        self.__dict__[key] = [value] * 2


class DoppelDict2(UserDict):

    def __setitem__(self, key, value):
        print('{},{}'.format(key, value))
        super().__setitem__(key, value)


if __name__ == '__main__':
    b = BingCage([1, 3])
    b._items = [11, 33]
    print(b._items)
    a = A()
    print(a.a)
    aaa = DoppelDict2(k=1)

