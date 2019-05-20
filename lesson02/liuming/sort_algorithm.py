#!/usr/bin/env python
# -*-encoding:utf-8-*-
# -------------------------------------------------------------------------------
# Name:         sort_algorithm.py
# Description:  
# Author:       Aaron
# Date:         2019/5/20
# -------------------------------------------------------------------------------
"""
初级排序三人组之冒泡排序
思想：
1、for循环无序数列，对比相邻俩个数的大小，并交换俩个数的位置；
2、对每一对相邻的数循环做该操作，最终得出无序数列中最值放到数列末尾； 此时无序列表的元素可以分为无序区间和有序区间；
3、对无序区间的元素重复上面的操作，每循环一次上面的操作，无序区间减少1个元素，有序区间加1元素，
4、重复以上操作，无序区间的元素为0，则排序结束，得到有序序列.
"""


# 简单版冒泡排序，时间复杂度：O(n^2)
def bubble_sort(data_list):
    """
    :param data_list:  unordered list  --> [5,8,7,1]
    :return: ordered list  --> [1,5,7,8]
    """
    for i in range(len(data_list)-1):
        for j in range(len(data_list)-i-1):
            if data_list[j] > data_list[j+1]:
                data_list[j], data_list[j+1] = data_list[j+1], data_list[j]


if __name__ == "__main__":
    import time
    import random

    start_time = time.time()
    unordered_list = [random.randint(0, 100) for i in range(18)]
    bubble_sort(unordered_list)
    print("\033[36m排序结果: {}\033[0m".format(unordered_list))
    print("\033[36m耗时: {}\033[0m".format(time.time()-start_time))