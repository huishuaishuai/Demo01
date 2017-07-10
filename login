#!/usr/bin/env python3

import sys
import time


def main():
    user_name = input('Login:')
    if user_name == 'hui':
        password = input('Password:')
        if password == '123456':
            print('Login successfully')
            time.sleep(60)
            sys.exit()
        else:
            print('Exit, password wrong!')
            sys.exit(1)
    else:
        print('Exit, account wrong!')
        sys.exit(1)


if __name__ == '__main__':
    main()