

'''
增加
删除
修改
列出
搜索
分页
退出
保存
加载

日志
csv
'''


# 标准模块
import sys
import json

# 第三方模块
from prettytable import PrettyTable



# 全局变量
DB_FILE = '51reboot.db'
FIELDS = ['name', 'age', 'tel', 'email']
RESULT = {'monkey': {'name': 'monkey', 'age': '12', 'tel': '132xxx', 'email': 'monkey@qq.com'}, 'monkey2': {'name': 'monkey2', 'age': '12', 'tel': '132xxx', 'email': 'monkey@qq.com'}}
# RESULT = [
#     {'name' : 'monkey1', 'age' : 12, 'tel' : '132xxx', 'email' : 'monkey1@qq.com'},
#     {'name' : 'monkey2', 'age' : 12, 'tel' : '132xxx', 'email' : 'monkey1@qq.com'},
# ]

# TMP_RESULT = {
#     'monkey1' : {'name' : 'monkey1', 'age' : 12, 'tel' : '132xxx', 'email' : 'monkey1@qq.com'}
# }


def addUser(args):
    '''
    add monkey1 12 132xxx monkey1@qq.com

    args = "monkey1 12 132xxx monkey1@qq.com"
    :return:
    '''
    userinfolist = args.split(" ")
    if len(userinfolist) != 4:
        return "addUser failed, args length != 4"

    username = userinfolist[0]
    if username in RESULT:
        print("Username: {} already exists.".format(username))
    else:
        RESULT[username] = {
            'name'  : username,
            'age'   : userinfolist[1],
            'tel'   : userinfolist[2],
            'email' : userinfolist[3],
        }
        print("add user {} secc.".format(username))





def deleteUser(args):
    '''
    delete monkey1
    args = monkey1
    :param args:
    :return:
    '''
    print(RESULT)
    userinfolist = args.split(" ")
    if len(userinfolist) != 1:
        return "deleteUser failed, args length != 1"

    username = args
    if username in RESULT:
        RESULT.pop(username, None)
        print("delete user {} secc.".format(username))
    else:
        print("Username: {} not found.".format(username))


def updateUser():
    pass

def listUser():
    '''
    打印所有用户信息
    :return:
    '''
    xtb = PrettyTable()
    xtb.field_names = FIELDS
    for k, v in RESULT.items():
        xtb.add_row(v.values())
    print(xtb)

def findUser():
    pass

def displayUser():
    pass

def save():
    '''
    写内存中的数据到磁盘中
    :return:
    '''
    with open(DB_FILE, 'w') as fd:
        fd.write(json.dumps(RESULT))

def load():
    '''
    读磁盘的数据加载到内存中
    :return: dict
    '''
    with open(DB_FILE, 'r') as fd:
        data = fd.read()
        if not len(data):
            return {}
        else:
            return json.loads(data)



def logout():
    '''
    退出整个脚本
    break for、while
    :return:
    '''
    sys.exit(0)


def main():
    '''
    入口函数
    '''
    while True:
        userinfo = input("Please input userinfo: ")
        # if not len(userinfo):
        #     print("invalid input.")
        #     continue
        # addUser(userinfo)
        # deleteUser(userinfo)
        listUser()


if __name__ == '__main__':
    main()