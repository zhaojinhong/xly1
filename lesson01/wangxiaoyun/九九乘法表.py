#!/usr/bin/python36
#-*- coding: utf-8 -*-
#九九乘法表
for i in range(1,10):
    for j in range(1,10):
        sum = i * j
        if i >= j:
          print('%d * %d = %d' % (i,j,sum),end='  ')
    print ('')

#1+2+3+...+100
sum = 0
for i in range(1,101):
    sum = sum + i
print(sum)