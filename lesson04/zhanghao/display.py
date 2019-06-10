from prettytable import PrettyTable
import log
import user

logger = log.my_log()


def display(user_info, filename):
    try:
        xtb = PrettyTable()
        xtb.field_names = ["username", "age", "tel", "email"]
        RESULT = []
        page = int(user_info[2])
        pagesize = 5
        start = (page - 1) * pagesize
        end = page * pagesize
        result = user.users(filename)
        for k in result.keys():
            name = result[k]["name"]
            age = result[k]["age"]
            tel = result[k]["tel"]
            email = result[k]["email"]
            RESULT.append([name, age, tel, email])
        for i in RESULT[start:end]:
            xtb.add_row(i)
        print(xtb)
    except Exception as e:
        print(e)
        logger.error(e)
