'''
冒泡排序
需求：
- [3, 7, 2, 5, 20, 11]

将列表通过冒泡排序的方式实现排序。
'''

list = [3, 7, 2, 5, 20, 11]
num1 = 0

while num1 < len(list):
	num = 0
	while num < len(list)-1:
		if list[num] >= list[num+1]:
					x = list[num]
					list.pop(num)
					list.insert(num+1,x)
		else:
			num += 1
	num1 += 1
print(list)
