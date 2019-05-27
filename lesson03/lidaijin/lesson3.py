"""
1. 登录认证；
2. 增删改查和搜索
    3.1 增 add           # add monkey 12 132xxx monkey@51reboot.com
    3.2 删 delete        # delete monkey
    3.3 改 update        # update monkey set age = 18
    3.4 查 list          # list
    3.5 搜 find          # find monkey
3. 格式化输出
"""
import sys
from prettytable import PrettyTable


USERINFO = ("test","123456")
INIT_FAIL_CNT = 0
MAX_FAIL_CNT = 6
RESULT = {}


while INIT_FAIL_CNT < MAX_FAIL_CNT:
    username = input("Please input your username: ")
    password = input("Please input your password: ")

    if username == USERINFO[0] and password == USERINFO[1]:
        while True:
            info = input("Please input your operation:")
            info_list = info.split()
            peration = info_list[0]

            if peration == "add":
                if len(info_list) == 5:
                    if info_list[1] not in RESULT:
                        content = {"age":info_list[2],"tel":info_list[3],"emial":info_list[4]}
                        RESULT[info_list[1]] = content
                        print("Added {} user successfully".format(info_list[1]))
                    else:
                        print("User {} exists".format(info_list[1]))
                else:
                    print("Grammar mistakes")
            elif peration == "delete":
                if len(info_list) == 2:
                    if info_list[1] in RESULT:
                        RESULT.pop(info_list[1])
                        print("Delete user {} succeeded".format(info_list[1]))
                    else:
                        print("User {} does not exist".format(info_list[1]))
                else:
                    print("Grammar mistakes")
            elif peration == "update":
                if len(info_list) == 6:
                    if info_list[1] in RESULT:
                        if  info_list[2] == "set" and info_list[-2] == "=":
                            RESULT[info_list[1]][info_list[3]] = info_list[-1]
                        else:
                            print("Grammar mistakes")
                    else:
                        print("User {} does not exist".format(info_list[1]))
                else:
                    print("Grammar mistakes")
            elif peration == "list":
                li,t2 = [],[]
                xtb = PrettyTable()
                xtb.field_names = ["username", "age", "tel", "email"]
                for i in RESULT.values():
                    b = i.values()
                    #t = list(b)

                for x in RESULT.keys():
                    t = list(b)
                    #t.insert(0, x)
                    if x not in t2:
                        t.insert(0, x)
                        t2 = t
                        #t.insert(0,x)
                        li.append(t)

                for x in li:
                    xtb.add_row(x)

                print(xtb)

            elif peration == "find":
                if len(info_list) == 2:
                    xtb = PrettyTable()
                    xtb.field_names = ["username", "age", "tel", "email"]
                    if info_list[1] in RESULT:
                        test = list(RESULT[info_list[1]].values())
                        #print(test)
                        test.insert(0,info_list[1])
                        xtb.add_row(test)
                        print(xtb)
                    #print(RESULT[info_list[1]])
                    else:
                        print("User {} does not exist".format(info_list[1]))
                else:
                    print("Grammar mistakes")

            elif peration == "exit":
                sys.exit()
            else:
                print("The input is invalid")

    else:
        INIT_FAIL_CNT += 1
        print("username or password error.")
