'''
需求：
打印乘法口诀
'''
# Version1
for i in range(1,10):
    for j in range(1,i+1):
        print("%d * %d = %2d" % (j,i,j*i),end='  ')
    print('')

# Version2
i = 1
while i < 10:
    for j in range(1,i+1):
        print("%d * %d = %2d" % (j,i,j*i),end='  ')
    print('')
    i = i + 1
