"""Leetcode 791. ustom Sort String
Medium

URL: https://leetcode.com/problems/custom-sort-string/

You are given two strings order and s. All the words of order are unique and were sorted in some custom order previously.

Permute the characters of s so that they match the order that order was sorted. 
More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.

Return any permutation of s that satisfies this property.

Example 1:
Input: order = "cba", s = "abcd"
Output: "cbad"
Explanation: 
"a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a". 
Since "d" does not appear in order, it can be at any position in the returned string. 
"dcba", "cdba", "cbda" are also valid outputs.

Example 2:
Input: order = "cbafg", s = "abcd"
Output: "cbad"

Constraints:
- 1 <= order.length <= 26
- 1 <= s.length <= 200
- order and s consist of lowercase English letters.
- All the characters of order are unique.
"""

class SolutionCharFreqDict:
    def customSortString(self, order: str, s: str) -> str:
        """
        Time complexity: O(m + n).
        Space complexity: O(m).
        """
        # Iterate through s to build dict: char->freq.
        from collections import defaultdict

        char_freq_d = defaultdict(int)

        for char in s:
            char_freq_d[char] += 1

        # Iterate through order to concat result and pop completed char->freq.
        result = []
        for char in order:
            for _ in range(char_freq_d[char]):
                result.append(char)

            del char_freq_d[char]

        # Iterate through dict's remaining char->freq to concat result.
        for char, freq in char_freq_d.items():
            for _ in range(freq):
                result.append(char)

        return ''.join(result)


def main():
    # Output: "cbad"
    order = "cba"
    s = "abcd"
    print(SolutionCharFreqDict().customSortString(order, s))

    # Output: "cbad"
    order = "cbafg"
    s = "abcd"
    print(SolutionCharFreqDict().customSortString(order, s))


if __name__ == "__main__":
    main()
