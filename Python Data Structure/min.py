#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-22 09:58:46
# @Author  : IanLeto (ccssliu@163.com)
# @Link    : ccssliu@163.com
# @Version : $Id$
# min

import unittest
import random


class TestF(unittest.TestCase):

    def test_min_index(self):
        for i in range(30):
            test_list = [random.randint(1, 30)
                         for i in range(random.randint(1, 200))]
            self.assertEqual(index_of_min(test_list), min(test_list))

    def test_sequential_search(self):
        for i in range(30):
            test_list = [random.randint(1, 30)
                         for i in range(random.randint(1, 200))]
            target = random.randint(1, 30)
            self.assertEqual(seqsearch(target, test_list), target in test_list)

    def test_binary_search(self):
        for i in range(30):
            test_list = [random.randint(1, 30)
                         for i in range(random.randint(1, 200))]
            target = random.randint(1, 30)
            self.assertEqual(binarySearch(target, test_list),
                             test_list.index(target))


def index_of_min(list_test: list):
    min_index = 0
    current_index = 1
    while current_index < len(list_test):
        if list_test[current_index] < list_test[min_index]:
            list_test[min_index] = list_test[current_index]
        current_index += 1
    return list_test[min_index]


def seqsearch(target, tlist):
    position = 0
    while position < len(tlist):
        if target == tlist[position]:
            return True
        position += 1
    return False


def binarySearch(target, tlist: list):
    left = 0
    right = len(tlist) - 1
    while left <= right:
        midpoint = (left + right) // 2
        if target == tlist[midpoint]:
            return tlist.index(target)
        elif target < tlist[midpoint]:
            right = midpoint - 1
        else:
            left = midpoint - 1
    return False


if __name__ == '__main__':
    unittest.main()
