#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/19 20:20
# @Author  : 罗小贱
# @email: ljq906416@gmail.com
# @File    : 用户登录认证管理系统
# @Software: PyCharm

sum_people = ['as']

def add():
    '添加用户'
    add_people = input('请输入添加的用户名:')
    if add_people in sum_people:
        print('添加的用户已经存在,请重新输入')
    else:
        sum_people.append(add_people)

def delete():
    '删除用户'
    delete_people = input('请输入删除的用户名:')
    try:
        if delete_people in sum_people:
            print('正在删除')
            sum_people.remove(delete_people)
        else:
            print('不存在此用户')
    except Exception as e:
        print(e)

def modfiy():
    '修改用户'
    modfiy_before_people = input('请输入需要修改的用户：')
    modfiy_after_people = input('将用户修改为：')
    try:
        if modfiy_before_people in sum_people:
            modfiy_index =sum_people.index(modfiy_before_people)
            sum_people[modfiy_index] = modfiy_after_people
        else:
            print('删除的用户不存在，请检查用户名')
    except Exception as e:
        print(e)

'查询用户list'
def check():
    check_people = input('请输入需要查询的用户：')
    try:
        if check_people in sum_people:
            print('查询的用户存在')
        else:
            print('查询的用户不存在，请检查用户名')
    except Exception as e:
        print(e)

'搜查用户find'
def find():
    find_people = input('请输入需要查询的用户：')
    try:
        for i,people in enumerate(sum_people):
            if people.find(find_people) != -1:
                print('搜查的用户存在')
            else:
                print('搜查的用户不存在,请检查用户名')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    print('--------------------')
    print('欢迎登录用户管理系统')
    print('增加用户请输入：add')
    print('删除用户请输入：delete')
    print('修改用户请输入：modfiy')
    print('查询用户请输入：check')
    print('搜寻用户请输入：find')
    print('-----------------------------------')
    user_input = input('按照上面提示输入：')
    try:
        if user_input == 'add':
            add()
        elif user_input == 'delete':
            delete()
        elif user_input == 'modfiy':
            modfiy()
        elif user_input == 'check':
            check()
        elif user_input == 'find':
            find()
        else:
            print('检查输入的选项是不是以上提示的选项，请重新输入')
    except Exception as e:
        print(e)
    # add()
    # delete()
    # modfiy()
    # find()


print(sum_people)