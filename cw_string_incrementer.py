"""Codewars: String incrementer
5 kyu

URL: https://www.codewars.com/kata/54a91a4883a7de5d7800009c

Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the
new string.

Examples:
foo -> foo1
foobar23 -> foobar24
foo0042 -> foo0043
foo9 -> foo10
foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.
"""


def increment_string(strng):
    pass


def main():
    # Output: 'foo1'
    strng = 'foo'
    print increment_string(strng)

    # Output: 'foobar002'
    strng = 'foobar001'
    print increment_string(strng)

    # Output: 'foobar2'
    strng = 'foobar1'
    print increment_string(strng)

    # Output: 'foobar01'
    strng = 'foobar00'
    print increment_string(strng)

    # Output: 'foobar100'
    strng = 'foobar99'
    print increment_string(strng)

    # Output: 'foobar100'
    strng = 'foobar099'
    print increment_string(strng)

    # Output: '1'
    strng = ''
    print increment_string(strng)


if __name__ == '__main__':
    main()
