#!/usr/bin/env python
# -*- encoding:utf8 -*-
#*******************************************
# Author: LuoFeng
# Date: 2019-06-15
# Filename: utils.py
# Describe:
#*******************************************

import csv
import json
from logzero import logger

def save_audit_log(**kwargs):
    '''保存用户操作记录'''

    try:
        audit_log_file = kwargs.get('audit_log_file', 'user_oper_audit.log')
        oper_audit_msg = kwargs.get('oper_audit_msg')

        with open(audit_log_file, 'a') as f:
            f.write(oper_audit_msg + '\n')
            logger.info('user actions have been successfully recorded.')

    except Exception as e:
            logger.info('wirte error',e)


def save_data_to_csv(**kwargs):
    '''将数据写入csv文件'''

    try:
        csv_file_path = kwargs.get('csv_file_path', 'default.csv')
        csv_column_name   = kwargs.get('column_name', [])
        data = kwargs.get('data')

        with open(csv_file_path, 'w', newline='') as f:
            fhandler = csv.DictWriter(f, column_name)
            fhandler.writeheader()
            fhandler.writerows(data)
            logger.info('user data write Successfully.')

    except Exception as e:
            logger.error('write error', e)

def read_data_in_file(**kwargs):
    '''读取文件的数据'''

    try:
        filename = kwargs.get('filename')
        with open(filename, 'r') as f:
            userdata = f.readlines()

        return userdata

    except Exception as e:
        return False


def write_data_to_file(**kwargs):
    '''写数据到文件中'''

    try:
        filename = kwargs.get('filename')
        userdata = kwargs.get('userdata')

        with open(filename, 'w+') as f:
            for data in userdata:
                f.write(json.dumps(data)+'\n')

        return True

    except Exception as e:
        return False

#save_data_to_csv(
#    cvs_file_path = './test2.csv',
#    column_name = ['class', 'name', 'sex', 'height', 'year'],
#    data = rows
#)
