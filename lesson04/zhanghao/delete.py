import save
import log
import user

logger = log.my_log()


def del_user(user_info, filename):
    username = user_info[1]
    result = user.users(filename)
    usernames = result.keys()
    delete_flag = False
    if username in usernames:
        result.pop(username)
        save.save_user(result, filename)
        print("\033[0;31;1muser {} remove success.\033[0m".format(username))
        msg = "user {} remove success.".format(username)
        logger.error(msg)
        delete_flag = True
    if not delete_flag:
        print("\033[0;31;1muser {} not found.\033[0m".format(username))
        msg = "user {} not found.".format(username)
        logger.error(msg)
    return result
