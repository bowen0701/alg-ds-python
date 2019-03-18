"""Leetcode 290. Word Pattern
Easy

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a 
letter in pattern and a non-empty word in str.

Example 1:
Input: pattern = "abba", str = "dog cat cat dog"
Output: true

Example 2:
Input: pattern = "abba", str = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false

Example 4:
Input: pattern = "abba", str = "dog dog dog dog"
Output: false

Notes:
You may assume pattern contains only lowercase letters, and str contains 
lowercase letters separated by a single space.
"""

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s = str.split(' ')
        if len(pattern) != len(s):
            return False
        
        d = {}
        for i, p in enumerate(pattern):
            if d.get(p, None):
                if d[p] != s[i]:
                    return False
            else:
                if s[i] in d.values():
                    return False
                d[p] = s[i]              
        return True


def main():
    pattern = "abba"
    str = "dog cat cat dog"    # Ans: True.
    output = Solution().wordPattern(pattern, str)
    print 'pattern: {0}; str: {1} => {2}'.format(pattern, str, output)

    pattern = "abba"
    str = "dog cat cat fish"    # Ans: False.
    output = Solution().wordPattern(pattern, str)
    print 'pattern: {0}; str: {1} => {2}'.format(pattern, str, output)

    pattern = "aaaa"
    str = "dog cat cat dog"    # Ans: False.
    output = Solution().wordPattern(pattern, str)
    print 'pattern: {0}; str: {1} => {2}'.format(pattern, str, output)

    pattern = "abba"
    str = "dog dog dog dog"    # Ans: False.
    output = Solution().wordPattern(pattern, str)
    print 'pattern: {0}; str: {1} => {2}'.format(pattern, str, output)

    pattern = "jquery"
    str = "jquery"    # Ans: False.
    output = Solution().wordPattern(pattern, str)
    print 'pattern: {0}; str: {1} => {2}'.format(pattern, str, output)


if __name__ == '__main__':
    main()
