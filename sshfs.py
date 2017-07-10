#!/usr/bin/env python3

import pexpect


def ssh():
    child = pexpect.spawn('login')
    try:
        index = child.expect(['Login:', 'Password:'])
        if index == 0:
            print('********************0')
            print(child.before)
            print(child.after)
            child.sendline('hui')
            i = child.expect(['Login:', 'Password:'])
            print('***************************************', i)
            # print(child)
            print(child.before)
            print(child.after)
            child.sendline('123456')
            ind = child.expect('Login successfully')
            print('88888888888888888888888888888888888888888', ind)
            print(child.before)
            print(child.after)
        elif index == 1:
            print('********************1')
    except Exception as e:
        print('EOF: error')


def main():
    ssh()


if __name__ == '__main__':
    main()
