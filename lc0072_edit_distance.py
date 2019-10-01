"""Leetcode 72. Edit Distance
Hard

URL: https://leetcode.com/problems/edit-distance/

Given two words word1 and word2, find the minimum number of operations 
required to convert word1 to word2.

You have the following 3 operations permitted on a word:
- Insert a character (to word1)
- Delete a character (of word1)
- Replace a character (of word1 & word2)

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""

class SolutionRecurNaive(object):
    def _recur(self, word1, word2):
        # If word1 and word2 are empty strings.
        if not word1 and not word2:
            return 0

        # If one of word1 and word2 is empty string.
        if not word1 or not word2:
            return len(word1) or len(word2)

        if word1[0] == word2[0]:
            # If 1st chars are equal, edit the remaining words. 
            return self._recur(word1[1:], word2[1:])
        else:
            # If not, recursively get min of insert, delete, and replace.
            insert = 1 + self._recur(word1, word2[1:])
            delete = 1 + self._recur(word1[1:], word2)
            replace = 1 + self._recur(word1[1:], word2[1:])
            return min(insert, delete, replace)


    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int

        Time complexity: O(n1*n2*2^(n1+n2)).
        Space complexity: O((n1*n2)^2).
        """
        return self._recur(word1, word2)


class SolutionRecurPointer(object):
    def _recur(self, word1, word2, i1, i2):
        # If word1 and word2 are empty strings.
        if i1 == len(word1) and i2 == len(word2):
            return 0

        # If one of word1 and word2 is empty string.
        if i1 == len(word1) or i2 == len(word2):
            return len(word1) - i1 or len(word2) - i2

        if word1[i1] == word2[i2]:
            # If 1st chars are equal, edit the remaining words. 
            return self._recur(word1, word2, i1 + 1, i2 + 1)
        else:
            # If not, recursively get min of insert, delete, and replace.
            insert = 1 + self._recur(word1, word2, i1, i2 + 1)
            delete = 1 + self._recur(word1, word2, i1 + 1, i2)
            replace = 1 + self._recur(word1, word2, i1 + 1, i2 + 1)
            return min(insert, delete, replace)


    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int

        Time complexity: O(2^(n1+n2)).
        Space complexity: O(n1*n2).
        """
        i1 = 0
        i2 = 0
        return self._recur(word1, word2, i1, i2)


class SolutionDp(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int

        Time complexity: O(n1*n2).
        Space complexity: O(n1*n2).
        """
        # Apply dynamic programming with table T.
        n1, n2 = len(word1), len(word2)

        T = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        for j in range(n2 + 1):
            # If word1 = ''.
            T[0][j] = j

        for i in range(n1 + 1):
            # If word2 = ''.
            T[i][0] = i

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    # If chars i & j are equal, set to the previous T[i-1][j-1]. 
                    T[i][j] = T[i - 1][j - 1]
                else:
                    # If not, set to min of insert, delete and replace.
                    T[i][j] = min(1 + T[i][j - 1], 1 + T[i - 1][j], 1 + T[i - 1][j - 1])

        return T[-1][-1]


def main():
    # Ans: 3.
    word1 = "horse"
    word2 = "ros"
    print SolutionRecurNaive().minDistance(word1, word2)
    print SolutionRecurPointer().minDistance(word1, word2)
    print SolutionDp().minDistance(word1, word2)

    # Ans: 5.
    word1 = "intention"
    word2 = "execution"
    print SolutionRecurNaive().minDistance(word1, word2)
    print SolutionRecurPointer().minDistance(word1, word2)
    print SolutionDp().minDistance(word1, word2)


if __name__ == '__main__':
    main()
