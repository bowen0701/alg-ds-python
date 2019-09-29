"""Codewars: Find the unique number
6 kyu

URL: https://www.codewars.com/kata/find-the-unique-number-1/

There is an array with some numbers. All numbers are equal except for one.
Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55

It's guaranteed that array contains more than 3 numbers.

The tests contain some very huge arrays, so think about performance.

This is the first kata in series:
- Find the unique number (this kata)
- Find the unique string
- Find The Unique
"""

def find_uniq(arr):
    """
    Use dict to collect number counts.

    Time complexity: O(n).
    Space complexity: O(1).
    """
    from collections import defaultdict

    num_counts = defaultdict(int)

    for num in arr:
        num_counts[num] += 1

    for num, count in num_counts.items():
        if count == 1:
            n = num

    return n


def main():
    # Output: 2
    arr = [ 1, 1, 1, 2, 1, 1 ]
    print find_uniq(arr)

    # Output: 0.55
    arr = [ 0, 0, 0.55, 0, 0 ]
    print find_uniq(arr)


if __name__ == '__main__':
    main()
