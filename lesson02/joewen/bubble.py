# -*- coding: utf-8 -*-
# @Time    : 2019-05-18 12:48
# @Author  : Joe
# @Site    : 
# @File    : bubble.py
# @Software: PyCharm
# @function: xxxxx


my_list = [9, 8, 0, 1, 5, 7, 3]

# new_list = sorted(my_list)
# print(new_list)

for i in range(len(my_list)):
    # print(i, my_list[i])
    for j in range(0, len(my_list)-i-1):
        if my_list[j] > my_list[j+1]:
            my_list[j+1], my_list[j] = my_list[j], my_list[j+1]

print(my_list)


