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

class SolutionRecurNaive(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int

        Apply recursion.

        Time complexity: O(2^n).
        Space complexity: O(n).
        """
        if not s:
            return 1

        if s[0] == '0':
            return 0

        # Since s[0] is valid, decode s by decoding s[1:].
        n_ways = self.numDecodings(s[1:])

        # If len of s is larger than 2 and the first 2 chars are valid,
        # further decode s by s[2:].
        if len(s) >= 2 and '10' <= s[:2] <= '26':
            n_ways += self.numDecodings(s[2:])

        return n_ways


class SolutionRecur(object):
    def numDecodingsUtil(self, s, k):
        """Helper function for numDecodings."""
        # Check the last k chars.
        if k == 0:
            return 1

        # Check the start of the last k chars is valid.
        start = len(s) - k
        if s[start] == '0':
            return 0

        # Since start of the last k chars is valid, 
        # decode s by decoding the last (k - 1) chars.
        n_ways = self.numDecodingsUtil(s, k - 1)

        # If the len of the last k chars is larger than 2, 
        # and the first 2 chars are valid, 
        # further decode the last (k - 2) chars.
        if k >= 2 and '10' <= s[start:(start + 2)] <= '26':
            n_ways += self.numDecodingsUtil(s, k - 2)

        return n_ways

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int

        Apply recursion with pointer method without copying lists.

        Time complexity: O(2^n).
        Space complexity: O(1).
        """ 
        return self.numDecodingsUtil(s, len(s))


class SolutionMemo(object):
    def numDecodingsUtil(self, s, k, T):
        # Check the last k chars.
        if T[k]:
            return T[k]

        if k == 0:
            return 1

        # Check the start of the last k chars is valid.
        start = len(s) - k
        if s[start] == '0':
            return 0

        # Since start of the last k chars is valid, 
        # decode s by decoding the last (k - 1) chars.
        result = self.numDecodingsUtil(s, k - 1, T)

        # If the len of the last k chars is larger than 2, 
        # and the first 2 chars are valid, 
        # further decode the last (k - 2) chars.
        if k >= 2 and '10' <= s[start:(start + 2)] <= '26':
            result += self.numDecodingsUtil(s, k - 2, T)

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
        T = [None] * (n + 1)
        return self.numDecodingsUtil(s, n, T)


class SolutionDP(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int

        Apply bottom-up dynamic progromming.

        Time complexity: O(n).
        Space complexity: O(n).
        """
        # If empty string, decode in 1 way.
        if not s:
            return 1

        # Check s[0] is valid.
        if s[0] == '0':
            return 0

        n = len(s)

        # Apply bottom-up dynamic programming.
        T = [0] * (n + 1)
        # For (1) empty string and (2) the 1st char is valid, decode in 1 way.
        T[0] = 1
        T[1] = 1
        
        for i in range(2, n + 1):
            if s[i - 1] != '0':
                # If the previous 1 char is valid, add its decode ways.
                T[i] += T[i - 1]
            if '10' <= s[(i - 2):i] <= '26':
                # If the previous 2 chars are valid, further add its decode ways.
                T[i] += T[i - 2]
        
        return T[-1]


class SolutionIter(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int

        Apply bottom-up iteration

        Time complexity: O(n).
        Space complexity: O(1).
        """
        # If empty string, decode in 1 way.
        if not s:
            return 1

        # Check s[0] is valid.
        if s[0] == '0':
            return 0

        n = len(s)
        # For (a) empty string and (b) the 1st char is valid, decode in 1 way.
        a, b = 1, 1

        for i in range(2, n + 1):
            c = 0
            if s[i - 1] != '0':
                # If the previous 1 char is valid, add its decode ways.
                c += b
            if '10' <= s[(i - 2):i] <= '26':
                # If the previous 2 chars are valid, further add its decode ways.
                c += a

            a, b = b, c

        return b


def main():
    import time

    s = '110' # Should be 1 = #{(1,10)}.

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

    print '==='
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

    print '==='
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
