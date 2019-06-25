'''
create table users(
	username varchar(32) not null,
	age int not null,
	sex char(2) not null CHECK (sex LIKE '男' OR sex LIKE '女'),
	phone char(11) not null CHECK (LEN(phone)=11),
	email varchar(32) not null
);
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/25 15:20
# @Author  : 罗小贱
# @email: ljq906416@gmail.com
# @File    : dbutils
# @Software: PyCharm

import pymysql
import configmgt

FILENAME = 'db.ini'

def connect():
    cfg,ok = configmgt.ReadConfig(FILENAME,'lxjdb')
    if not ok:
        return cfg,False
    try:
        conn = pymysql.connect(
            host = cfg['host'],
            user = cfg['username'],
            password=cfg['password'],
            database=cfg['database'],
            port=int(cfg['port']),
        )
    except Exception as e:
        return None
    return conn

#数据库增加
def db_insert(data):
    conn = connect()
    cur = conn.cursor()
    sql_insert = "insert into users(username,age,sex,phone,email) values (%s,%s,%s,%s,%s);"
    print(sql_insert)
    try:
       cur.execute(sql_insert,data)
       conn.commit()
    except Exception as e:
        conn.rollback()
    finally:
        conn.close()

#数据库删除
def db_delete(username):
    conn = connect()
    cur = conn.cursor()
    sql_delete = "delete from users where username = %s"
    print(sql_delete)
    try:
        cur.execute(sql_delete,(username))
        conn.commit()
    except Exception as e:
        conn.rollback()
    finally:
        conn.close()

#更新数据库
def db_update(data):
    conn = connect()
    cur = conn.cursor()
    sql_update = "update users set username = %s,age = %s,sex = %s,phone = %s,email = %s where username = %s"
    try:
        cur.execute(sql_update,(data))
        conn.commit()
    except Exception as e:
        conn.rollback()
    finally:
        conn.close()

#查询数据库
def db_qurey():
    conn = connect()
    cur = conn.cursor()
    sql = '''select * from users'''
    try:
        cur.execute(sql)
        results = cur.fetchall()
        for row in results:
            username = row[0]
            print(username)
    except Exception as e:
        raise  e
    finally:
        conn.close()
