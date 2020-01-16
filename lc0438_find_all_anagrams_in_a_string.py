"""Leetcode 438. Find All Anagrams in a String
Medium

URL: https://leetcode.com/problems/find-all-anagrams-in-a-string/

Given a string s and a non-empty string p, find all the start indices of p's
anagrams in s.

Strings consists of lowercase English letters only and the length of both strings
s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:
Input:
s: "cbaebabacd" p: "abc"
Output:
[0, 6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input:
s: "abab" p: "ab"
Output:
[0, 1, 2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""

class SolutionCharCountListSlidingWindow(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]

        Time complexity: O(n), where n is length of s.
        Space complexity: O(1).
        """
        # Edge case.
        if not s or len(s) < len(p):
            return []

        result = []

        len_p = len(p)
        len_s = len(s)

        # Create array of length 26 to aggregate char's count for p.
        p_char_counts = [0] * 26
        for i in range(len_p):
            p_char_counts[ord(p[i]) - ord('a')] += 1

        # Apply sliding window for s of length p to get char's count.
        s_char_counts = [0] * 26
        
        # Initalize 1st sliding window's prefix for s w/o last char of p.
        for i in range(len_p - 1):
            s_char_counts[ord(s[i]) - ord('a')] += 1

        for i in range(len_p - 1, len_s):
            # Increment by RHS char of sliding window of s.
            s_char_counts[ord(s[i]) - ord('a')] += 1

            # Decrement by LHS char of sliding window of s.
            if i - len_p >= 0:
                s_char_counts[ord(s[i - len_p]) - ord('a')] -= 1

            if s_char_counts == p_char_counts:
                # Append start index of sliding window.
                result.append(i - len_p + 1)

        return result


def main():
    # Output: [0, 6]
    s = "cbaebabacd"
    p = "abc"
    print SolutionCharCountListSlidingWindow().findAnagrams(s, p)

    # Output: [0, 1, 2]
    s = "abab"
    p = "ab"
    print SolutionCharCountListSlidingWindow().findAnagrams(s, p)


if __name__ == '__main__':
    main()
