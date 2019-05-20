'''
1. 登录认证；
2. 增删改查和搜索
    3.1 增 add           # add monkey 12 132xxx monkey@51reboot.com
    3.2 删 delete        # delete monkey
    3.3 改 update        # update monkey set age = 18
    3.4 查 list          # list
    3.5 搜 find          # find monkey
3. 格式化输出
'''


# 定义变量
RESULT = []
# INIT_FAIL_CNT = 0
# MAX_FAIL_CNT = 6
COUNTER = 0
USERINFO = ("51reboot", "123456")
FIELDS = ['username', 'age', 'tel', 'email']
RESULT.append(FIELDS)

class Useradmin(object):
    '''用户管理'''
    def add(self,info_list):
        '''添加模块'''
        #判断用户是否存在*
        action_info = info_list[1]
        userinfo_name = []
        for i in RESULT:
            userinfo_name.append(i[0])
        if action_info not in userinfo_name:
            print("Add {} succ.".format(info_list[1]))
            RESULT.append(info_list[1:])
        else:
            print('User already exists')


    def delete(self,info_list):
        '''删除模块'''
        action_info = info_list[1]
        userinfo_name = []
        for i in RESULT:
            userinfo_name.append(i[0])
        if action_info not in userinfo_name:
            print('User does not exist')
        else:
            for i in RESULT:
                if action_info in i:
                    tmp_info = RESULT.index(i)
            RESULT.pop(tmp_info)
            print("Del {} succ.".format(info_list[1]))
            for x in RESULT:
                print("{} {} {} {}".format(x[0], x[1], x[2], x[3]), end="\t")
                print()
                print("-" * 50)


    def update(self,info_list):
        '''修改模块'''
        action_info = info_list[1]
        userinfo_name = []
        for i in RESULT:
            userinfo_name.append(i[0])
        if action_info not in userinfo_name:
            print('User does not exist')
        else:
            for i in RESULT:
                if action_info in i:
                    tmp_info = RESULT.index(i)
                    if info_list[3] == 'name':
                        action_info = info_list[1]
                        userinfo_name = []
                        for i in RESULT:
                            userinfo_name.append(i[0])
                        if action_info not in userinfo_name:
                            RESULT[tmp_info][0] = info_list[5]
                            print("Update {} succ.".format(info_list[1]))
                        else:
                            print('User already exists')
                    elif info_list[3] == 'age':
                        RESULT[tmp_info][1] = info_list[5]
                        print("Update {} succ.".format(info_list[1]))
                    elif info_list[3] == 'tel':
                        RESULT[tmp_info][2]  = info_list[5]
                        print("Update {} succ.".format(info_list[1]))
                    elif info_list[3] == 'email':
                        RESULT[tmp_info][3] = info_list[5]
                        print("Update {} succ.".format(info_list[1]))
                    else:
                        print('The input is wrong',
                              'pless:update monkey set name = mk,',
                              'pless:update monkey set age = 20,',
                              'pless:update monkey set tel = 177,',
                              'pless:update monkey set email = 111@qq.com.',
                              )
            print("-" * 50)
            for x in RESULT:
                print("{} {} {} {}".format(x[0], x[1], x[2], x[3]), end="\t")
                print()
                print("-" * 50)


    def list(self):
        '''查询模块'''
        #如果是空提示内容为空
        if len(RESULT) <= 1:
            print('User information is empty.')
        else:
            for x in RESULT:
                print("{} {} {} {}".format(x[0], x[1], x[2], x[3]), end="\t")
                print()
                print("-" * 50)


    def find(self,info_list):
        '''单个搜索模块'''
        action_info = info_list[1]
        userinfo_name = []
        for i in RESULT:
            userinfo_name.append(i[0])
        if action_info not in userinfo_name:
            print('User does not exist')
        else:
            for i in RESULT:
                if action_info in i:
                    tmp_info = RESULT.index(i)
            tmp_info = RESULT[tmp_info]
            for i in tmp_info:
                print("{} {} {} {}".format(i[0], i[1], i[2], i[3]), end="\t")
                print("-" * 50)


def main():
    user = Useradmin()
    for i in range(6):
        username = input("Please input your username: ")
        password = input("Please input your password: ")
        if username == USERINFO[0] and password == USERINFO[1]:
            print('Login successful')
            while True:
                info = input("Please input your operation: ")
                info_list = info.split()
                action = info_list[0]
                if action == "add":
                    user.add(info_list)
                elif action == 'delete':
                    user.delete(info_list)
                elif action == 'update':
                    user.update(info_list)
                elif action == 'list':
                    user.list()
                elif action == 'find':
                    user.find(info_list)
                elif action == "exit":
                    exit('by')
        else:
            print("Username or password error.")


if __name__ == '__main__':
    main()
