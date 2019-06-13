import save
import log
import user

logger = log.my_log()


def update_user(user_info, filename):
    username = user_info[1]
    try:
        keyword = user_info[2]
        field = user_info[3]
        new_value = user_info[-1]
        mark = user_info[-2]
        if keyword != "set" or mark != "=":
            print("\033[0;31;1mupdate method error.\033[0m")
            msg = "update method error."
            logger.error(msg)
        else:
            result = user.users(filename)
            usernames = result.keys()
            if username in usernames:
                if field == "age":
                    result[username]["age"] = new_value
                    save.save_user(result, filename)
                    print("\033[0;31;1mupdate {} age success.\033[0m".format(username))
                    msg = "update {} age success.".format(username)
                    logger.error(msg)
                elif field == "tel":
                    result[username]["tel"] = new_value
                    save.save_user(result, filename)
                    print("\033[0;31;1mupdate {} tel success.\033[0m".format(username))
                    msg = "update {} tel success.".format(username)
                    logger.error(msg)
                elif field == "email":
                    result[username]["email"] = new_value
                    save.save_user(result, filename)
                    print("\033[0;31;1mupdate {} email success.\033[0m".format(username))
                    msg = "update {} email success.".format(username)
                    logger.error(msg)
                else:
                    print("\033[0;31;1mupdate field {} not found.\033[0m".format(field))
                    msg = "update field {} success.".format(field)
                    logger.error(msg)
            else:
                print("\033[0;31;1muser {} not found.\033[0m".format(username))
                msg = "user {} not found.".format(username)
                logger.error(msg)
    except Exception as e:
        print(e)
        logger.error(e)
