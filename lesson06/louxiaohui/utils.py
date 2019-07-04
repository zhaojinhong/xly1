#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql
from configmgt import readconfig
import sys

dbinfo, ok = readconfig('config.ini', 'dbinfo')


class DB(object):
    def __init__(self):
        dbinfo['port'] = int(dbinfo['port'])
        try:
            self.conn = pymysql.connect(**dbinfo)
            self.cur = self.conn.cursor()
        except Exception as e:
            print (e)
            return None


    def insert(self, sql):
        if not self.conn:
            return "conn db fail", False
        try:
            self.cur.execute(sql)
            self.conn.commit()
            return 'Insert succ.', True
        except Exception as e:
            self.conn.rollback()
            return e, False


    def update(self, sql):
        if not self.conn:
            return "conn db fail", False
        try:
            self.cur.execute(sql)
            print(self.cur.rowcount)
            if self.cur.rowcount == 0:
                return 'Update fail', False
            self.conn.commit()
            return 'Update succ.', True
        except Exception as e:
            self.conn.rollback()
            return e, False


    def select(self, sql):
        if not self.conn:
            return "conn db fail", False
        try:
            self.cur.execute(sql)
        except Exception as e:
            return e, False
        else:
            rows = self.cur.fetchall()
            if len(rows) == 0:
                return "Empty set.", False
            else:
                return rows, True


    def delete(self, sql):
        if not self.conn:
            return "conn db fail", False
        try:
            self.cur.execute(sql)
            print(self.cur.rowcount)
            if self.cur.rowcount == 0:
                return 'Delete fail', False
            self.conn.commit()
            return 'Insert succ.', True
        except Exception as e:
            self.conn.rollback()
            return e, False


    def __del__(self):
        self.conn.close()
        self.cur.close()


#db = DB()
#sql = '''update users set age = 21 where username = 'monkey11';'''
#result, ok = db.update(sql)
#print (result)


def main():
    #for i in range(10, 30):
    #    sql = '''insert into users(username,age,tel,email)  values('monkey{}', {},'132xxx','monkey{}@51reboot.com');'''.format(i, i ,i)
    #    insertMsg, ok = insert(sql)
    #    if not ok:
    #        print(insertMsg)

    # sql = '''delete from users where username = 'monkey10';'''
    # deleteMsg, ok = delete(sql)
    # if not ok:
    #     print(deleteMsg)
    # sql = '''update users set age = 20 where username = 'monkey11';'''
    # msg, ok = update(sql)
    # if not ok:
    #     print(msg)

    sql = '''select * from users limit 2;'''
    result, ok = select(sql)
    if not ok:
        print(result)
    else:
        fields = ['id', 'username', 'age', 'tel', 'email']
        # for i in result:
        #     print(dict(zip(fields, i)))
        retdata = [ dict(zip(fields, i)) for i in result ]
        import json
        print(json.dumps(retdata, indent=4))


#if __name__ == '__main__':
#    main()
