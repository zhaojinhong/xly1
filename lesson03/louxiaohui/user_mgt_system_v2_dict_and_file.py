#!/usr/bin/env python
# **********************************************************
# * Author        : xoyabc
# * Email         : lxh1031138448@gmail.com
# * Last modified : 2019-05-27 22:46
# * Filename      : user_mgt_system_dict_and_file.py
# * Description   : 
# **********************************************************
'''
1. 登录认证；
2. 增删改查和搜索
    2.1 增 add           # add monkey 12 132xxx monkey@51reboot.com
    2.2 删 delete        # delete monkey
    2.3 改 update        # update monkey set age = 18
    2.4 查 list          # list
    2.5 搜 find          # find monkey
    2.6 分页显示         # display page 1 pagesize 5
3. 格式化输出
4. 数据结构：列表 -> 字典；
5. 文件持久化,数据存到文件中
6. 异常处理
7. PrettyTable 优雅的格式化输出
8. 扩展：导出csv(可写可不写)
'''

# 标准模块
import os
import sys
import json
from prettytable import PrettyTable


# 定义变量
RESULT = {}
TITLE= ['name', 'age', 'Tel', 'Email']
INIT_FAIL_CNT = 0
MAX_FAIL_CNT = 6
USERINFO = ("admin", "123456")
CHANCE_TIMES = 5

while INIT_FAIL_CNT < MAX_FAIL_CNT:
    username = input("Please input your username: ")
    password = input("Please input your password: ")
    if username == USERINFO[0] and password == USERINFO[1]:
        # 如果输入无效的操作，则反复操作, 直到输入exit退出
        while True:
            # 业务逻辑
            info = input("Please input the action and info: ")
            # string -> list
            info_list = info.split()
            # print(info)
            # print(info_list)
            # print (len(info_list))
            # define a dictionary named dict_info to store use info
            dict_info = {}
            # handle abnormal input,do not exit until input exit
            try:
                action = info_list[0]
            except IndexError:
                print("invalid input info,pls input again")
                continue
            # get the name
            if len(info_list) > 1:
                name = info_list[1]
            if action == "add":
                # check if input field is complete
                try:
                    dict_info['name'] = info_list[1]
                    dict_info['age'] = info_list[2]
                    dict_info['tel'] = info_list[3]
                    dict_info['email'] = info_list[4]
                except Exception as e:
                    print ("you forget input one or more field.")
                # add user if input field is complete
                else:
                    # check if name is already added to the system
                    flag = 0
                    for x in RESULT.keys():
                        if name == x:
                            flag += 1
                    if flag > 0:
                        print ("'{}' is already added" .format(" ".join(info_list[1:])))
                    else:
                        RESULT[info_list[1]] = dict_info
                        print ("add '{}' succeed" .format(" ".join(info_list[1:])))
                        print (RESULT)
            elif action == "save":
                # get the previous user data 
                try:
                    fd = open('user_info.txt', 'rU')
                    data = fd.read()
                except Exception as e:
                    continue
                else:
                    RESULT_DICT = json.loads(data, strict=False)
                    for k, v in RESULT_DICT.items():
                        for m in list(RESULT):
                            if k == m:
                                continue
                            else:
                                RESULT[k] = v
                finally:
                    fd.close()
                # store the user info to file
                fd = open('user_info.txt', 'w')
                try:
                    fd.write(json.dumps(RESULT))
                except Exception as e:
                    print ("Write error,errmsg: {}" .format(e))
                finally:
                    fd.close()
            elif action == "delete":
                # remove from RESULT if name exist
                flag = 0
                delete_list = []
                for x in RESULT:
                    if name in x[0]:
                        flag += 1
                        delete_list = x
                if flag > 0:
                    RESULT.remove(delete_list)
                else:
                    print ("user '{}' does not exist" .format(info_list[1]))
            elif action == "update":
                update_list = info.replace("="," ").split()
                ele = update_list[3]
                ele_value = update_list[4]
                # check if name is already added to the system
                flag = 0
                for x in RESULT:
                    if name in x[0]:
                        flag += 1
                        if ele == "age":
                            x[1] = ele_value
                        elif ele == "Tel":
                            x[2] = ele_value
                        elif ele == "Email":
                            x[3] = ele_value
                        else:
                            print ("invalid update field")
                if flag == 0:
                    print ("user '{}' does not exist" .format(info_list[1]))
            elif action == "list":
                xoy = PrettyTable()
                xoy.field_names = ['name', 'age', 'Tel', 'Email']
                if len(RESULT.keys()) > 0:    
                    for k, v in RESULT.items(): 
                        xoy.add_row([v['name'], v['age'], v['tel'], v['email']])
                    print(xoy)
                else:
                    print ("There is no user in system")
            elif action == "load":
                xoy = PrettyTable()
                xoy.field_names = ['name', 'age', 'Tel', 'Email']
                fd = open('user_info.txt', 'rU')
                data = fd.read()
                try:
                    RESULT_DICT = json.loads(data, strict=False)
                    for k, v in RESULT_DICT.items(): 
                        row_list = [v['name'], v['age'], v['tel'], v['email']]
                        xoy.add_row(row_list)
                    print(xoy)
                except Exception as e:
                    print ("There is no user in system")
                finally:
                    fd.close()
            elif action == "find":
                pass
                # check if name is already added to the system
                flag = 0
                ele_list = []
                for x in RESULT:
                    if name in x[0]:
                        flag += 1
                        ele_list = x
                if flag > 0:
                    print ("--------------------------------------------------------")
                    print ("|{:<10} |{:<3} |{:<13} |{:<20}" .format(TITLE[0],TITLE[1],TITLE[2],TITLE[3]))
                    print ("--------------------------------------------------------")
                    print ("|{:<10} |{:<3} |{:<13} |{:<20}" .format(ele_list[0],ele_list[1],
                                                 ele_list[2],ele_list[3]))
            elif action == "exit":
                sys.exit(0)
            else:
                print("invalid action.")
    else:
        # 带颜色
        print("\033[1;31m username or password error,you have {} times to input \033[0m" .format(CHANCE_TIMES))
        CHANCE_TIMES -= 1
        INIT_FAIL_CNT += 1

print("\n\033[1;31m Input {} times, all failed, Terminal will exit.\033[0m".format(MAX_FAIL_CNT))

