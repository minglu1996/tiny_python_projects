#!/usr/bin/env python3
#new commit
"""
Author : Minglu <john@localhost>
Date   : 2022-10-05
Purpose: Choose the correct article
"""
import argparse
# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's Nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word')

    return parser.parse_args()

def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    article = 'an' if word[0].lower() in 'aeiou' else 'a'
    print('Ahoy, Captain, {} {} off the larboard bow!' .format(article, word))



# --------------------------------------------------
if __name__ == '__main__':
    main()
