#!/usr/bin/env python3
"""
Author : minglu <mingluxie@gmail.com>
Date   : 2022-10-08
Purpose: Picnic game
"""
import argparse
# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('Item',
                        metavar='str',
                        nargs='+',
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                        action='store_true')

    return parser.parse_args()
# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    Item = args.Item
    num = len(Item)

    if args.sorted:
        Item = sorted(Item)

    if num <= 1:
        print(f'You are bringing {Item[0]}.')
    elif num <3:
        print(f"You are bringing {' and '.join(Item)}.")
    elif num <4:
        print(f"You are bringing {', '.join(Item)}.")
    else:
        print(f"You are bringing {', '.join(Item[:3])}, and {Item[-1]}.")
##now it is time to make sorted flag to work properly


    #print(f'You are bringing {Item}.')
    #print('You are bringing {}.'.format(Item))
# --------------------------------------------------
if __name__ == '__main__':
    main()
