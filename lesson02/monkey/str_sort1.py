s = "68301897889713"

'''
1. string -> list
2. list.sort()
3. list -> string
string
'''

data = []

for x in s:
    data.append(x)

print(data)

datasort = data.sort()
print(data)

rets = ""
for x in data:
    rets = rets + x
print(rets)



