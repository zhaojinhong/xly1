lis = [3, 7, 2, 5, 20, 11]
print (lis)

count=len(lis)
for i in range(0,count):
    for j in range(i+1,count):
        if lis[i]>lis[j]:
            lis[i],lis[j]=lis[j],lis[i]
print(lis)
