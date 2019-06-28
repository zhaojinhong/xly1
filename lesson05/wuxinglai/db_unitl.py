import  pymysql
db = pymysql.connect("localhost", "wxl", "123456", "testdb")

#sql = '''insert into users(username,age,tel,email)  values('monkey2', 12,'132xxx','monkey2@51reboot.com')'''
sql='''select * from users '''
cursor = db.cursor()
cursor.execute(sql)
db.commit()
data=cursor.fetchall()
print(data)
db.close()