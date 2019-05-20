


l1 = [1, 2, 5, 7, 11, 11, 2, 3, 1]
l2 = []

for x in l1:
    if l1.count(x) >= 2:
        if x not in l2:
            l2.append(x)


print(l2)


