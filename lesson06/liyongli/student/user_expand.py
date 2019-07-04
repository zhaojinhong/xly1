# -*- coding:utf-8 -*-
# author: lyl
import hashlib
import user_manger
from models import user

class Auth(object):
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def md5cmd(self):
        password = self.password
        # 加盐操作
        md5 = hashlib.md5(b'51reboot')
        md5.update(password.encode())
        # 返回输入字符串的md5
        return md5.hexdigest()

    def auth(self):
        username, password = self.username, self.password

        try:
            tag = user.select().where(user.username == username).get()

        except Exception as e:
            message = e.__str__()
            # 对返回信息进行判断，确认是数据库无法连接，还是用户不存在
            if '2003,' in message:
                print(e)
                return False
            else:
                return False
        try:

            if self.md5cmd() == tag.password:
                return True
        except:
            return False

    def logout(self):
        exit(0)


def user_help(username='', Help=False):
    base = ''' 
    list        显示所有用户
    find        查找指定用户
    display     分页显示用户信息
    export      将当前所有用户保存至csv文件   
    logout      退出系统
    add         增加用户
    delete      删除指定用户   
    update      更新指定用户
    help        查看帮助信息
        '''
    if Help:
        format_print(True, "{}".format(base))
    else:
        format_print(True, "Hello {} 欢迎登陆，本系统支持如下功能".format(username))
        format_print(True, "{}".format(base))


def logic():
    while True:
        userinfo = input("Please inpur user info: ")  # add monkey 12 132xx monkey!@qq.com
        if len(userinfo) == 0:
            print("invalid input.")
        else:
            user_info_list = userinfo.split()
            action = user_info_list[0]
            user_info_string = ' '.join(user_info_list[1:])
            cmd = user_manger.User(user_info_string)
            if action == 'add':
                cmd.addUser()
            elif action == 'delete':
                cmd.deleteUser()
            elif action == 'update':
                cmd.updateUser()
            elif action == 'find':
                cmd.findUser()
            elif action == 'display':
                cmd.displayUser()
            elif action == 'list':
                cmd.listUser()
            elif action == 'export':
                cmd.ExportUser()
            elif action == 'logout':
                Auth().logout()
            elif action == 'help':
                user_help(Help=True)


def format_print(tag, *args):
    if tag:
        print("\033[1;32m{}\033[0m".format(*args))
    else:
        print("\033[1;31m{}\033[0m".format(*args))
