#!/usr/bin/env python3
"""
Author : Minglu <john@localhost>
Date   : 2022-10-06
Purpose: choose the right article word
"""
import argparse
# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word')
    return parser.parse_args()
# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    word = args.word
    article = 'an' if word[0].lower() in 'aeiou' else 'a'
    print('Ahoy, Captain, {} {} off the larboard bow!'.format(article, word))
    #f'Ahoy, Captain, {article} {word} off the larboard bow!'
# --------------------------------------------------
if __name__ == '__main__':
    main()
