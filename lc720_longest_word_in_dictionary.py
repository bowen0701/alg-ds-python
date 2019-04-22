"""Leetcode 720. Longest Word in Dictionary
Easy

URL: https://leetcode.com/problems/longest-word-in-dictionary/

Given a list of strings words representing an English Dictionary, 
find the longest word in words that can be built one character at a time by 
other words in words. If there is more than one possible answer, return the 
longest word with the smallest lexicographical order.

If there is no answer, return the empty string.

Example 1:
Input: 
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation: 
The word "world" can be built one character at a time by 
"w", "wo", "wor", and "worl".

Example 2:
Input: 
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation: 
Both "apply" and "apple" can be built from other words in the dictionary. 
However, "apple" is lexicographically smaller than "apply".

Note:
All the strings in the input will only contain lowercase letters.
The length of words will be in the range [1, 1000].
The length of words[i] will be in the range [1, 30].
"""

class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str

        Time complexity: O(n), where n is the length of words.
        Space complexity: O(m), where m is the max length of word.
        """
        prefix = longest = ''
        for w in sorted(words):
            if w[:len(w) - 1] == prefix[:len(w) - 1]:
                prefix = w
                longest = max([longest, prefix], key=len)
        return longest


class SolutionTrie(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str

        Time complexity: O(??).
        Space complexity: O(??).
        """
        pass


def main():
    # Ans: "world".
    words = ["w","wo","wor","worl", "world"]
    print(Solution().longestWord(words))

    # Ans: "apple".
    words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    print(Solution().longestWord(words))


if __name__ == '__main__':
    main()
