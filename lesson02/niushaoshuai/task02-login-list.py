# task02模拟登陆-列表实现方式
"""
Created on May 21th 20:20:52 2019
Modify1 on May 22th 16:49:30 2019
@author: Owen.Niu
"""

# 标准模块
import os

# 定义变量
RESULT = []
INIT_FAIL_CNT = 1
MAX_FAIL_CNT = 6
USERINFO = ("51reboot","123456")

while INIT_FAIL_CNT <= MAX_FAIL_CNT:
    username = input("Please input your username: ")
    password = input("Please input your password: ")
    if username == USERINFO[0] and password == USERINFO[1]:
        print("\033[1mLogin {} succ.".format(username))
        print('\033[0m')
        while True:
            # 业务逻辑
            info = input("Please input userinfo: ")
            info_list = info.split()
            ## 输入过滤器
            if len(info_list) == 3:
                action = info_list[0]
                username = info_list[1]
                password = info_list[2]
            elif len(info_list) == 2:
                action = info_list[0]
                username = info_list[1]
            else:
                action = info_list[0]

            if action == "add" and len(info_list) >=2:
                RESULT.append(info_list[1:])
                print("\033[1mAdd {} succ.".format(info_list[1]))
                print('\033[0m')
            elif action == "delete" and len(info_list) >=2:
                username=info_list[1]
                for i in RESULT:
                    if i[0] == username:
                        j=RESULT.index(i)
                        del(RESULT[j])
                        print("\033[1mDel {} succ.".format(username))
                        print('\033[0m')
                        break
                else:
                    print('\033[35mDel {} fail.'.format(username))
                    print('\033[0m')
            elif action == "update" and len(info_list) > 2:
                username=info_list[1]
                password=info_list[2]
                for i in RESULT:
                    if i[0] == username:
                        i[1] = password
                        
            elif action == "list":
                print(RESULT)
            elif action == "exit":
                break
            else:
                print("\033[35minvalid action")
                print('\033[0m')
    else:
        # 带颜色ex
        print('\033[35musername or password error,剩余{}次'.format(6-INIT_FAIL_CNT))
        print('\033[0m')
        #print("username or password error")
        INIT_FAIL_CNT += 1
print("\nInput {} failed,Game Over.".format(MAX_FAIL_CNT))
