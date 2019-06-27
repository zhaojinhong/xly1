# -*- coding:utf-8 -*-
# author: lyl
import hashlib
import user_manger
from models import user


def md5cmd(password):
    # 加盐操作
    md5 = hashlib.md5(b'51reboot')
    md5.update(password.encode())
    # 返回输入字符串的md5
    return md5.hexdigest()


def auth(username, password):
    try:
        tag = user.select().where(user.username == username).get()
        if md5cmd(password) == tag.password:
            return True
    except:
        return False



def logout():
    '''
    退出整个脚本
    break for、while
    :return:
    '''
    exit(0)


def logic():
    while True:
        userinfo = input("Please inpur user info: ")  # add monkey 12 132xx monkey!@qq.com
        if len(userinfo) == 0:
            print("invalid input.")
        else:
            userinfo_list = userinfo.split()
            action = userinfo_list[0]
            userinfo_string = ' '.join(userinfo_list[1:])
            if action == 'add':
                user_manger.addUser(userinfo_string)
            elif action == 'delete':
                user_manger.deleteUser(userinfo_string)
            elif action == 'update':
                user_manger.updateUser(userinfo_string)
            elif action == 'find':
                user_manger.findUser(userinfo_string)
            elif action == 'display':
                user_manger.displayUser(userinfo_string)
            elif action == 'list':
                user_manger.listUser()
            elif action == 'save':
                save()
            elif action == 'load':
                global RESULT
                RESULT = load()
            elif action == 'logout':
                logout()


md5cmd('123456')
