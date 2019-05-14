#Filename : 9x9.py
#author by: Thomas.Wu
#v1 from  for 
for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(j, i, i*j), end='')
    print()
