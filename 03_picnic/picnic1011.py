#!/usr/bin/env python3
"""
Author : minglu <john@localhost>
Date   : 2022-10-11
Purpose: Picnic game
"""

import argparse
# --------------------------------------------------


def get_arg():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('item',
                        metavar='str',
                        nargs='+',
                        help='Item(s) to bring'
                        )
    parser.add_argument('-s',
                        '--sorted',
                        action="store_true",
                        default=False,
                        help='Sort the items')
    return parser.parse_args()

# --------------------------------------------------


def main():
    args = get_arg()
    item = args.item
    num = len(item)

    if args.sorted:
        item.sort()

    if num == 1:
        print("You are bringing {}.".format(item[0]))
    elif num == 2:
        print("You are bringing {} and {}.".format(item[0], item[1]))
    elif num == 3:
        print(
            "You are bringing {}, {}, and {}.".format(
                item[0],
                item[1],
                item[2]))
    else:
        print("You are bringing {}, {}, {}, and {}.".format(
            item[0], item[1], item[2], item[-1]))


# --------------------------------------------------
if __name__ == '__main__':
    main()
