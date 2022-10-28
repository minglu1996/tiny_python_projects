#!/usr/bin/env python3
# Purpose: Jump Five

import argparse


def get_args():
    parser = argparse.ArgumentParser(description='Jump the Five',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('number',
                        metavar='str',
                        help='Input text'
                        )
    return parser.parse_args()


def main():
    args = get_args()
    number = args.number
    jumper = {'1': '9', '2': '8', '3': '7', '4': '6', '5': '0', '6': '4', '7': '3', '8': '2', '9': '1', '0': '5',
              '-': '-'}
    a = list(jumper.keys())
    for char in number:
        print(jumper.get(char, char), end='')


# for this task, I got stuck in the step which I don't know how to return the other letters which are not numbers. I used:
# if char in a:
# print(jumper[char])
# which can only process the numbers that you inputed. Until I saw 'Dict.get()' function. Then it made this task really easy and achieveable.

# phone = jumper[char]
# print(phone,end='')


# print(f'Call {print(jumper[char],end="")} today!')
# print(phone)
# print(args.number)
# print(jumper.get(char))
# print(type(a))
# print(jumper[char],end='')

# ---------
if __name__ == '__main__':
    main()
