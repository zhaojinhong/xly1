from prettytable import PrettyTable
import log
import user

logger = log.my_log()


def find_user(user_info, filename):
    try:
        username = user_info[1]
        find_flag = False
        result = user.users(filename)
        usernames = result.keys()
        xtb = PrettyTable()
        xtb.field_names = ["username", "age", "tel", "email"]
        if username in usernames:
            name = result[username]["name"]
            age = result[username]["age"]
            tel = result[username]["tel"]
            email = result[username]["email"]
            xtb.add_row([name, age, tel, email])
            find_flag = True
            print(xtb)
        if not find_flag:
            print("\033[0;31;1muser {} not found.\033[0m".format(username))
            msg = "user {} not found.".format(username)
            logger.error(msg)
    except Exception as e:
        print(e)
        logger.error(e)
