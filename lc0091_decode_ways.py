"""Leetcode 91. Decode Ways
Medium

URL: https://leetcode.com/problems/decode-ways/

A message containing letters from A-Z is being encoded to numbers using the
following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26

Given a non-empty string containing only digits, determine the total number
of ways to decode it.

Example 1:
Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""

class SolutionRecurNaive(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int

        Apply recursion.

        Time complexity: O(2^n).
        Space complexity: O(n).
        """
        # Base case.
        if not s:
            return 1

        # Check 1 digit: if the start char is not valid.
        if s[0] == '0':
            return 0

        # If valid, decode the remaining string after 1 digit.
        n_ways = self.numDecodings(s[1:])

        # Check 2 digits: if len of s >= 2 and first 2 chars are valid,
        # decode the remaining string after 2 digits.
        if len(s) >= 2 and '10' <= s[:2] <= '26':
            n_ways += self.numDecodings(s[2:])

        return n_ways


class SolutionRecur(object):
    def _decodeRecur(self, s, k):
        """Recursively decode the last k chars."""
        # Base case.
        if k == 0:
            return 1

        # Check 1 digit: if the start of the last k chars is not valid.
        start = len(s) - k
        if s[start] == '0':
            return 0

        # If valid, decode the last (k - 1) chars.
        n_ways = self._decodeRecur(s, k - 1)

        # Check 2 digits: if k >= 2 and first 2 chars are valid,
        # decode the last (k - 2) chars.
        if k >= 2 and '10' <= s[start:(start + 2)] <= '26':
            n_ways += self._decodeRecur(s, k - 2)

        return n_ways

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int

        Apply recursion with pointer method without copying lists.

        Time complexity: O(2^n).
        Space complexity: O(1).
        """
        n = len(s)
        return self._decodeRecur(s, n)


class SolutionMemo(object):
    def _decodeRecur(self, s, k, T):
        """Recursively check the last k chars."""
        # Base case.
        if k == 0:
            return 1

        # Check 1 digit: if the start of the last k chars is not valid.
        start = len(s) - k
        if s[start] == '0':
            return 0

        # Check memo table.
        if T[k]:
            return T[k]

        # If valid, decode the remaining (k - 1) chars.
        result = self._decodeRecur(s, k - 1, T)

        # Check 2 digits: if k >= 2 and first 2 chars are valid, 
        # decode the remaining (k - 2) chars.
        if k >= 2 and '10' <= s[start:(start + 2)] <= '26':
            result += self._decodeRecur(s, k - 2, T)

        T[k] = result
        return result

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int

        Apply top-down dynamic progromming by memoization.

        Time complexity: O(n).
        Space complexity: O(n).
        """
        n = len(s)
        T = [0] * (n + 1)
        return self._decodeRecur(s, n, T)


class SolutionDP(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int

        Apply bottom-up dynamic progromming.

        Time complexity: O(n).
        Space complexity: O(n).
        """
        # Base case.
        if not s:
            return 1

        # Check if the 1st char is not valid.
        if s[0] == '0':
            return 0

        n = len(s)
        T = [0] * (n + 1)

        # For empty string and the valid 1st char, decode in 1 way.
        T[0] = 1
        T[1] = 1
        
        for i in range(2, n + 1):
            # Check 1 digit: if the previous 1 char is valid, add to result.
            if s[i - 1] != '0':
                T[i] += T[i - 1]

            # Check 2 digits: if the previous 2 are valid, add to result.
            if '10' <= s[(i - 2):i] <= '26':
                T[i] += T[i - 2]
        
        return T[-1]


class SolutionIter(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int

        Apply bottom-up iteration.

        Time complexity: O(n).
        Space complexity: O(1).
        """
        # Base case.
        if not s:
            return 1

        # Check if s[0] is not valid.
        if s[0] == '0':
            return 0

        n = len(s)

        # For empty string and the valid 1st char, decode in 1 way.
        a, b = 1, 1

        for i in range(2, n + 1):
            c = 0

            # Check 1 digit: if the previous 1 char is valid, add to result.
            if s[i - 1] != '0':
                c += b

            # Check 2 digits: if the previous 2 are valid, add to result.
            if '10' <= s[(i - 2):i] <= '26':
                c += a

            a, b = b, c

        return b


def main():
    import time

    s = '12' # Should be 2 = #{(1,2), (12)}.

    start_time = time.time()
    print 'By naive recur: {}'.format(SolutionRecurNaive().numDecodings(s))
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'By recur: {}'.format(SolutionRecur().numDecodings(s))
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'By memo: {}'.format(SolutionMemo().numDecodings(s))
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'By DP: {}'.format(SolutionDP().numDecodings(s))
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'By iter: {}'.format(SolutionIter().numDecodings(s))
    print 'Time: {}'.format(time.time() - start_time)

    print '---'

    s = '226' # Should be 3 = #{(2,2,6), (22,6), (2,26)}

    start_time = time.time()
    print 'By naive recur: {}'.format(SolutionRecurNaive().numDecodings(s))
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'By recur: {}'.format(SolutionRecur().numDecodings(s))
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'By memo: {}'.format(SolutionMemo().numDecodings(s))
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'By DP: {}'.format(SolutionDP().numDecodings(s))
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'By iter: {}'.format(SolutionIter().numDecodings(s))
    print 'Time: {}'.format(time.time() - start_time)


if __name__ == '__main__':
    main()
