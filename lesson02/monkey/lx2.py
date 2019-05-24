

retdata = [5, 12, 32, 4, 2, 10, 25]

max_value = 0

for x in retdata:
    if x > max_value:
        max_value = x

print(max_value)

'''
 6 = 6 // 2 + 1
 4before
 
 7 = 7 // 2 + 1
 4before
'''


index = len(retdata) // 2 + 1
retdata.insert(index, max_value)


print(retdata)

