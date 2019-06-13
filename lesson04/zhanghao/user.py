import log
import json

logger = log.my_log()


def users(filename):
    with open(filename, 'r') as f:
        result = f.read()
        if not result:
            print("\033[0;31;1m{} is none.\033[0m".format(filename))
            msg = "{} is none.".format(filename)
            logger.error(msg)
            result = {}
        else:
            result = json.loads(result)
    return result
