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
                    # If not, set to 1 + min of insert, delete and replace.
                    T[i][j] = 1 + min(T[i][j - 1], T[i - 1][j], T[i - 1][j - 1])

        return T[-1][-1]


def main():
    # Ans: 3.
    word1 = "horse"
    word2 = "ros"
    print SolutionDp().minDistance(word1, word2)

    # Ans: 5.
    word1 = "intention"
    word2 = "execution"
    print SolutionDp().minDistance(word1, word2)


if __name__ == '__main__':
    main()
