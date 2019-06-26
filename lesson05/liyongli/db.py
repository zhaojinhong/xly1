import pymysql
'''
def __init__(self, host=None, user=None, password="",
                 database=None, port=0, unix_socket=None,
                 charset='', sql_mode=None,
                 read_default_file=None, conv=None, use_unicode=None,
                 client_flag=0, cursorclass=Cursor, init_command=None,
                 connect_timeout=10, ssl=None, read_default_group=None,
                 compress=None, named_pipe=None,
                 autocommit=False, db=None, passwd=None, local_infile=False,
                 max_allowed_packet=16*1024*1024, defer_connect=False,
                 auth_plugin_map=None, read_timeout=None, write_timeout=None,
                 bind_address=None, binary_prefix=False, program_name=None,
                 server_public_key=None):
'''

conn = pymysql.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '123456',
    database = 'ops'
)

cur = conn.cursor()


# sql = '''insert into users(username,age,tel,email)  values('monkey2', 12,'132xxx','monkey2@51reboot.com');'''
sql = 'select * from users'

cur.execute(sql)
conn.commit()
data = cur.fetchall()
print(data)
# 关闭游标
cur.close()

# 关闭连接
conn.close()