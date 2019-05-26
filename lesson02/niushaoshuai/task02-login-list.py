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
    username = input("\033[36mPlease input your username: \033[0m")
    password = input("\033[36mPlease input your password: \033[0m")
    if username == USERINFO[0] and password == USERINFO[1]:
        print("\033[32mLogin {} succ.\033[0m".format(username))
        while True:
            # 业务逻辑
            info = input("\033[36mPlease input userinfo: \033[0m")
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
                print("\033[32mAdd {} succ.\033[0m".format(info_list[1]))
            elif action == "delete" and len(info_list) >=2:
                username=info_list[1]
                for i in RESULT:
                    if i[0] == username:
                        j=RESULT.index(i)
                        del(RESULT[j])
                        print("\033[32mDel {} succ.\033[0m".format(username))
                        break
                else:
                    print('\033[31mDel {} fail.\033[0m'.format(username))
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
                print("\033[31minvalid action \033[0m")
    else:
        # 带颜色ex
        print('\033[31musername or password error,剩余{}次 \033[0m'.format(6-INIT_FAIL_CNT))
        #print("username or password error")
        INIT_FAIL_CNT += 1
print("\033[31m Input {} failed,Game Over.\033[0m".format(MAX_FAIL_CNT))
