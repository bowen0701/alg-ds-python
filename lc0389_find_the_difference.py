"""Leetcode 389. Find the Difference
Easy

URL: https://leetcode.com/problems/find-the-difference/

Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then 
add one more letter at a random position.

Find the letter that was added in t.

Example:
Input:
s = "abcd"
t = "abcde"
Output:
e
Explanation:
'e' is the letter that was added.
"""

class SolutionSortIter(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str

        Time complexity: O(n*logn).
        Space complexity: O(n).
        """
        # Sort s & t.
        s_ls = list(s)
        t_ls = list(t)
        s_ls.sort()
        t_ls.sort()

        # Iterate through s's chars to check mismatch.
        for i, c in enumerate(s_ls):
            if c != t_ls[i]:
                return t_ls[i]

        # If no mismatch, then the t's last char is the diff one.
        return t_ls[-1]


class SolutionCharCountDict(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str

        Time complexity: O(n).
        Space complexity: O(n).
        """
        from collections import defaultdict

        char_count_d = defaultdict(int)

        # Iterate through s's chars and increment counter.
        for c in s:
            char_count_d[c] += 1

        # Iterate through t's chars.
        for c in t:
            if not char_count_d[c]:
                # If c is not in s, c is additional char.
                return c
            else:
                # If c is in s, decrement its counter.
                char_count_d[c] -= 1


class SolutionOrdSumDiff(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str

        Time complexity: O(n).
        Space complexity: O(1).
        """
        ord_sum_diff = 0

        # Decrement ord_sum_diff by s's char ordinal.
        for c in s:
            ord_sum_diff -= ord(c)

        # Increment by t's char ordinal.
        for c in t:
            ord_sum_diff += ord(c)

        return chr(ord_sum_diff)


class SolutionXOR(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str

        Time complexity: O(n).
        Space complexity: O(1).
        """
        xor = 0

        # XOR by s's char ord.
        for c in s:
            xor ^= ord(c)

        # XOR by t's char ord.
        for c in t:
            xor ^= ord(c)

        return chr(xor)
        

def main():
    # Output: e
    s = "abcd"
    t = "abcde"
    print SolutionSortIter().findTheDifference(s, t)
    print SolutionCharCountDict().findTheDifference(s, t)
    print SolutionOrdSumDiff().findTheDifference(s, t)
    print SolutionXOR().findTheDifference(s, t)

    # Output: a
    s = ""
    t = "a"
    print SolutionSortIter().findTheDifference(s, t)
    print SolutionCharCountDict().findTheDifference(s, t)
    print SolutionOrdSumDiff().findTheDifference(s, t)
    print SolutionXOR().findTheDifference(s, t)


if __name__ == '__main__':
    main()
