# -*- coding: utf-8 -*-

import random

a = 69

for i in range(6):
    if random.randint(0,100) > a:
        print("大了")
    if random.randint(0,100) < a:
        print("小了")
    else:
        print("对了")

