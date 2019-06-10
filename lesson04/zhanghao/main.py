import sys
import os
import add
import delete
import update
import select
import find
import display
import log
import login

logger = log.my_log()

FILENAME = "51reboot.txt"

if not os.path.exists(FILENAME):
    f = open(FILENAME, 'w')
    f.close()


def main():
    login_flag = login.login()
    if login_flag:
        print("\033[0;31;1mlogin success.\033[0m")
        title = '''
        1.1 增 add        # add monkey 12 188*** monkey@51reboot.com
        1.2 删 delete     # delete monkey
        1.3 改 update     # update monkey set age = 20
        1.4 查 list       # list
        1.5 搜 find       # find monkey
        1.6 分页 display  # display page 1
            '''
        print(title)
        while True:
            try:
                info = input("Please input your operation：")
                info_list = info.strip().split()
                action = info_list[0]
                if action == "add":
                    add.add_user(info_list, FILENAME)
                elif action == "delete":
                    delete.del_user(info_list, FILENAME)
                elif action == "update":
                    update.update_user(info_list, FILENAME)
                elif action == "list":
                    select.list_user(FILENAME)
                elif action == "find":
                    find.find_user(info_list, FILENAME)
                elif action == "display":
                    display.display(info_list, FILENAME)
                elif action == "exit":
                    sys.exit(0)
                else:
                    print("\033[0;31;1minvalid operation.\033[0m")
                    logger.error("invalid operation.\n")
            except Exception as e:
                print(e)
                logger.error(e)
    if not login_flag:
        print("\n\033[0;31;1mInput {} times failed,Terminal will exit.\033[0m".format(6))
        sys.exit(0)


if __name__ == '__main__':
    main()
