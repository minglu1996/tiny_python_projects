#!/usr/bin/env python3
"""
Author : Minglu <mingluxie@gmail.com>
Date   : 2022-11-06
Purpose: Howler (upper-cases input)
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler (upper-cases input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    if args.outfile:
        outfile = args.outfile
        name_out = os.path.basename(outfile)
        # print(name_out)
        if os.path.isfile(text):
            text = open(text).read().rstrip()
        print(text.upper(), file=open(name_out, 'wt'))
        # open(name_out,'wt').write(text.upper())
        # print(text_real, file= open(name_out, 'wt'))
    else:
        if os.path.isfile(text):
            text = open(text).read().rstrip()
        print(text.upper())


# --------------------------------------------------
if __name__ == '__main__':
    main()
