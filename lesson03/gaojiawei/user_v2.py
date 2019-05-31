"""
1. 登录认证；
2. 增删改查和搜索
    3.1 增 add           # add monkey 12 132xxx monkey@51reboot.com
    3.2 删 delete        # delete monkey
    3.3 改 update        # update monkey set age = 18
    3.4 查 list          # list
    3.5 搜 find          # find monkey
3. 格式化输出
"""


# 标准模块
import sys
import json
import datetime
import csv
from prettytable import PrettyTable

# 定义变量
RESULT = {}
INIT_FAIL_CNT = 0
MAX_FAIL_CNT = 6
USERINFO = ("51reboot", "123456")
FILENAME = "51reboot.txt"

def help_info():
    info = {
        '增' : 'add monkey 12 132xxx monkey@51reboot.com',
        '删' : 'delete monkey',
        '改' : 'update monkey set age = 18',
        '查' : 'list',
        '搜' : 'find monkey',
        '存' : 'save',
        '读' : 'load',
        '分' : 'display page 1 pagesize 5',
        '退' : 'exit',
        '帮' : 'help'
    }
    for k,v in info.items():
        print(k,v)


def display(info_list):
    xtb = PrettyTable()
    xtb.field_names = ["username", "age", "tel", "email"]
    info = []
    for k, v in RESULT.items():
        tmp_info = RESULT[k].values()
        tmp_info = list(tmp_info)
        info.append(tmp_info)
    page = int(info_list[2])
    line = int(info_list[-1])
    start = (page - 1) * line
    end = line * page

    for x in info[start:end]:
        xtb.add_row(x)
    print(xtb)


def add(info_list):
        username = info_list[1]
        dic_info = {"name": info_list[1], "age": info_list[2], 'tel': info_list[3], 'email': info_list[4]}

        if username not in RESULT:
            RESULT[username] = dic_info
            print("Add {} succ.".format(info_list[1]))

        else:
            print("Add {} failure .{} existing .".format(info_list[1], info_list[1]))


def delete(info_list):
    cur_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    username = info_list[1]
    if username not in RESULT:
        print("User {} not found.".format(username))
    else:
        del RESULT[username]
        print("[DEBUG] {} {}".format(cur_time, info))


def update(info_list):
    username = info_list[1]
    upinfo = info_list[3]
    nupinfo = info_list[-1]
    try:
        if username not in RESULT:
            print(' A null value.')
        else:
            RESULT[username][upinfo] = nupinfo
            print('update {} succ.'.format(username))
    except Exception as e:
        print(e)


def mylist():
    if len(RESULT) < 1:
        print('A null value.')
    else:
        xtb = PrettyTable()
        xtb.field_names = ["username", "age", "tel", "email"]
        info = []
        for k, v in RESULT.items():
            tmp_info = RESULT[k].values()
            tmp = list(tmp_info)
            info.append(tmp)

        for x in info:
            xtb.add_row(x)
        print(xtb)


def find(info_list):
    username = info_list[1]
    if username not in RESULT:
        print(' A null value.')
    else:
        xtb = PrettyTable()
        xtb.field_names = ["username", "age", "tel", "email"]
        info = []

        tmp_info = RESULT[username].values()

        tmp_info = list(tmp_info)

        info.append(tmp_info)
        for x in info:
            xtb.add_row(x)
        print(xtb)


def save():
    # save
    # 1. 打开文件 file describe
    fd = open(FILENAME, 'w')

    # 2. 操作文件 read / write
    fd.write(json.dumps(RESULT))

    # 3. 关闭文件
    fd.close()

    print("Save file:{} succ.".format(FILENAME))


def load():
    try:
        # 1. 打开文件 file describe
        fd = open(FILENAME, 'r')
        # 2. 操作文件 read / write
        data = fd.read()
        RESULT = json.loads(data)
        # 3. 关闭文件
        print(RESULT)
        fd.close()

    except Exception as e:
        print(e)


def main():
    INIT_FAIL_CNT = 0
    MAX_FAIL_CNT = 6
    while INIT_FAIL_CNT < MAX_FAIL_CNT:
        username = input("Please input your username: ")
        password = input("Please input your password: ")
        if username == USERINFO[0] and password == USERINFO[1]:
            # 如果输入无效的操作，则反复操作, 否则输入exit退出

            while True:
                # 业务逻辑
                try:
                    info = input("Please input your operation: ")
                    # add monkey1 12 13987654321 monkey@51reboot.com
                    # string -> list
                    info_list = info.split()
                    # print(info)
                    # print(info_list)
                    action = info_list[0]
                except Exception as e:
                    print(e)

                else:
                    if action == "add":
                        add(info_list)
                    elif action == "delete":
                        delete(info_list)
                    elif action == "update":
                        update(info_list)
                    elif action == "list":
                        mylist()
                    elif action == "find":
                        find(info_list)
                    elif action == "save":
                        save()
                    elif action == "load":
                        load()
                    elif action == "display":
                        display(info_list)
                    elif action == "exit":
                        sys.exit(0)
                    elif action == 'help':
                        help_info()
                    else:
                        print("invalid action.")
        else:
            # 带颜色
            print("musername or password error.")
            INIT_FAIL_CNT += 1

    print("\nInput {} failed, Terminal will exit.".format(MAX_FAIL_CNT))


if __name__ == '__main__':
    main()
