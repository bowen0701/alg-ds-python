"""Leetcode 1119.Remove Vowels from a String (Premium)
Easy

URL: https://leetcode.com/problems/remove-vowels-from-a-string

Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it,
and return the new string.

Example 1:
Input: "leetcodeisacommunityforcoders"
Output: "ltcdscmmntyfrcdrs"

Example 2:
Input: "aeiou"
Output: ""

Note:
- S consists of lowercase English letters only.
- 1 <= S.length <= 1000
"""

class SolutionSet(object):
    def removeVowels(self, S):
        """
        :type S: string
        :rtype: string

        Time complexity: O(n).
        Space complexity: O(n).
        """
        if not S:
            return ''

        # Push vowels into set for quick lookup.
        vowels = set(['a', 'e', 'i', 'o', 'u'])

        # Collect non-vowels into a list.
        result = []

        for s in S:
            if s not in vowels:
                result.append(s)

        return ''.join(result)


def main():
    # Output: "ltcdscmmntyfrcdrs"
    S = 'leetcodeisacommunityforcoders'
    print SolutionSet().removeVowels(S)

    # Output: ""
    S = 'aeiou'
    print SolutionSet().removeVowels(S)


if __name__ == '__main__':
    main()
