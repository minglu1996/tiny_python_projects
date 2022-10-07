#!/usr/bin/env python3
# !/usr/bin/python3
################################################
#  File Name:hello.py
#  Author: Minglu.Xie
#  Mail: mingluxie@gmail.com
#  Created Time: Wed 05 Oct 2022 01:54:43 PM CEST
################################################
#!/home/john/miniconda3/bin/python
# purpose: Say hello

import argparse


def get_args():
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n', '--name', metavar='name',
                        default='World', help='Name to greet')
    return parser.parse_args()

def main():
    args = get_args()
    print('Hello, ' + args.name + '!')


if __name__ == '__main__':
    main()
