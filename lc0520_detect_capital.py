"""Leetcode 520. Detect Capital
Easy

URL: https://leetcode.com/problems/detect-capital/

Given a word, you need to judge whether the usage of capitals in it is right
or not.

We define the usage of capitals in a word to be right when one of the following
cases holds:
- All letters in this word are capitals, like "USA".
- All letters in this word are not capitals, like "leetcode".
- Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
 
Example 1:
Input: "USA"
Output: True

Example 2:
Input: "FlaG"
Output: False
 
Note: The input will be a non-empty word consisting of uppercase and lowercase
latin letters.
"""

class SolutionCapitalCount(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # Count the number of capitals.
        n_capitals = 0

        for c in word:
            if c.isupper():
                n_capitals += 1

        return (n_capitals == len(word) or
                n_capitals == 0 or
                (n_capitals == 1 and word[0].isupper()))


def main():
    # Output: True
    word = 'USA'
    print SolutionCapitalCount().detectCapitalUse(word)

    # Output: False
    word = 'FlaG'
    print SolutionCapitalCount().detectCapitalUse(word)


if __name__ == '__main__':
    main()
