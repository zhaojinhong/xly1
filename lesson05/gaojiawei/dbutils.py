import pymysql

import configmgt

FILENAME = 'dbinfo.ini'

def connnet():

    cfg, ok = configmgt.ReadConfig(FILENAME, 'db')
    if not ok:
        return cfg, False

    try:
        conn = pymysql.connect(
            host=cfg['host'],
            user=cfg['username'],
            password=cfg['password'],
            database=cfg['database'],
            port=int(cfg['port']),
        )
    except:
        return None
    return conn

def insert(sql):
    conn = connnet()
    if not conn:
        return "conn db fail", False
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
    conn = connnet()
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

def select(sql):
    conn = connnet()
    if not conn:
        return "conn db fail", False
    cur = conn.cursor()

    try:
        cur.execute(sql)
    except Exception as e:
        return e, False
    else:
        rows = cur.fetchall()
        return rows, True
    finally:
        cur.close()
        conn.close()

def delete(sql):
    conn = connnet()
    if not conn:
        return "conn db fail", False
    cur = conn.cursor()

    try:
        cur.execute(sql)
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
def cleartab(sql):
    conn = connnet()
    if not conn:
        return "conn db fail", False
    cur = conn.cursor()

    try:
        cur.execute(sql)
        print(cur.rowcount)
        if cur.rowcount == 0:
            return 'Clear tables fail', False

        conn.commit()
        return 'Clear tables succ.', True
    except Exception as e:
        conn.rollback()
        return e, False
    finally:
        cur.close()
        conn.close()




