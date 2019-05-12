# 需求：
#     输入6个数字
#     输出，求和
sum = 0
for i in range(5):
    sum += int(input("Please input number: "))
print(sum)


# 需求：
#     计算1到100的和
sum = 0
for i in range(100):
    sum += i + 1
print(sum)


# 需求：
#     输入n个数，知道输入0结束
sum = 0
while True:
    in1 = int(input("Please input number: "))
    if in1 == 0:
        break
    sum += in1
print(sum)

