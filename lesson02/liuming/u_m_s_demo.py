#!/usr/bin/env python
# -*-encoding:utf-8-*-
# -------------------------------------------------------------------------------
# Name:         u_m_s_demo.py
# Description:  Simple version of user management system
# Author:       Aaron
# Date:         2019/5/19
# -------------------------------------------------------------------------------
"""
需求
1. 登录认证；
2. 增删改查和搜索
    3.1 增 add           # add monkey 12 132xxx monkey@51reboot.com
    3.2 删 delete        # delete name
    3.3 改 update        # update index=new_value
    3.4 查 list          # list
    3.5 搜 find          # find index or [start:stop:step]
3. 格式化输出
"""

from utils import DataOperate

# 定义变量
MAX_FAIL_CNT = 6
USERINFO = ("liuming", "1")
data_operate = DataOperate()

while MAX_FAIL_CNT:
    username = input("\033[36mPlease input your username: \033[0m")
    password = input("\033[36mPlease input your password: \033[0m")
    if username == USERINFO[0] and password == USERINFO[1]:
        # 如果输入无效的操作，则反复操作, 否则输入exit退出
        while True:
            # 业务逻辑
            info = input("\033[36mPlease input what do u wanna do: \033[0m").strip()
            try:
                # string -> list
                info_list = info.split()

                # print(info)
                # print(info_list)
                action = info_list[0]
            except IndexError:
                continue

            if action == "add":
                data_list = info_list[1:]
                getattr(data_operate, action)(data_list)
            elif action == "delete":
                data_list = info_list[1:]
                getattr(data_operate, action)(data_list)
            elif action == "update":
                where_update = [tuple(i.split("=")) for i in info_list[1:]]
                getattr(data_operate, action)(where_update)
            elif action == "list":
                getattr(data_operate, action)()
            elif action == "find":
                index_list = [int(i) for i in info_list[1:]]
                getattr(data_operate, action)(*index_list)
            elif action == "exit":
                break
            else:
                print("invalid action.")
    else:
        print("\033[31musername or password error.\033[0m")
        MAX_FAIL_CNT -= 1


print("\033[31m\nYou tried too many times, Terminal will exit.\033[0m")
