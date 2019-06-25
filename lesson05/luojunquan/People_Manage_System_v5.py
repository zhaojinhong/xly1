from db import db_insert,db_delete,db_update,db_qurey

def add(username,age,sex,phone,email):
    data = (username,age,sex,phone,email)
    db_insert(data)

def delete(username):
    db_delete(username)

def update(new_username,new_age,new_sex,new_phone,new_email,username):
    data = (new_username,new_age,new_sex,new_phone,new_email,username)
    db_update(data)

def query():
    db_qurey()
# add('lxj3',35,'男','13993845125','lxj3@qq.com')
# delete('lxj3')
# update('lxj5',36,'男','13993845126','lxj5@qq.com,','lxj2')
query()