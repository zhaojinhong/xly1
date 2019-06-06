import json


def save_user(result, filename):
    with open(filename, 'w') as f:
        f.write(json.dumps(result))
