#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-30 10:09:53
# @Author  : IanLeto (ccssliu@163.com)
# @Link    : ccssliu@163.com
# @Version : $Id$
# usage: 测试python类等
from datetime import date, timedelta, datetime


class Person():
    """
        顶层person

    """

    create_date = datetime.now()
    # 外界对这个人的评价,不应该出现在inti方法中
    label = []

    def __init__(self, race: str, faith: str, age: date, name: str, job=None, pay=0) -> None:
        self.race = race
        self.faith = faith
        self.name = name
        self.job = job
        self.pay = pay
        # 计算年龄
        if isinstance(age, date):
            today = date.today()
            if age.month < today.month:
                self.age = today.year - age.year
            else:
                self.age = today.year - age.year - 1
        else:
            self.age = age

    # 开始封装last_name
    def getLastname(self):
        return self.name.split()[-1]

    # as a person 难免会被打上不同的标签
    def setLable(self, word: str):
        keyword = ['time']
        if isinstance(word, str):
            self.label.extend(word.split())
        elif isinstance(word, dict):
            for k in word:
                if k in keyword:
                    self.label.append(word[k])
        else:
            raise IOError

    # 打印实例的时候,我们不想看到她对应的内存地址,因为这毫无意义
    # so 我们使用__str__来让她好看些
    def __str__(self):
        return 'Person: %s' % self.name


class PornStar(Person):
    # PornStar 不宜以真实姓名示人(希望仁义廉耻能够继续下去)
    # so 我们应该重写其方法
    # example-1
    # 不易于维护的方法,但我很好奇,哪个沙雕会这样写代码
    category = []

    def setLable(self, word: str):
        keyword = ['time']
        if isinstance(word, str):
            self.label.extend(word.split())
        elif isinstance(word, dict):
            for k in word:
                if k in keyword:
                    self.label.append(word[k])
        # 为了加上这段代码,我们copy了整个setLable方法
        if self.category:
            self.label.extend(self.category)
        else:
            raise IOError

    def setLable(self):
        pass

    if __name__ == '__main__':
        aragaki = Person(race='Asia', faith='', name='Aragaki Yui',
                         age=date(1988, 6, 11), job='Shine Star')
        # 此时,我们要获取gakki的lastname
        aragaki_last_name = aragaki.name.split()[-1]
        print(aragaki_last_name)
        # 然鹅,我们发现,如果接下来要取gakki的fistname作为lastname(总之就是取值方法变了,比如aragaki.name.split()[-1] + '<<>>')
        # 但是,这段代码已经被无数个类调用了,(毕竟云老婆(〃'▽'〃))
        # 我们就需要改写这段代码, 在emabc是就发现,这是一件大工程
        # 如果getlastname 作为一个方法()在类内,岂不是很 van ♂ 美
        # 这个()里面填的词,就是 >>封装<<

        # 就是tmd这么简单
        print(aragaki.getLastname(), '\n', aragaki)
        aragaki.setLable({'time': 'not enough'})
        aragaki.setLable('cute brave')
        print(aragaki.label)

nums= list(range(1,2))
def function(k, nums):
    i = 0
    while i < k:
        nums.insert(0, nums.pop())
        i += 1
    return nums

print(function(0,nums))
