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

class SolutionWordposDictPrefixSuffixPalindrome(object):
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

        # Use dict: word->pos for quick lookup.
        word_pos_d = {word: pos for pos, word in enumerate(words)}

        # Iterate through words, check word's prefix and suffix based on each char.
        for word, pos in word_pos_d.items():
            m = len(word)

            for j in range(m + 1):
                prefix = word[:j]
                suffix = word[j:]

                # If prefix is palindrome, reversed suffix in words but not current one,
                # append (reversed suffix pos, word pos).
                if self._isPalindrom(prefix):
                    rev_suffix = suffix[::-1]
                    if rev_suffix != word and rev_suffix in word_pos_d:
                        pal_pairs.append([word_pos_d[rev_suffix], pos])

                # If suffix is palindrome but not '', and prefix in words, 
                # append (word pos, reversed prefix pos).
                if j != m and self._isPalindrom(suffix):
                    rev_prefix = prefix[::-1]
                    if rev_prefix in word_pos_d:
                        pal_pairs.append([pos, word_pos_d[rev_prefix]])

        return pal_pairs


def main():
    # Output: [[0,1],[1,0],[3,2],[2,4]] 
    words = ["abcd","dcba","lls","s","sssll"]
    print SolutionWordposDictPrefixSuffixPalindrome().palindromePairs(words)

    # Output: [[0,1],[1,0]] 
    words = ["bat","tab","cat"]
    print SolutionWordposDictPrefixSuffixPalindrome().palindromePairs(words)

    # Output: [[2,0],[2,1]] 
    words = ["bot","t","to"]
    print SolutionWordposDictPrefixSuffixPalindrome().palindromePairs(words)


if __name__ == '__main__':
    main()
