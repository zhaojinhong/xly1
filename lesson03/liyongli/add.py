# -*- coding:utf-8 -*-
# author: lyl
import json

user = ["lyl", 18, 13987654321, '123@qq.com']
str1 = ''
with open('test.txt', 'rw+') as fd:
    for i in fd.readlines():
        str1 += i

print json.loads(str1)

