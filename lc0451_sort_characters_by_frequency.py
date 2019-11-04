"""Leetcode 451. Sort Characters By Frequency
Medium

URL: https://leetcode.com/problems/sort-characters-by-frequency/

Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:
Input:
"tree"
Output:
"eert"
Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:
Input:
"cccaaa"
Output:
"cccaaa"
Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:
Input:
"Aabb"
Output:
"bbAa"
Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""

class SolutionCharFreqDict(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str

        Time complexity: O(n*logn), where n is the length of s.
        Space complexity: O(n).
        """
        from collections import defaultdict

        if not s:
            return ''

        # Use a dict to collect chars's frequencies.
        char_freqs = defaultdict(int)
        for c in s:
            char_freqs[c] += 1

        # Sort dict by values.
        sorted_char_freqs = sorted(char_freqs.items(), 
                                   key=lambda x: x[1], reverse=True)

        # Convert dict to list with duplicated chars based on frequencies.
        sorted_chars = [char * freq for (char, freq) in sorted_char_freqs]
        return ''.join(sorted_chars)


def main():
    # Output: eert
    s = "tree"
    print SolutionCharFreqDict().frequencySort(s)

    # Output: cccaaa
    s = "cccaaa"
    print SolutionCharFreqDict().frequencySort(s)

    # Output: bbAa
    s = "Aabb"
    print SolutionCharFreqDict().frequencySort(s)


if __name__ == '__main__':
    main()
