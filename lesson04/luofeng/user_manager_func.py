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
from utils import save_audit_log, save_data_to_csv, read_data_in_file, write_data_to_file

# global variables
USERINFO = ("luofeng", "123456")
filename = 'user_data_file.txt'
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

    content = kwargs.get('userdata')
    filename = kwargs.get('filename')
    userdata = {}

    try:
        userdata.update({
            "username": content[0],
            "age": content[1],
            "tel": content[2],
            "email": content[3],
            "address": content[4],
        })

        username = userdata.get('username')
        result = json.loads(check_users(username = username, filename = filename))

        if result.get('status'):
            msg = "user {} already exist.".format(username)
            out_data.update({
                "status": 1,
                "msg": msg
            })

            logger.info(msg)

        else:
            msg = "user {} was successfully added.".format(username)
            out_data.update({
                "status": 0,
                "msg": msg
            })

            result = json.loads(save_data(filename = filename, userdata = userdata))

            if not result.get('status'):
                save_audit_log(
                    audit_log_file = "user_oper_audit.log",
                    oper_audit_msg = msg
                )

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
        filename = kwargs.get('filename')
        username = kwargs.get('username')
        userdata = kwargs.get('username')

        # 判断用户数据长度
        if len(userdata) < 5:
            logger.error('input error, please try enter(username age tel email address):')

        # 判断用户是否存在
        result = json.loads(check_users(filename=filename, username=username))
        if not result.get('status'):


def check_users(**kwargs):
    '''判断用户是否存在'''
    username = kwargs.get('username')
    filename = kwargs.get('filename')

    try:
        with open(filename, 'r') as f:
            result = f.readlines()

        user_flag = False
        if len(result) > 0:
            for data in result:
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
        with open(filename, 'a', newline='\n') as f:
            f.write(json.dumps(userdata))
            out_data.update({
                "status": 0,
                "msg": "user information has been saved."
            })

            return json.dumps(out_data)

    except Exception as e:
        logger.error(e)


#check_users(
#    username = 'luofeng',
#    filename = 'user_data_file.txt'
#)

#add_user(
#    userdata = ['reboot', '29', '18210085737', '18210085737@139.com', 'beijing'],
#    filename = filename
#)

del_user(
    username = 'reboot',
    filename = filename
)
