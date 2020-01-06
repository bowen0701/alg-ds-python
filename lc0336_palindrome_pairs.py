"""336. Palindrome Pairs
Hard

URL: https://leetcode.com/problems/palindrome-pairs/

Given a list of unique words, find all pairs of distinct indices (i, j) in the given
list, so that the concatenation of the two words, i.e. words[i] + words[j] is a
palindrome.

Example 1:
Input: ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]] 
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]

Example 2:
Input: ["bat","tab","cat"]
Output: [[0,1],[1,0]] 
Explanation: The palindromes are ["battab","tabbat"]
"""

class SolutionWordIdxDictPrefixSuffixPalindrome(object):
    def _isPalindrom(self, word):
        return word == word[::-1]

    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]

        Time complexity: O(n*m^2), where
          - n: number of words
          - m: max length of words
        Space complexity: O(n+m).
        """
        # For each word, check if word's prefix and suffix are palindromes.
        n = len(words)
        pal_pairs = []

        # Use dict: word->idx for quick lookup.
        word_idx_d = {word: i for i, word in enumerate(words)}

        # Iterate through words, check word's prefix and reversed suffix (and vice versa).
        for word, idx in word_idx_d.items():
            m = len(word)

            for j in range(m + 1):
                prefix = word[:j]
                suffix = word[j:]

                if self._isPalindrom(prefix):
                    # If prefix and reversed suffix are palindrome, 
                    # append (reversed suffix idx, word idx).
                    rev_suffix = suffix[::-1]
                    if rev_suffix != word and rev_suffix in word_idx_d:
                        pal_pairs.append([word_idx_d[rev_suffix], idx])

                if j != m and self._isPalindrom(suffix):
                    # If suffix and reversed prefix are palindrome, 
                    # append to (word idx, reversed prefix word idx).
                    rev_prefix = prefix[::-1]
                    if rev_prefix in word_idx_d:
                        pal_pairs.append([idx, word_idx_d[rev_prefix]])

        return pal_pairs


def main():
    # Output: [[0,1],[1,0],[3,2],[2,4]] 
    words = ["abcd","dcba","lls","s","sssll"]
    print SolutionWordIdxDictPrefixSuffixPalindrome().palindromePairs(words)

    # Output: [[0,1],[1,0]] 
    words = ["bat","tab","cat"]
    print SolutionWordIdxDictPrefixSuffixPalindrome().palindromePairs(words)

    # Output: [[2,0],[2,1]] 
    words = ["bot","t","to"]
    print SolutionWordIdxDictPrefixSuffixPalindrome().palindromePairs(words)


if __name__ == '__main__':
    main()
