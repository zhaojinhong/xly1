#冒泡排序
my_list = [3,6,1,2,7,9,5]
for i in range(len(my_list)-1):
    for j in range(len(my_list)-1):
        if my_list[j] > my_list[j+1]:
            tmp = my_list[j]
            my_list[j] = my_list[j+1]
            my_list[j+1] = tmp
print(my_list)
