#!/usr/bin/python
'''
1. 登录认证；
2. 增删改查和搜索
    3.1 增 add           # add monkey 12 132xxx monkey@51reboot.com
    3.2 删 delete        # delete monkey
    3.3 改 update        # update monkey set age = 18
    3.4 查 list          # list
    3.5 搜 find          # find monkey
3. 格式化输出
'''
info = '''提示：
增: add monkey 12 132xxx monkey@51reboot.com
删: delete monkey
改: update monkey set age = 18
查: list
搜: find monkey
'''

import sys,os

# 定义变量
RESULT = []
INIT_FAIL_CNT = 0
MAX_FAIL_CNT = 6
USERINFO = ("test", "123")
FIELDS = ['username', 'age', 'tel', 'email']
RESULT.append(FIELDS)

def check_user(username,*args):
    for i in RESULT:
        if username == i[0]:
            global flag
            flag = True
            global inx
            inx = RESULT.index(i)
            return inx,flag
        else:
            pass
def add_user(info_list):
    while len(info_list) == 5:
        # 判断用户是否存在, 如果用户存在，提示用户已经存在， 不在添加
        check_user(info_list[1])
        if flag == False:
            RESULT.append(info_list[1:])
            # 打印结果信息
            return("\033[1;32mAdd {} succ.\033[0m\n".format(info_list[1]))
        else:
            return ("\033[5;31m{} already exists.\033[0m\n".format(info_list[1]))
    else:
        return("\033[1;31mInput Error！\033[0m\n\033[5;33;42mUsage: add [{}] [{}] [{}] [{}]\033[0m\n").format(FIELDS[0], FIELDS[1], FIELDS[2], FIELDS[3])
def del_user(info_list):
    while len(info_list) == 2:
        check_user(info_list[1])
        if flag:
            RESULT.pop(inx)
            return ("\033[5;31m{}\033[0m has been deleted.\n".format(info_list[1]))
            break
        else:
            return "\033[5;31m{} does not exist.\033[0m\n".format(info_list[1])
    else:
        return ("\033[1;31mInput Error！\033[0m\n\033[5;33;42mUsage: delete | del [{}]\033[0m\n").format(FIELDS[0])
def find_info(info_list):
    while len(info_list) == 2:
        check_user(info_list[1])
        if flag:
            print("|{} |{} |{} |{}|\n".format(FIELDS[0].ljust(10), FIELDS[1].ljust(3), FIELDS[2].ljust(11),FIELDS[3].ljust(20), end="\t"))
            print("|{} |{} |{} |{}|".format(RESULT[inx][0].ljust(10),RESULT[inx][1].ljust(3),RESULT[inx][2].ljust(11),RESULT[inx][3].ljust(20), end="\t"))
            break
        else:
            return "\033[1;31;43m{} does not exist!\033[0m\n".format(info_list[1])
    else:
        return("\033[1;31mInput Error！\033[0m\n\033[5;33;42mUsage: find [{}]\033[0m\n").format(FIELDS[0])
def update_info(info_list):
    while len(info_list) == 6:
        check_user(info_list[1])
        if flag and info_list[3] in FIELDS:
            iny = FIELDS.index(info_list[3])
            RESULT[inx][iny] = info_list[5]
            return "{} {} was changed to {}.".format(info_list[1],info_list[3],info_list[5], end="\t")
            break
        if info_list[3] not in FIELDS:
            return "\033[1;31;43m{} does not exist!\033[0m\n".format(info_list[3])
        else:
            return "\033[1;31;43m{} does not exist!\033[0m\n".format(info_list[1])
    else:
        return("\033[1;31mInput Error！\033[0m\n\033[5;33;42mUsage: update [{}] set [ {}|{}|{} ] = [ Target field ]\033[0m\n").format(FIELDS[0],FIELDS[1],FIELDS[2],FIELDS[3])

while INIT_FAIL_CNT < MAX_FAIL_CNT:
    username = input("Please input your username: ")
    password = input("Please input your password: ")
    if username == USERINFO[0] and password == USERINFO[1]:
        print("\033[1;36mLogin Suceesfully.\033[0m")
        # 如果输入无效的操作，则反复操作, 否则输入exit退出
        while True:
            flag = False
            # 业务逻辑
            info = input("\033[1;35mPlease input your operation: \033[0m")
            # string -> list
            info_list = info.split()
            action = info_list[0]
            if action == "add":
                res = add_user(info_list)
                print(res)
            elif action == "delete" or action == "del":
                # .remove
                res = del_user(info_list)
                print(res)
            elif action == "find":
                res = find_info(info_list)
            elif action == "update":
                res = update_info(info_list)
                print(res)
            elif action == "list":
                # 如果没有一条记录， 那么提示为空
                if (len(RESULT)) == 1:
                    print("\033[1;31;43mEmpty.Please add user information!\033[0m")
                else:
                    for i in RESULT:
                        #定义字符串长度为?，字符对齐到左边，默认填充空格
                        print("|{} |{} |{} |{}|".format(i[0].ljust(10), i[1].ljust(3), i[2].ljust(11), i[3].ljust(20)), end="\t")
                        print()
                        print("-".ljust(52,'-'))
            elif action == "exit":
                sys.exit(0)
            else:
                print("invalid action.")
    else:
        # 带颜色
        print("\033[5;31;43musername or password error.\033[0m")
        INIT_FAIL_CNT += 1



print("\nInput {} failed, Terminal will exit.".format(MAX_FAIL_CNT))