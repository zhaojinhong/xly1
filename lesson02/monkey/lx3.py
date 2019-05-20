l1 = [1, 2, 3]

l2 = [4, 5, 6]

# [1, 4, 2, 5, 3, 6]

l3 = []
#
# cnt = 0
#
# while cnt < len(l1):
#     l3.append(l1[cnt])
#     l3.append(l2[cnt])
#     cnt += 1
#
# print(l3)


for i in range(0, len(l1)):
    # l3.append(l1[i])
    # l3.append(l2[i])
    l3.extend([l1[i], l2[i]])
print(l3)

# for i in l1:
#     for j in l2:
#         l3.append(i)
#         l3.append(j)
#
# print(l3)

'''
for x in l2:
    l1.append(x)

print(l1)
'''
