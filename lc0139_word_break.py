"""Leetcode 139. Word Break
Medium

URL: https://leetcode.com/problems/word-break/

Given a non-empty string s and a dictionary wordDict containing a list of
non-empty words, determine if s can be segmented into a space-separated sequence
of one or more dictionary words.

Note:
- The same word in the dictionary may be reused multiple times in the segmentation.
- You may assume the dictionary does not contain duplicate words.

Example 1:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""

class SolutionDp(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool

        Time complexity: O(n*m*k), where 
          - n is the length of s,
          - m is the number of words in wordDict,
          - k is the max length of words.
        Space complexity: O(max(n, k)).
        """
        # Apply DP with tabular T, where T[i] denotes if s[:i] can be segmented.
        n = len(s)        
        T = [False] * (n + 1)

        # Empty string is breakable.
        T[0] = True

        for i in range(1, n + 1):
            for w in wordDict:
                # Check if previous word is valid and can be segmented, 
                # and the remaining word is in word dict.
                k = len(w)
                if i - k >= 0 and T[i - k] and s[i-k:i] == w:
                    T[i] = True
                    break

        return T[-1]


class SolutionDp2(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool

        Time complexity: O(m+n^2*k), where
          - m is the number of words in wordDict, 
          - n is the length of s,
          - k is the max length of words.
        Space complexity: O(max(m, n, k)).
        """
        # Apply DP with tabular T, where T[i] denotes if s[:i] can be segmented.
        n = len(s)        
        T = [False] * (n + 1)

        # Use set for quick lookup.
        wordDict = set(wordDict)

        # Empty string is breakable.
        T[0] = True

        for i in range(n):
            for j in range(i + 1, n + 1):
                if T[i] and s[i:j] in wordDict:
                    # Check if s[:i] and s[i:j] are in dict.
                    T[j] = True

        return T[-1]


def main():
    # Ans: True
    s = "leetcode"
    wordDict = ["leet", "code"]
    print SolutionDp().wordBreak(s, wordDict)
    print SolutionDp2().wordBreak(s, wordDict)

    # Ans: True
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    print SolutionDp().wordBreak(s, wordDict)
    print SolutionDp2().wordBreak(s, wordDict)

    # Ans: False
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print SolutionDp().wordBreak(s, wordDict)
    print SolutionDp2().wordBreak(s, wordDict)

    # Ans: True
    s = "aaaaaaa"
    wordDict = ["aaaa","aaa"]
    print SolutionDp().wordBreak(s, wordDict)
    print SolutionDp2().wordBreak(s, wordDict)


if __name__ == '__main__':
    main()
