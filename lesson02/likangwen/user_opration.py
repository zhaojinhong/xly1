'''
1. 登录认证；
2. 增删改查和搜索
    2.1 增 add           # add monkey 12 132xxx monkey@51reboot.com
    2.2 删 delete        # delete monkey
    2.3 改 update        # update monkey set age = 18
    2.4 查 list          # list
    2.5 搜 find          # find monkey
3. 格式化输出

# 测试数据
add wen 12 10086 wen@hh.com
add lee 40 12345 lee@hh.com
'''

import sys
import getpass

# 定义变量
RESULT = []
INIT_FAIL_CNT = 0
MAX_FAIL_CNT = 6
USERINFO = ("admin", "123456")
# USERINFO = ("a", "a")
FIELDS = ['username', 'age', 'tel', 'email']
RESULT.append(FIELDS)

FORMAT = """
====================================================================
1.表字段格式
username age tel email
2. 增删改查和搜索
    2.1 增 add           # add monkey 12 132xxx monkey@51reboot.com
    2.2 删 delete        # delete monkey
    2.3 改 update        # update monkey set age = 18
    2.4 查 list          # list
    2.5 搜 find          # find monkey
====================================================================
"""

# 添加用户函数
def add(info_list):
    try:
        username = info_list[0]
    except Exception:
        return "\033[0m请输入正确格式\033[0m \n{}".format(FORMAT)
        # return "请输入正确格式"

    if username and len(info_list)==4:
        if username not in [u[0] for u in RESULT]:  # 检查用户是否不存在
            RESULT.append(info_list)
            return "{}用户添加成功".format(username)
        else:
            return "{}用户已存在，需要修改请使用update方法".format(username)
    else:
        return "参数有误，请输出正确参数"

# 删除用户函数
def delete(info_list):
    for user_list in RESULT:
        if user_list[0] == info_list[0]:
            FIELDS.pop(user_list)
            return "{}用户删除成功".format(info_list[0])
    return "删除失败，用户列表查无{}此用户".format(info_list[0])

# 修改用户函数
def update(info_list):
    for user_list in RESULT:
        if user_list[0] == info_list[0]:
            copy_user_list = user_list  # 拷贝一份
            location_index = info_list.index("=")   # 获取 = 在哪个位置
            key_name = info_list[location_index - 1]   # 获取要修改的参数，如age，username等
            if key_name in FIELDS:
                print(key_name)
                key_location = FIELDS.index(key_name)   # 获取要修改的参数在列表对应的位置
                user_list[key_location] = info_list[location_index + 1] # 修改参数
                RESULT[RESULT.index(copy_user_list)] = user_list
                return "{}用户修改成功".format(username)
            else:
                return "{}，无此字段参数".format(key_name)


    return "{}用户修改失败，用户列表查无此用户".format(username)

# 按需打印用户函数
def list(ret_list=None):
    if ret_list:
        # 此处给find调用，当传来的ret有序列，打印
        for user_list in ret_list:
            print("{:^10}\t{:^10}\t{:^10}\t{:^10}".format(user_list[0],user_list[1],user_list[2],user_list[3]))
    else:
        for user_list in RESULT:
            print("{:^10}\t{:^10}\t{:^10}\t{:^10}".format(user_list[0], user_list[1], user_list[2], user_list[3]))  # 格式限定符规定打印格式

# 查找用户函数
def find(info_list):
    find_list = []
    for user_list in RESULT:
        # 判断查找的用户是否存在于列表里
        if user_list[0] == info_list[0]:
            find_list.append(FIELDS)
            find_list.append(user_list)
            return find_list
    print("用户列表查无{}此用户".format(info_list[0]))

while INIT_FAIL_CNT < MAX_FAIL_CNT:
    username = input("Please input your username: ")
    password = input("Please input your password: ")
    # password = getpass.getpass("Please input your password: ")
    if username == USERINFO[0] and password == USERINFO[1]:
        # 提示增删改查操作
        print(FORMAT)
        while True:
            info = input("Please input your operation: ").lower()
            if not info:    # 当直接回车时不会报错
                continue
            info_list = info.split()

            try:    # 异常处理
                action = info_list.pop(0)
            except:
                pass

            if action == "add":
                ret = add(info_list)
                print(ret)
            elif action == "delete":
                ret = delete(info_list)
                print(ret)
            elif action == "update":
                ret = update(info_list)
                print(ret)
            elif action == "list":
                list(info_list)
            elif action == "find":
                ret = find(info_list)
                if ret:
                    list(ret)
            elif action == "exit":
                pass
            else:
                print("Syntax error")
                print(FORMAT)
    else:
        print("账号或密码错误")
        INIT_FAIL_CNT += 1

print("密码错误次数超过6次, 系统退出")