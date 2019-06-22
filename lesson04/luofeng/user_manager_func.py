#!/usr/bin/env python
# -*- encoding:utf8 -*-
#*******************************************
# Author: LuoFeng
# Date: 2019-06-15
# Filename: user_manager_func.py
# Describe:
#*******************************************

import time
import json
from logzero import logger
from prettytable import PrettyTable
from utils import save_audit_log, save_data_to_csv, read_data_in_file, write_data_to_file

# global variables
USERINFO = ("luofeng", "123456")
filename = 'user_data_file.txt'
cvs_file = 'userdata.cvs'
audit_log_file = 'user_oper_audit.log'
out_data = {}


def login():
    '''用户登录'''

    INIT_FAIL_CNT = 0
    MAX_FAIL_CNT = 6

    while INIT_FAIL_CNT < MAX_FAIL_CNT:
        username = input("Please input your username: ")
        password = input("Please input your password: ")
        if username == USERINFO[0] and password == USERINFO[1]:
            out_data.update({
                "status": 0,
                "msg": "user {} successfully registered, logged in status.".format(username)
            })
            logger.info(ou_data.get('msg'))

        else:
            out_data.update({
                "status": 1,
                "msg": "Login failure, username or password error !!!"
            })

            logger.error(out_data.get('msg'))
        INIT_FAIL_CNT+=1

    return json.dumps(out_data)

def add_user(**kwargs):
    '''增加用户信息'''

    userinfo = kwargs.get('userinfo')
    filename = kwargs.get('filename')
    userdata = []
    content = {}

    try:
        content.update({
            "username": userinfo[0],
            "age": userinfo[1],
            "tel": userinfo[2],
            "email": userinfo[3],
            "address": userinfo[4],
        })

        userdata.append(content)

        username = content.get('username')
        result = json.loads(check_users(username = username, filename = filename))

        if result.get('status'):
            msg = "user {} already exist.".format(username)
            out_data.update({
                "status": 1,
                "msg": msg
            })

            logger.info(msg)

        else:
            result = json.loads(save_data(filename = filename, userdata = userdata))
            if not result.get('status'):
                msg = "user {} was successfully added.".format(username)
                save_audit_log(
                        audit_log_file = audit_log_file,
                        oper_audit_msg = msg
                )

                out_data.update({
                    "status": 0,
                    "msg": "Success",
                    "data": True
                })

            return json.dumps(out_data)

    except Exception as e:
        logger.error(e)

def del_user(**kwargs):
    '''删除用户信息'''

    try:
        userdata = []
        filename = kwargs.get('filename')
        username = kwargs.get('username')
        content = read_data_in_file(filename = filename)
        for data in content:
            data = json.loads(data)

            if username == data.get('username'):
                del data

            else:
                userdata.append(data)
                write_data_to_file(filename=filename, userdata=userdata)

    except Exception as e:
        logger.error(e)

def update_user(**kwargs):
    '''更新用户信息'''

    try:
        userdata = []
        filename = kwargs.get('filename')
        username = kwargs.get('username')
        userinfo = kwargs.get('userinfo')

        # 判断用户数据长度
        if len(userinfo) < 5:
            logger.error('input error, please try enter(username age tel email address):')

        # 判断用户是否存在
        result = json.loads(check_users(filename=filename, username=username))
        if result.get('status'):
            context = json.loads(read_data_in_file(filename=filename))
            for data in context.get('data'):
                data = json.loads(data)
                if username == data.get('username'):
                    data.update({
                        "username": userinfo[0],
                        "age": userinfo[1],
                        "tel": userinfo[2],
                        "email": userinfo[3],
                        "address": userinfo[4]
                    })
                    userdata.append(data)
                else:
                    userdata.append(data)

            # 重新用户信息文件
            result = write_data_to_file(
                    filename = filename,
                    userdata = userdata
            )

        else:
            return json.dumps(result)

    except Exception as e:
        print(e)

def query_user(**kwargs):
    '''查询用户信息'''

    try:
        username = kwargs.get('username')
        filename = kwargs.get('filename')

        # 判断用户是否存在
        result = json.loads(check_users(
            username = username,
            filename = filename
        ))

        if result.get('status'):
            context = json.loads(read_data_in_file(filename=filename))

            if not context.get('status'):
                for data in context.get('data'):
                    data = json.loads(data)

                    if username == data.get('username'):
                        field_names = data.keys()
                        table = PrettyTable()
                        table.field_names = field_names
                        table.add_row([
                            data.get('username'),
                            data.get('age'),
                            data.get('tel'),
                            data.get('email'),
                            data.get('address')
                        ])

                    logger.info('user data query success.')
                    print(table)
        else:
            logger.error(result.get('msg'))

    except Exception as e:
        print(e)

def check_users(**kwargs):
    '''判断用户是否存在'''

    try:
        username = kwargs.get('username')
        filename = kwargs.get('filename')

        result = json.loads(read_data_in_file(filename=filename))
        user_flag = False
        if not result.get('status'):
            for data in result.get('data'):
                data = json.loads(data)
                usernames = data.values()

                if username in usernames:
                    user_flag = True

            if user_flag:
                msg = "user {} already exist.".format(username)
                out_data.update({
                    "status": 1,
                    "msg": msg
                })


            else:
                msg = 'user {} does not exist.'.format(username)
                out_data.update({
                    "status": 0,
                    "msg": msg
                })

            return json.dumps(out_data)

    except Exception as e:
        logger.error(e)

def save_data(**kwargs):
    '''保存用户信息'''

    filename = kwargs.get('filename')
    userdata = kwargs.get('userdata')

    try:
        context = json.loads(read_data_in_file(
            filename = filename
        ))

        if not context.get('status'):
            for data in context.get('data'):
                data = json.loads(data)
                userdata.append(data)

            result = json.loads(write_data_to_file(
                filename= filename,
                userdata = userdata
            ))

        if not result.get('status'):
            out_data.update({
                "status": 0,
                "msg": "user information has been saved."
            })

            return json.dumps(out_data)

        else:
            return json.dumps(result)

    except Exception as e:
        logger.error(e)

#def export_data_to_cvsfile(**kwargs):
#    '''导出用户信息'''
#
#    try:
#        cvs_file = kwargs.get('cvs_file')
#        column_name =
#
