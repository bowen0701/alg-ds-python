"""Leetcode 91. Decode Ways
Medium

URL: https://leetcode.com/problems/decode-ways/

A message containing letters from A-Z is being encoded to numbers using the
following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26

Given a non-empty string containing only digits, determine the total number of 
ways to decode it.

Example 1:
Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""

class SolutionRecur(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 1
        if len(s) == 1:
            if s[0] == '0':
                return 0
            else:
                return 1

        # For string with length >= 2, mimic Fibonacci series.
        if s[0] > '0':
            if '10' <= s[:2] <= '26':
                return self.numDecodings(s[1:]) + self.numDecodings(s[2:])
            else:
                return self.numDecodings(s[1:])
        else:
            return 0


def main():
    s = '12' # Should be 2 = #{1,2; 12}.
    print SolutionRecur().numDecodings(s)

    s = '226' # Should be 3 = #{2,2,6; 22,6; 2,26}
    print SolutionRecur().numDecodings(s)

    s = '27' # Should be 1 = #{2,7}
    print SolutionRecur().numDecodings(s)

    s = '1111' # Should be 5 = #{1,1,1,1; 1,11,1; 1,1,11; 11,1,1; 11,11}
    print SolutionRecur().numDecodings(s)


if __name__ == '__main__':
    main()
