#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
1: 打印乘法口诀
提示：尝试print(‘monkey’)与print(‘monkey’, end=‘’)的区别
'''

num_list = [1,2,3,4,5,6,7,8,9]

for x in num_list:
    print('\n')
    for y in num_list:
        res = x * y
        print(('{}x{}={} ').format(x,y,res),end='')

'''
for x in range(1,10):
    print('\n')
    for y in range(1,10):
        res = x * y
        print(('{}x{}={} ').format(x,y,res),end='')
'''





