import csv
import json
import log

FILENAME = "51reboot.txt"
CSVFILE = "51reboot.csv"
RESULT = []

logger = log.my_log()


def dataToCsv(filename):
    with open(FILENAME, 'r') as f:
        result = f.read()
        if not result:
            msg = "\033[0;31;1m{} is none.\033[0m".format(FILENAME)
            print(msg)
            logger.error(msg)
        else:
            result = json.loads(result)
            for i in result.keys():
                name = result[i]["name"]
                age = result[i]["age"]
                tel = result[i]["tel"]
                email = result[i]["email"]
                RESULT.append([name, age, tel, email])
    csvFile = open(filename, 'w', newline='')
    try:
        writer = csv.writer(csvFile)
        writer.writerow(("name", "age", "tel", 'email'))
        for info in RESULT:
            writer.writerow((info[0], info[1], info[2], info[3]))
    except Exception as e:
        print(e)
    finally:
        csvFile.close()


dataToCsv(CSVFILE)
