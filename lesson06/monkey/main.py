

class User(object):

    def add(self, name, age, tel, email):
        pass

    def delete(self, name):
        pass

    def update(self, name, field, value):
        pass

    def find(self, name):
        pass

    def list(self):
        pass

    def display(self, page, pagesize=5):
        pass


class Auth(object):

    def login(self, username, password):
        pass

    def session(self):
        pass

    def logout(self):
        pass


class Persistence(object):

    def save(self):
        pass

    def load(self):
        pass


class DB(object):

    def __init__(self, host, username, password, port):
        self.host = host
        self.username = username
        self.password = password
        self.port = port

    def select(self, sql):
        pass

    def insert(self, sql):
        pass

    def update(self, sql):
        pass

    def delete(self, sql):
        pass


def logic():
    pass

def main():
    logic()


main()