"""Leetcode 344. Reverse String
Easy

URL: https://leetcode.com/problems/reverse-string/

Write a function that reverses a string.
The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying
the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

Example 1:
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""

class SolutionTwoPointers(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.

        Time complexity: O(n).
        Space complexity: O(1).
        """
        # Apply two pointer method.
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


def main():
    # Output: ["o","l","l","e","h"]
    s = ["h","e","l","l","o"]
    SolutionTwoPointers().reverseString(s)
    print s

    # Output: ["h","a","n","n","a","H"]
    s = ["H","a","n","n","a","h"]
    SolutionTwoPointers().reverseString(s)
    print s

if __name__ == '__main__':
    main()
