# -*- coding: utf-8 -*-
# @Time    : 10/2/18 3:05 PM
# @Author  : Ian Leto
# @File    : Sorting_Algorithm.py
# 干啥的    : 各种排序算法

import unittest
import random


def swap(slist: list, i, j):
    slist[i], slist[j] = slist[j], slist[i]

# def checkone(func):
#     def check(*args):
#         if 2 == 1:
#             return 1
#         else:
#             func(*args)
#
#     return check

class SortAlgor:

    # def checkone(self, func):
    #     def check(*args):
    #         if 2 == 1:
    #             return 1
    #         else:
    #             func(*args)
    #
    #     return check

    def selection_sort(self, slist: list) -> list:
        """
        :param slist: 接受参数为ｌｉｓｔ
        :return: 排好序的ｌｉｓｔ
        最好情况　ｎ²
        最坏情况　ｎ²
        """
        i = 0
        while i < len(slist):
            minIndex = i
            j = i + 1
            while j < len(slist):
                if slist[minIndex] > slist[j]:
                    minIndex = j
                j += 1
            if minIndex != i:
                swap(slist, i, minIndex)
            i += 1

        return slist

    # @checkone
    def bubbleSort(self, slist: list) -> list:
        """
        :param slist: 接受参数为ｌｉｓｔ
        :return: 排好序的ｌｉｓｔ
        最好情况　n
        最坏情况　ｎ²
        """
        n = len(slist)
        while n > 1:
            swapped = False
            i = 1
            while i < n:
                if slist[i - 1] > slist[i]:                  # 如果后一项比前一项大
                    swap(slist, i, i - 1)                    # 则交换位置
                    swapped = True
                i += 1
            if not swapped:
                return slist
            n -= 1  # 　最后一项拍好了，所以ｌｉｓｔ长度－１

    def insertSort(self, slist: list) -> list:
        """
        :param slist: 接受参数为ｌｉｓｔ
        :return: 排好序的ｌｉｓｔ
        最好情况　n
        最坏情况　ｎ²
        """
        i = 1
        while i < len(slist):
            itemToInsert = slist[i]
            j = i - 1
            while j > 0:
                if slist[j] > itemToInsert:  # 如果　前一位比后一位大
                    slist[j + 1] = slist[i]    # 后一位值等于前一位
                    j -= 1
                else:
                    break

            slist[j + 1] = itemToInsert
            i += 1
        return slist


class TestAlgorithm(unittest.TestCase):

    sort_algorithm = SortAlgor()

    def testSort(self):
        for i in range(10):
            test_list = [random.randint(1, 30)
                         for i in range(random.randint(1, 20))]
            self.assertEqual(
                self.sort_algorithm.selection_sort(test_list),
                sorted(test_list))
            self.assertEqual(
                self.sort_algorithm.bubbleSort(test_list),
                sorted(test_list))
            self.assertEqual(
                self.sort_algorithm.insertSort(test_list),
                sorted(test_list))


def main():
    """

    :return:测试类
    """
    unittest.main()


if __name__ == '__main__':
    main()
