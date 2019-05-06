from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


NUM_CHARS = 26


def _get_char_counts(s):
    char_counts = [0] * NUM_CHARS
    for c in s:
        pos = ord(c) - ord('a')
        char_counts[pos] += 1
    return char_counts


def _get_char_diff(char_counts1, char_counts2):
    char_diff = 0
    for i in range(NUM_CHARS):
        char_diff += abs(char_counts1[i] - char_counts2[i])
    return char_diff


def anagram_making(s1, s2):
    """Anagram making.
    
    Count how many characters we need to remove to make anagram.
    """
    char_counts1 = _get_char_counts(s1)
    char_counts2 = _get_char_counts(s2)
    char_diff = _get_char_diff(char_counts1, char_counts2)
    return char_diff


def main():
    s1 = 'hello'
    s2 = 'billion'
    # Ans: anagram: 'llo', thus 2 + 4 = 6.
    print('Anagram making: {}'.format(anagram_making(s1, s2)))


if __name__ == '__main__':
    main()
