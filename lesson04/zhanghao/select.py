from prettytable import PrettyTable
import log
import user

logger = log.my_log()


def list_user(filename):
    try:
        result = user.users(filename)
        xtb = PrettyTable()
        xtb.field_names = ["username", "age", "tel", "email"]
        for v in result.values():
            name = v["name"]
            age = v["age"]
            tel = v["tel"]
            email = v["email"]
            xtb.add_row([name, age, tel, email])
        print(xtb)
    except Exception as e:
        print(e)
        logger.error(e)
