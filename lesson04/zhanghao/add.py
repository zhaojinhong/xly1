import save
import log
import user

logger = log.my_log()


def add_user(user_info, filename):
    username = user_info[1]
    field = {}
    try:
        field["name"] = user_info[1]
        field["age"] = user_info[2]
        field["tel"] = user_info[3]
        field["email"] = user_info[4]
        result = user.users(filename)
        usernames = result.keys()
        if username in usernames:
            print("\033[0;31;1muser {} already exists.\033[0m".format(username))
            msg = "user {} already exists.".format(username)
            logger.error(msg)
        else:
            result[username] = field
            save.save_user(result, filename)
            print("\033[0;31;1muser {} add success.\033[0m".format(username))
            msg = "user {} add success.".format(username)
            logger.error(msg)
    except Exception as e:
        print(e)
        logger.error(e)
