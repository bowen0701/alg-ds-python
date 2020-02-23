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


def _add_one(nums):
    """Add one to nums."""
    from collections import deque

    nums = deque(nums)
    n = len(nums)
    carry = 1
    for i in reversed(range(n)):
        add = carry + int(nums[i])
        carry, nums[i] = add // 10, str(add % 10)
    
    if carry:
        nums.appendleft(str(carry))
    
    return list(nums)


def increment_string(strng):
    """Increment string."""
    # Edge case.
    if not strng:
        return '1'
  
    # Find the 1st position from reverse where it's not digit.
    index = -1
    for i in reversed(range(len(strng))):
        if not strng[i].isdigit():
            index = i
            break

    # Separate strng into char and number strings.    
    char_str = strng[:index+1]
    num_str = strng[index+1:]
    
    # Add one to number string.
    if not num_str:
        num_str = '1'
    else:
        nums_add_one = _add_one(num_str)
        num_str = ''.join(nums_add_one)
    
    return char_str + num_str


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
