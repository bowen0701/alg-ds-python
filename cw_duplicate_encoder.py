"""Codewars: Duplicate Encoder
6 kyu

URL: https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/

The goal of this exercise is to convert a string to a new string where
each character in the new string is "(" if that character appears only once
in the original string, or ")" if that character appears more than once in
the original string. Ignore capitalization when determining if a character
is a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 
"""

def duplicate_encode(word):
    from collections import defaultdict

    # Convert word to lower case.
    word_lower = word.lower()

    # Create a dict to accumulate char numbers.
    char_nums = defaultdict(int)

    for c in word_lower:
        char_nums[c] += 1

    # Create a duplicate encoder based on char number dict.
    encoder = [''] * len(word)

    for i, c in enumerate(word_lower):
        # There are duplicates in char c.
        if char_nums[c] > 1:
            encoder[i] = ')'
        else:
            encoder[i] = '('

    return ''.join(encoder)


def main():
    # "din"      =>  "((("
    word = "din"
    print duplicate_encode(word)

    # "recede"   =>  "()()()"
    word = "recede"
    print duplicate_encode(word)

    # "Success"  =>  ")())())"
    word = "Success"
    print duplicate_encode(word)

    # "(( @"     =>  "))((" 
    word = "(( @"
    print duplicate_encode(word)


if __name__ == '__main__':
    main()
