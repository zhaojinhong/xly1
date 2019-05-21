
def mp(list1):
    for x in range(len(list1) - 1): # 外层循环次数
        for y in range(len(list1) - x - 1):     # 优化循环次数代码，原因看下面注释。人类一思考，上帝就发笑！
            if list1[y] > list1[y + 1]: # 这里第y次循环已经把最大数挪到倒数第y位，所以接下来就不用去比较最后y位数大小
                list1[y] ,list1[y + 1] = list1[y + 1], list1[y]


list1 = [3, 7, 2, 5, 20, 11]
list2 = [100, 123, 4, 98, 43, 23, 45, 67, 76]
mp(list1)
mp(list2)
print(list1)
print(list2)

