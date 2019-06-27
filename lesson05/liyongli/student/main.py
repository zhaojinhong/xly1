# -*- coding:utf-8 -*-
# author: lyl
import user_expand


def main():
    init_fail_count = 0
    max_fail_count = 3
    while init_fail_count < max_fail_count:
        username = input("Please input your login username: ")
        password = input("Please input your login password: ")
        if user_expand.auth(username, password):
            print("\n\tWelcome to user magage system.\n")
            user_expand.logic()
        else:
            print("username or password valid failed.")
            init_fail_count += 1
    print("Game Over.")


if __name__ == '__main__':
    main()
