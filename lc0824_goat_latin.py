"""Leetcode 824. Goat Latin
Easy

URL: https://leetcode.com/problems/goat-latin/

A sentence S is given, composed of words separated by spaces.
Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin"
(a made-up language similar to Pig Latin.)

The rules of Goat Latin are as follows:

- If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
For example, the word 'apple' becomes 'applema'.
 
- If a word begins with a consonant (i.e. not a vowel), remove the first letter and
append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".
 
- Add one letter 'a' to the end of each word per its word index in the sentence,
starting with 1.
For example, the first word gets "a" added to the end, the second word gets "aa"
added to the end and so on.
Return the final sentence representing the conversion from S to Goat Latin. 

Example 1:
Input: "I speak Goat Latin"
Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

Example 2:
Input: "The quick brown fox jumped over the lazy dog"
Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa
         hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"

Notes:
S contains only uppercase, lowercase and spaces. Exactly one space between each word.
1 <= S.length <= 150.
"""

class SolutionSplitWordList(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str

        Time complexity: O(n*m), where
          - n: length of words.
          - m: max lengths of words.
        Space complexity: O(m).
        """
        # Split S into word list.
        words = S.split()

        # Create lowercase & upercase vowel set for quick lookup.
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

        # Iterate through words, with word index.
        for i, w in enumerate(words):
            if w[0] in vowels:
                # For word starting with a, e, i, o, or u, append ma and repeated a's.
                words[i] = w + 'ma' + 'a' * (i + 1)
            else:
                # For word starting with non-vowels, move 1st char to tail and append repeated a's.
                words[i] = w[1:] + w[0] + 'ma' + 'a' * (i + 1)

        return ' '.join(words)


def main():
    # Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
    S = "I speak Goat Latin"
    print SolutionSplitWordList().toGoatLatin(S)

    # Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
    S = "The quick brown fox jumped over the lazy dog"
    print SolutionSplitWordList().toGoatLatin(S)


if __name__ == '__main__':
    main()
