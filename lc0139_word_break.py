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
        # Apply DP with tabular T.
        n = len(s)        
        T = [False] * (n + 1)

        # Empty string is breakable.
        T[0] = True

        for i in range(1, n + 1):
            for w in wordDict:
                # Check index is valid, the previous word is breakable, and
                # the partial word is in word dict. 
                if i - len(w) >= 0 and T[i - len(w)] and s[(i - len(w)):i] == w:
                    T[i] = True
                    break

        return T[-1]


def main():
    # Ans: True
    s = "leetcode"
    wordDict = ["leet", "code"]
    print SolutionDp().wordBreak(s, wordDict)

    # Ans: True
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    print SolutionDp().wordBreak(s, wordDict)

    # Ans: False
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print SolutionDp().wordBreak(s, wordDict)

    # Ans: True
    s = "aaaaaaa"
    wordDict = ["aaaa","aaa"]
    print SolutionDp().wordBreak(s, wordDict)


if __name__ == '__main__':
    main()
