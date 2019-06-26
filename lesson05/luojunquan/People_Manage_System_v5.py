#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/25 21:20
# @Author  : 罗小贱
# @email: ljq906416@gmail.com
# @File    : People_Manage_System_v5
# @Software: PyCharm
from db import db_insert,db_delete,db_update
from check_utils import check_email,check_phone,check_sex,check_user
from utils import list_table

#添加用户
def add():
    username = input('请输入用户名：')
    age = input('请输入年龄：')
    sex = input('请输入性别：')
    phone = input('请输入手机号：')
    email = input('请输入邮箱地址：')
    email_tag = check_email(email)
    phone_tag = check_phone(phone)
    sex_tag = check_sex(sex)
    username_tag = check_user(username)
    if email_tag is not True:
        print(email_tag)
    elif phone_tag is not True:
        print(phone_tag)
    elif sex_tag is not True:
        print(sex_tag)
    elif username_tag is not True:
        print(username_tag)
    else:
        data = (username,age,sex,phone,email)
        db_insert(data)

#删除用户
def delete():
    username = input('请输入需要删除的用户名：')
    db_delete(username)

#更新用户
def update():
    username = input('请输入需要更新的用户名：')
    new_username = input('请输入新用户名：')
    new_age = input('请输入新年龄：')
    new_sex = input('请输入新性别：')
    new_phone = input('请输入新手机号：')
    new_email = input('请输入新邮箱地址：')
    db_update(username,new_username,new_age,new_sex,new_phone,new_email)

#显示所有用户
def list_all():
    list_table()

# 定义变量
INIT_FAIL_CNT = 0
MAX_FAIL_CNT = 6

def main():
    # 主函数，程序入口
    while INIT_FAIL_CNT < MAX_FAIL_CNT:
        print("""
                  用户管理系统
                1-展示用户信息
                2-增加用户信息
                3-修改用户信息
                4-删除用户信息
                5-插入数据库字段
                0-退出程序
                """)
        num = int(input('请输入操作编号：'))
        if num == 1:
            list_all()
        elif num == 2:
            add()
        elif num == 3:
            update()
        elif num == 4:
            delete()
        elif num == 0:
            break

if __name__ == '__main__':
    main()
# add('lxj6',35,'男','13993845112','lxj6@qq.com')
# delete('lxj3')
# update('lxj5',36,'男','13993845126','lxj5@qq.com,','lxj2')
# username,age,sex,phone,email = db_qurey()
# username,age,sex,phone,email =check_user()
# print(username,age,sex,phone,email)
# c =check_user()
# print(c)