import pymysql

db=pymysql.connect("localhost", "wxl", "123456", "testdb")
cursor = db.cursor()
#sql = "insert into users(username,age,tel,email)  values( tmpv[0], tmpv[1],tmpv[2],tmpv[3])"



dic={"w": {"name": "w", "age": "12", "tel": "e", "email": "r"}, "test": {"name": "test","age": "123", "tel": "456", "email": "444"}}
for k,v in dic.items():
    #print(v),print(type(v))
    tmpv=list(v.values())
    print(type(tmpv[0]))
   # print(tmpv[0])
    sql = "insert into users(username,age,tel,email)  values( '{}', {},'{}','{}')".format((tmpv[0]),tmpv[1],tmpv[2],tmpv[3])
    cursor.execute(sql)
    print(sql)
db.commit()
#data=cursor.fetchall()
#print(data)
db.close()
   # print(tmpv)
