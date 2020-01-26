"""Leetcode 140. Word Break II
Medium

URL: https://leetcode.com/problems/word-break-ii/

Given a non-empty string s and a dictionary wordDict containing a list of
non-empty words, add spaces in s to construct a sentence where each word is a
valid dictionary word. Return all such possible sentences.

Note:
- The same word in the dictionary may be reused multiple times in the segmentation.
- You may assume the dictionary does not contain duplicate words.

Example 1:
Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]

Example 2:
Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:
Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
"""

class SolutionDPBacktrackDFS(object):
    def _check_word_break(self, s, wordDict):
        # Apply DP with T, where T[i] denotes s[:i] is segmented.
        n = len(s)
        T = [False] * (n + 1)

        # Edge case: empty string is segmented.
        T[0] = True

        # Iterate to check if s[:i] is segmented, and the remaining of s in dict.
        for i in range(n):
            for j in range(i + 1, n + 1):
                if T[i] and s[i:j] in wordDict:
                    T[j] = True

        is_breakable = T[-1]
        return is_breakable

    def _backtrack(self, result, temp, s, wordDict):
        # Append temp string if arrived at the end of s, with the last char ' '.
        if not s:
            result.append(temp[:-1])
            return None

        # Check if the 1st part of s is in dict, if yes, apply DFS for the remaining s.
        for i in range(1, len(s) + 1):
            if s[:i] in wordDict:
                self._backtrack(
                    result, temp + s[:i] + ' ', s[i:], wordDict)

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]

        Apply backtracking:
        - check if s can be segmented by word break I.
        - if yes, apply DFS to search remaining part of s.

        Time complexity: O(n^3+n*2^n)=O(n*n^2), where n is the length of s.
        Space complexity: O(n^2).
        """
        # Edge case.
        if not s:
            return []

        # Use set for quick lookup.
        wordDict = set(wordDict)

        # Check if s can be segmented.
        is_breakable = self._check_word_break(s, wordDict)
        if not is_breakable:
            return []

        # Apply backtracking DFS to collect sentences.
        result = []
        temp = ''
        self._backtrack(result, temp, s, wordDict)
        return result


def main():
    # Output:
    # [
    #   "cats and dog",
    #   "cat sand dog"
    # ]
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    print SolutionDPBacktrackDFS().wordBreak(s, wordDict)


if __name__ == '__main__':
    main() 
