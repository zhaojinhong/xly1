# -*- coding: utf-8 -*-
# @Time    : 2019-05-19 10:24
# @Author  : Joe
# @Site    : 
# @File    : user_manage.py
# @Software: PyCharm
# @function: User_manage

'''
输入格式
add joe 18 13800138000 wennjoe@163.com
add joe1 18 13800138000 wennjoe@163.com
'''

import sys

user_lists = []
times = 0
retry_times = 6
logininfo = ('joe', '1')
# username_all变量装载user_lists中的用户名，方便各个方法定位
username_all = []


def judge_user():
    '''
    判断用户是否存在，并定位输入用户info在user_lists中的下标
    :return: input_user_index
    '''
    if user_list[1] in username_all:
        input_user_index = username_all.index(user_list[1])
        return input_user_index
    else:
        return print("no user: %s" % user_list[1])


while times < retry_times:
    username = input('input username:')
    password = input('input password:')

    if username == logininfo[0] and password == logininfo[1]:
        print("%s login success!" % username)

        while True:
            userinfo = input("input userinfo:")
            # str --> list type
            user_list = userinfo.split(' ')

            if user_list[0] == 'add':
                if user_list[1] not in username_all:
                    user_lists.append(user_list[1:])
                    username_all.append(user_list[1])
                    print("add %s userinfo success!" % user_list[1])
                else:
                    print("useinfo exist")

            elif user_list[0] == 'del':
                input_user_index = judge_user()
                if input_user_index is not None:
                    user_lists.pop(input_user_index)
                    username_all.pop(input_user_index)
                    print("delete user: %s success" % user_list[1])

            elif user_list[0] == 'update':
                input_user_index = judge_user()
                if input_user_index is not None:
                    if user_list[3] == 'username':
                        if user_list[5] in username_all:
                            print("%s username exist!" % user_list[5])
                        else:
                            user_lists[input_user_index][0] = user_list[5]
                            username_all[input_user_index] = user_list[5]
                            print("modify username is: %s" % user_list[5])
                    elif user_list[3] == 'age':
                        user_lists[input_user_index][1] = user_list[5]
                        print("modify %s age: %s" % (user_list[1], user_list[5]))

                    elif user_list[3] == 'telephone':
                        user_lists[input_user_index][2] = user_list[5]
                        print("modify %s telephone: %s" % (user_list[1], user_list[5]))

                    elif user_list[3] == 'email':
                        user_lists[input_user_index][3] = user_list[5]
                        print("modify %s email: %s" % (user_list[1], user_list[5]))
                    else:
                        print("no item")

            elif user_list[0] == 'list':
                print("username", "age", "telephone", "email")
                print("*" * 50)
                for x in user_lists:
                    print(x, end='\n')
                    print("*" * 50)

            elif user_list[0] == 'find':
                input_user_index = judge_user()
                if input_user_index is not None:
                    print("username", "age", "telephone", "email")
                    print("result: %s" % user_lists[input_user_index])
            else:
                sys.exit()

    else:
        times += 1
        print("username or password error!")
