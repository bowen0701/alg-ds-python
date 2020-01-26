"""Leetcode 953. Verifying an Alien Dictionary
Easy

URL: https://leetcode.com/problems/verifying-an-alien-dictionary/

In an alien language, surprisingly they also use english lowercase letters,
but possibly in a different order. The order of the alphabet is some permutation
of lowercase letters.

Given a sequence of words written in the alien language, and the order of the
alphabet, return true if and only if the given words are sorted lexicographicaly
in this alien language.

Example 1:
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1],
hence the sequence is unsorted.

Example 3:
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is
shorter (in size.) According to lexicographical rules "apple" > "app", because 
'l' > '', where '' is defined as the blank character which is less than any
other character (More info).

Constraints:
- 1 <= words.length <= 100
- 1 <= words[i].length <= 20
- order.length == 26
- All characters in words[i] and order are English lowercase letters.
"""

class SolutionCharOrderDicPrevCurCharOrder(object):
    def _is_not_ordered(self, w_prev, w_cur):
        min_len = min(len(w_prev), len(w_cur))

        for j in range(min_len):
            c_prev, c_cur = w_prev[j], w_cur[j]

            if c_prev != c_cur:
                return self.char_order_d[c_prev] > self.char_order_d[c_cur]

        return len(w_prev) > len(w_cur)

    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool

        Time complexity: O(m*n).
        Space complexity: O(1).
        """
        if not words or len(words) == 1:
            return True

        # Create dict: char->order; +1 for empty string order.
        self.char_order_d = {char: i + 1 for i, char in enumerate(order)}

        # For each word & previous one, check 1st mismatch chars's order correctness.
        n = len(words)

        for i in range(1, n):
            w_prev, w_cur = words[i - 1], words[i]
            
            if self._is_not_ordered(w_prev, w_cur):
                return False

        return True


def main():
    # Output: true
    words = ["hello","leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    print SolutionCharOrderDicPrevCurCharOrder().isAlienSorted(words, order)

    # Output: false
    words = ["word","world","row"]
    order = "worldabcefghijkmnpqstuvxyz"
    print SolutionCharOrderDicPrevCurCharOrder().isAlienSorted(words, order)

    # Output: false
    words = ["apple","app"]
    order = "abcdefghijklmnopqrstuvwxyz"
    print SolutionCharOrderDicPrevCurCharOrder().isAlienSorted(words, order)

    # Output: true
    words = ["kuvp","q"]
    order = "ngxlkthsjuoqcpavbfdermiywz"
    print SolutionCharOrderDicPrevCurCharOrder().isAlienSorted(words, order)


if __name__ == '__main__':
    main()
