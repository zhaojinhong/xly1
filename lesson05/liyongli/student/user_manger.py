# -*- coding:utf-8 -*-
# author: lyl

from prettytable import PrettyTable

from models import student

FIELDS = ['id', 'username', 'age', 'phone', 'email']


def addUser(args):
    '''
    add monkey1 12 132xxx monkey1@qq.com
    '''
    user_info_list = args.split(" ")
    if len(user_info_list) != 4:
        print("addUser failed, args length != 4")
        return

    username = user_info_list[0]
    try:
        student.select().where(student.username == username).get()
        print("{} 已存在".format(username))
        return
    except:
        RESULT = {
            'username': username,
            'age': user_info_list[1],
            'phone': user_info_list[2],
            'email': user_info_list[3],
        }
        try:
            student.insert(RESULT).execute()
            print("add user {} secc.".format(username))
        except Exception as e:
            print(e)


def deleteUser(args):
    '''
    delete monkey1
    args = monkey1
    :param args:
    :return:
    '''

    user_info_list = args.split(" ")
    if len(user_info_list) != 1:
        print("deleteUser failed, args length != 1")
        return

    username = args
    try:
        tag = student.delete().where(student.username == username).execute()
        if tag:
            print("delete user {} secc.".format(username))
        else:
            print("Username: {} not found.".format(username))
    except Exception as e:
        print(e)


def updateUser(args):
    '''
    update monkey1 set age = 20
    :param args: monkey1 set age = 20
    :return:
    '''

    user_info_list = args.split()
    if len(user_info_list) != 5:
        return "updateUser failed, args length != 5"

    where = user_info_list[1]
    symbol = user_info_list[-2]

    if where != 'set' or symbol != '=':
        return 'syntax error.'
    else:
        username = user_info_list[0]
        where_field = user_info_list[2]
        update_value = user_info_list[-1]
        result = findUser(username, tag=True)
        if not result:
            return
        try:
            tag = student.update({where_field: update_value}).where(student.username == username).execute()
            # 检查用户更新值是否与原值相同
            if tag:
                print("user {} update secc".format(username))
            else:
                print("兄弟你这也没更新啊！！")
        except Exception as e:
            print(e)


def listUser():
    '''
    打印所有用户信息
    :return:
    '''
    # 查询数据库全部信息
    user_data = student.select()
    # 将数据转化为列表
    user_list = [user_data[values].__data__.items() for values in range(len(user_data))]

    xtb = PrettyTable()
    xtb.field_names = FIELDS
    # 设置字段左对齐
    xtb.align = 'l'
    for v in user_list:
        # 强制转化为字典
        xtb.add_row(dict(v).values())
    print(xtb)


def findUser(args, tag=None):
    # 有个bug 暂时没考虑模糊查询
    username = args
    user_data = student.select().where(student.username == username)
    if len(user_data):
        user_dict = dict(user_data[0].__data__.items())
        xtb = PrettyTable()
        xtb.field_names = FIELDS
        xtb.add_row(user_dict.values())
        # tag 非None才打印
        if not tag:
            print(xtb)
        result = True
    else:
        print("Username: {} not found.".format(username))
        result = False

    if tag:
        return result

def displayUser(args):
    '''
    display page 2 pagesize 5
    :param args: page 2 pagesize 5 ;default pagesize = 5
    page 1 -> 0-4
    切片
    slice
    '''
    try:
        user_data = student.select()
        values = [user_data[values].__data__.items() for values in range(len(user_data))]
        xtb = PrettyTable()
        xtb.field_names = FIELDS
        # 设置字段左对齐
        xtb.align = 'l'
    except Exception as e:
        print(e)
        return

    user_info_list = args.split()
    if len(user_info_list) == 2:
        if user_info_list[0] != 'page':
            print("syntax error.")
            return

        page_value = int(user_info_list[1]) - 1  # 1
        pagesize = 5
        start = page_value * pagesize
        end = start + pagesize

        for t_user_info in values[start:end]:
            xtb.add_row(dict(t_user_info).values())
        print(xtb)

    elif len(user_info_list) == 4:
        if user_info_list[0] != 'page' and user_info_list[-2] != 'pagesize':
            print("syntax error.")
            return

        page_value = int(user_info_list[1]) - 1
        pagesize = int(user_info_list[-1])
        start = page_value * pagesize
        end = start + pagesize

        for t_user_info in values[start:end]:
            xtb.add_row(dict(t_user_info).values())
        print(xtb)
    else:
        print("syntax error.")
