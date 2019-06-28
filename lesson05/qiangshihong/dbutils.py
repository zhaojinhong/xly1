#!/usr/bin/python

import pymysql
from config import configmgt

FILENAME = 'config/mysql_config.ini'

def connect():
    # 获取配置文件 db_connect 章节下字段(字典类型)，成功 ok = True,失败 ok =False
    cfg,ok = configmgt.ReadConfig(FILENAME,'db_connect')
    if not ok:
        return cfg,False
    try:
        # 打开数据库连接
        db_conn = pymysql.connect(
            # 获取配置文件 db_connect 章节下各 key 的值
            host=cfg['host'],
            user=cfg['user'],
            password=cfg['password'],
            database=cfg['database'],
            port=int(cfg['port'])
        )
        return db_conn
    except:
        return None

def select(sql):
    # 打开数据库连接
    db_conn = connect()

    #如果连接不成功，抛错
    if not db_conn:
        return "conn db fail", False
    else:
        # 使用 cursor() 方法创建一个游标对象 cur
        cur = db_conn.cursor()
    try:
        # 使用 execute() 方法执行 SQL 查询
        cur.execute(sql)
        # 使用 fetchall() 方法接收全部的返回结果行.
        rows = cur.fetchall()
        return rows, True
    except Exception as e:
        return e, False
    finally:
        # 关闭游标
        cur.close()
        # 关闭数据库连接
        db_conn.close()

def insert(sql):
    conn = connect()
    if not conn:
        return "conn db fail.",False
    cur = conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
        return 'Insert succ.', True
    except Exception as e:
        conn.rollback()
        return e, False
    finally:
        cur.close()
        conn.close()
def update(sql):
    conn = connect()
    if not conn:
        return "conn db fail", False
    cur = conn.cursor()

    try:
        cur.execute(sql)
        print(cur.rowcount)
        if cur.rowcount == 0:
            return 'Update fail', False

        conn.commit()
        return 'Update succ.', True
    except Exception as e:
        conn.rollback()
        return e, False
    finally:
        cur.close()
        conn.close()

def delete(sql):
    conn = connect()
    if not conn:
        return "conn db fail.", False
    cur = conn.cursor()

    try:
        cur.execute(sql)
        #打印sql执行后影响的行数
        print(cur.rowcount)
        if cur.rowcount == 0:
            return 'Delete fail', False

        conn.commit()
        return 'Insert succ.', True
    except Exception as e:
        conn.rollback()
        return e, False
    finally:
        cur.close()
        conn.close()

def main():
    # #增加用户
    # for i in range(10, 30):
    #     sql = '''insert into users(username,age,tel,email)  values('test{}', {},'132xxx','monkey{}@51reboot.com');'''.format(i,i,i)
    #     insertMsg, ok = insert(sql)
    #     if not ok:
    #         print(insertMsg)

    # #删除用户
    # sql = '''delete from users where username = 'test10';'''
    # deleteMsg, ok = delete(sql)
    # if not ok:
    #     print(deleteMsg)

    # #修改用户
    # sql = "update users set age = 20 where username = 'test11';"
    # msg,ok = update(sql)
    # if not ok:
    #     print(msg)

    sql = '''select * from users;'''
    result, ok = select(sql)
    if not ok:
        print(result)
    else:
        fields = ['id', 'username', 'age', 'tel', 'email']
        # for i in result:
        #     print(dict(zip(fields, i)))

        #列表生成式
        retdata = [ dict(zip(fields, i)) for i in result ]

        import json
        print(json.dumps(retdata, indent=8))

if __name__ == '__main__':
    main()


