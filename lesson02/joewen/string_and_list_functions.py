# -*- coding: utf-8 -*-
# @Time    : 2019-05-18 12:41
# @Author  : Joe
# @Site    : 
# @File    : string_and_list_functions.py
# @Software: PyCharm
# @function: xxxxx

print(dir(str))

for i in dir(str):
    print(i)

my_str = 'abcdabcd'

# 第一个字母大写
print(my_str.capitalize())
# 统计字符a在my_str里面出现的次数
print(my_str.count('a', 0, len(my_str)))




