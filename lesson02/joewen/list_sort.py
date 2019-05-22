# -*- coding: utf-8 -*-
# @Time    : 2019-05-22 11:51
# @Author  : Joe
# @Site    : 
# @File    : list_sort.py
# @Software: PyCharm
# @function: xxxxx

random = [(2, 2), (3, 4), (4, 1), (1, 3)]


def takesecond(element):
    print(element[1])
    return element[1]


random.sort(key=takesecond)

print(random)
