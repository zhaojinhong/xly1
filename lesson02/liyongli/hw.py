# -*- coding:utf-8 -*-
# author: lyl

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
import getpass
import re

# 定义变量
RESULT = []
INIT_FAIL_CNT = 0
MAX_FAIL_CNT = 6

USERINFO = {
    '51reboot': {
        "password": "123456",
        "role": "admin"
    },
    '52reboot': {
        "password": "123456",
        "role": "user"
    }
}


FIELDS = ['username', 'age', 'tel', 'email']
RESULT.append(FIELDS)
phone_add = [134, 135, 136, 137, 138, 139, 147, 150, 151, 152, 157, 158, 159, 172, 178, 182, 183, 184, 187, 188, 198,
             130, 131, 132, 145, 155, 156, 166, 171, 175, 176, 185, 186, 133, 149, 153, 173, 177, 180, 181, 189, 191,
             199]
mail_pattern = re.compile(r'([a-zA-Z0-9]([a-zA-Z0-9_]+)(\@))[a-zA-Z0-9]([a-zA-Z0-9_]+)\.(([a-z]+))')


# 定义功能函数
# 检测用户登录
def check_user_login(user_name, pass_word):
    if user_name not in USERINFO.keys() or USERINFO[user_name]['password'] != pass_word:
        return False
    return True


# 检测用户登录
def check_user_permission(user_name):
    return USERINFO[user_name]['role']


# 检测用户是否存在
def check_user(name):
    for i in RESULT:
        if name == i[0]:
            return True
    return False


# 检查用户更新用户更新字段
def check_input(tag, check_world=None):
    return {
        'username': lambda: 0 if check_world is None else check_input_type(),
        'age': lambda: 1 if check_world is None else check_input_type(age=check_world),
        'tel': lambda: 2 if check_world is None else check_input_type(phone=check_world),
        'email': lambda: 3 if check_world is None else check_input_type(mail=check_world),
    }[tag]()


# 检查用户输入内容是否有误
def check_input_type(age=None, phone=None, mail=None):
    if age is not None:
        if not age.isdigit():
            return "年龄有误"
    if phone is not None:
        if len(phone) != 11:
            return "手机号有误"
        # 提取用户输入手机号的前三位,并转化为int类型
        head = int(''.join(list(phone[:3])))
        if head not in phone_add:
            return "手机号有误，暂不支持虚拟运营商！！！"
    if mail is not None:
        # 粗略写的正则，凑活着用
        m = mail_pattern.match(mail)
        if m is None:
            return "邮件格式有误 eg: xxx@xxx.com"
    return True


# 增加用户
def add(infolist, user_name):  # 之所以写infolist是因为如果定义成info_list 不符合PEP8规范
    # add monkey 12 13987654321 monkey@51reboot.com
    # 检测用户输入，长度必须为5，个字段分别为：动作、姓名、年龄、手机号、邮箱
    if check_user_permission(user_name) == 'user':
        return "permission denied"
    if len(infolist) != 5:
        return "输入有误，请检查输入内容 eg: add monkey 12 132xxx monkey@51reboot.com"
    tag = check_input_type(age=infolist[2], phone=infolist[3], mail=infolist[4])
    if tag is not True:
        return tag
    name = infolist[1]
    if check_user(name):
        return "添加失败{}已存在".format(name)

    RESULT.append(infolist[1:])
    return "用户{}添加成功".format(name)


# 删除用户
def delete(infolist, user_name):
    if check_user_permission(user_name) == 'user':
        return "permission denied"
    # delete monkey
    if len(infolist) != 2:
        return "输入有误，请检查输入内容 eg: delete monkey"
    name = infolist[1]
    if check_user(name):
        for i in range(len(RESULT)):
            if name == RESULT[i][0]:
                RESULT.remove(RESULT[i])
                return "用户{}删除成功".format(name)
    return "用户{}删除失败，无此用户".format(name)


# 更新用户
def update(infolist, user_name):
    # ['username', 'age', 'tel', 'email']
    # update monkey set age = 18
    if check_user_permission(user_name) == 'user':
        return "permission denied"
    if len(infolist) != 6 or infolist[2] != 'set' or infolist[3] not in ['username', 'age', 'tel', 'email'] or \
            infolist[4] != "=":
        return "输入有误，请检查输入内容 eg: update monkey set age = 18"

    tag = check_input(infolist[3], check_world=infolist[5])
    if tag is not True:
        return tag
    name = infolist[1]
    if check_user(name):
        for i in range(len(RESULT)):
            if name == RESULT[i][0]:
                result_tag = check_input(info_list[3])
                RESULT[i][result_tag] = infolist[5]
        return "用户{}更新成功".format(name)
    return "用户{}更新失败，无此用户".format(name)


while INIT_FAIL_CNT < MAX_FAIL_CNT:
    username = input("Please input your username: ")
    # 设置密码输入为非明文方式，IDE 下不可用,仍以明文显示
    password = getpass.getpass(prompt="Please input your password: ")
    login_tag = check_user_login(username, password)
    if login_tag:
        # 如果输入无效的操作，则反复操作, 否则输入exit退出
        while True:
            # 业务逻辑
            info = input("Please input your operation: ")
            # string -> list
            info_list = info.split()
            # 检测用户是否输入内容
            try:
                action = info_list[0]
            except IndexError:
                print("兄弟什么都不输入几个意思？")
                continue

            if action == "add":
                # 判断用户是否存在, 如果用户存在，提示用户已经存在， 不在添加
                result = add(info_list, username)
                print(result)
            elif action == "delete":
                # .remove
                result = delete(info_list, username)
                print(result)
            elif action == "update":
                result = update(info_list, username)
                print(result)
            elif action == "list":
                # 如果没有一条记录， 那么提示为空

                # print(RESULT)
                for x in RESULT:
                    print("{} {} {} {}".format(x[0], x[1], x[2], x[3]), end="\t")
                    print()
                    print("-" * 50)
            elif action == "find":
                pass
            elif action == "exit":
                sys.exit(0)
            else:
                print("invalid action.")
    else:
        # 带颜色
        print("username or password error.")
        INIT_FAIL_CNT += 1

print("\nInput {} failed, Terminal will exit.".format(MAX_FAIL_CNT))
