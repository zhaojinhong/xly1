# git pull --rebase origin master
# git push -u origin master

import sys

flag = 0
user_info = ["51reboot","123456"]
user_list = ["lesson01","lesson02"]

def add_user():
    user_add = input("Please enter the user to join")
    if user_add in user_list:
        print("The user is exist")
    else:
        user_list.append(user_add)
        exit


while 1:
    try:
        username = input("please input username: ")
        password = input("plese input password: ")
        if username == user_info[0] and password == user_info[1]:
            flag = 1
            print('Welcome back：',username)
            cmd = input("\033[32;1mPlease input will run command: \033[0m")
            if flag == 1 and cmd == "add":
                print(cmd)
                add_user()
                break
            elif flag == 1 and cmd == "delete":
                print(cmd)
            elif flag == 1 and cmd == "update":
                print(cmd)
            elif flag == 1 and cmd == "list":
                print(cmd)
            elif flag == 1 and cmd == "find":
                print(cmd)
            elif flag == 1 and cmd == "exit":
                break
            else:
                break
        else:
            print('username or password is wrong')
            break
    except KeyboardInterrupt:
        print("\n\033[31;1mbye bye!\033[0m")
        break
