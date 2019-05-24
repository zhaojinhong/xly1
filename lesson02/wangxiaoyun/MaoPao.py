#!/usr/local/python36/bin/python3.6
#-*- coding: utf-8 -*-
#冒泡排序
L = [3, 7, 2, 5, 20, 11]
for i in range(len(L)-1):
    for j in range(len(L)-1-i):
        if L[j] > L[j+1]:
            L[j],L[j+1] = L[j+1],L[j]
print(L)
