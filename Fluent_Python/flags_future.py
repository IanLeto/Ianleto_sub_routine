# -*- coding: utf-8 -*-
# @Time    : 2018/9/30 9:25
# @Author  : Ian Leto
# @File    : flags_future.py
# 干啥的    : future 使用
import os
import time
import sys
import requests
from Python_Data_Structure.Decorator_For_Time import clock2


a = ('CN IN US ID PK ET MX CD TR IR '' ET EG FR').split()
BASE_URL = 'http://flupy.org/data/flags'
DEST_DIR = 'D:/'


def save_flag(img, filename):
    """
    保存文件
    :param img: 图片的字节序列
    :param filename: 文件名
    :return:
    """
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(img)


def get_flag(cc):
    """
    发送请求的函数
    :param cc:
    :return: 响应体原文
    """
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
    res = requests.get(url)
    return res.content


def show(text):
    """

    :param text:
    :return:
    """
    print(text)
    sys.stdout.flush()


def download_many(cc_list):
    """
    与并发实现比较的函数
    :param cc_list:国籍字符串
    :return:
    """
    for cc in sorted(cc_list):
        img = get_flag(cc)
        show(cc)
        save_flag(img, cc.lower() + '.gif')
    return len(cc_list)


def main(download_many):
    t0 = time.time()
    count = download_many(a)
    elapsed = time.time() - t0
    msg = '\n{} flags download in {:.2f}s'
    print(msg.format(count, elapsed))


MAX_WORKERS = 20


def download_one(cc):
    """
    下载一个图片的函数,在各个线程中执行的函数
    :param cc:国籍字符串
    :return:
    """
    img = get_flag(cc)
    show(cc)
    save_flag(img, cc.lower() + '.gif')
    return cc


from concurrent import futures


def download_many_by_future(cc_list):
    """

    :param cc_list:需要下载的国籍list
    :return:
    """
    # workers 为该工作创建的线程数量
    # MAX_WORKERS 允许创建的最大线程
    # 需要创建的线程数量
    workers = min(MAX_WORKERS, len(cc_list))
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(download_one, sorted(cc_list))
    return len(list(res))


# @test_time
def xx():
    return 1


if __name__ == '__main__':
    # main(download_many=download_many)
    main(download_many=download_many_by_future)
    print(xx())
