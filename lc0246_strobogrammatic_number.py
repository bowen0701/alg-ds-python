"""Leetcode 246. Strobogrammatic Number
Easy

URL: https://leetcode.com/problems/strobogrammatic-number/A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is
represented as a string.

Example 1:
Input:  "69"
Output: true

Example 2:
Input:  "88"
Output: true

Example 3:
Input:  "962"
Output: false
"""


class SolutionMapDictIter(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool

        Time complexity: O(n).
        Space complexity: O(n).
        """
        if not num:
            return True

        # Reverse num.
        rev_num = num[::-1]

        # Convert to mapped number or empty string.
        map_d = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }

        mapped_num_ls = []
        for n in rev_num:
            if n in map_d:
                mapped_num_ls.append(map_d[n])
            else:
                mapped_num_ls.append(' ')
        mapped_num = ''.join(mapped_num_ls)

        # Check if strobogrammatic.
        return mapped_num == num


class SolutionTwoPointersIter(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool

        Time complexity: O(n).
        Space complexity: O(1).
        """
        if not num:
            return True

        # Use two pointers from two sides: left & right.
        left, right = 0, len(num) - 1

        # Create mapping table.
        map_d = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }

        # Check if two pointers's char can be mapped.
        # If yes, move two pointers to middle; if not return False.
        while left <= right:
            if num[right] not in map_d or num[left] != map_d[num[right]]:
                return False

            left += 1
            right -= 1

        return True


def main():
    # Output: true
    num = "69"
    print SolutionMapDictIter().isStrobogrammatic(num)
    print SolutionTwoPointersIter().isStrobogrammatic(num)

    # Output: true
    num = "88"
    print SolutionMapDictIter().isStrobogrammatic(num)
    print SolutionTwoPointersIter().isStrobogrammatic(num)

    # Output: false
    num = "962"
    print SolutionMapDictIter().isStrobogrammatic(num)
    print SolutionTwoPointersIter().isStrobogrammatic(num)

    # Output: false
    num = "2"
    print SolutionMapDictIter().isStrobogrammatic(num)
    print SolutionTwoPointersIter().isStrobogrammatic(num)


if __name__ == '__main__':
    main()
