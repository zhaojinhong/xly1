import log

USERINFO = ("51reboot", "123456")

logger = log.my_log()


def login():
    login_flag = False
    for i in range(10):
        if i < 6:
            username = input("Please input your username：")
            password = input("Please input your password：")
            if username == USERINFO[0] and password == USERINFO[1]:
                login_flag = True
                break
            else:
                print("\033[0;31;1musername or password error.\033[0m")
                logger.error("username or password error.")
        else:
            msg = "Input {} times failed,Terminal will exit.".format(6)
            logger.error(msg)
            break
    return login_flag