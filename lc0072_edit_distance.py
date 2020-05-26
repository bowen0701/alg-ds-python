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
    def _editRecur(self, word1, word2):
        # If word1 and word2 are empty strings.
        if not word1 and not word2:
            return 0

        # If one of word1 and word2 is empty string.
        if not word1 or not word2:
            return len(word1) or len(word2)

        if word1[0] == word2[0]:
            # If 1st chars are equal, edit the remaining words. 
            return self._editRecur(word1[1:], word2[1:])
        else:
            # If not, recursively get min of insert, delete, and replace.
            insert = 1 + self._editRecur(word1, word2[1:])
            delete = 1 + self._editRecur(word1[1:], word2)
            replace = 1 + self._editRecur(word1[1:], word2[1:])
            return min(insert, delete, replace)

    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int

        Time complexity: O((n1+n2)*3^(n1+n2)).
        Space complexity: O((n1*n2)^2).
        """
        # Apply top-down DP by recursion.
        return self._editRecur(word1, word2)


class SolutionRecurPointer(object):
    def _editRecur(self, word1, word2, i1, i2):
        # If word1 and word2 are empty strings.
        if i1 == self.n1 and i2 == self.n2:
            return 0

        # If one of word1 and word2 is empty string.
        if i1 == self.n1 or i2 == self.n2:
            return self.n1 - i1 or self.n2 - i2

        if word1[i1] == word2[i2]:
            # If 1st chars are equal, edit the remaining words. 
            return self._editRecur(word1, word2, i1 + 1, i2 + 1)
        else:
            # If not, recursively get min of insert, delete, and replace.
            insert = 1 + self._editRecur(word1, word2, i1, i2 + 1)
            delete = 1 + self._editRecur(word1, word2, i1 + 1, i2)
            replace = 1 + self._editRecur(word1, word2, i1 + 1, i2 + 1)
            return min(insert, delete, replace)

    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int

        Time complexity: O(3^(n1+n2)).
        Space complexity: O(n1*n2).
        """
        # Apply top-down recursion with two pointers.
        self.n1, self.n2 = len(word1), len(word2)
        i1, i2 = 0, 0
        return self._editRecur(word1, word2, i1, i2)


class SolutionMemo(object):
    def _editRecur(self, word1, word2, i1, i2, T):
        # If word1 and word2 are empty strings.
        if i1 == self.n1 and i2 == self.n2:
            return 0

        # If one of word1 and word2 is empty string.
        if i1 == self.n1 or i2 == self.n2:
            return self.n1 - i1 or self.n2 - i2

        # Check memo table.
        if T[i1][i2]:
            return T[i1][i2]

        if word1[i1] == word2[i2]:
            # If 1st chars are equal, edit the remaining words.
            T[i1][i2] = self._editRecur(word1, word2, i1 + 1, i2 + 1, T)
        else:
            # If not, recursively get min of insert, delete, and replace.
            insert = 1 + self._editRecur(word1, word2, i1, i2 + 1, T)
            delete = 1 + self._editRecur(word1, word2, i1 + 1, i2, T)
            replace = 1 + self._editRecur(word1, word2, i1 + 1, i2 + 1, T)
            T[i1][i2] = min(insert, delete, replace)
        return T[i1][i2]

    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int

        Time complexity: O(n1*n2).
        Space complexity: O(n1*n2).
        """
        # Apply top-down DP with recursion in two pointers with memoization.
        self.n1, self.n2 = len(word1), len(word2)
        i1, i2 = 0, 0

        # Use a table T[i1][i2] for dist for word1[:i1] & word2[:i2].
        T = [[0] * self.n2 for _ in range(self.n1)]
        return self._editRecur(word1, word2, i1, i2, T)


class SolutionDP(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int

        Time complexity: O(n1*n2).
        Space complexity: O(n1*n2).
        """
        # Use a table T[i1][i2] for dist for word1[:i1] & word2[:i2].
        n1, n2 = len(word1), len(word2)
        T = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        # Fill T for word1 = ''.
        for c in range(n2 + 1):
            T[0][c] = c

        # Fill T for word2 = ''.
        for r in range(n1 + 1):
            T[r][0] = r

        for r in range(1, n1 + 1):
            for c in range(1, n2 + 1):
                if word1[r - 1] == word2[c - 1]:
                    # If chars i & j are equal, ignore them & use up-left.
                    T[r][c] = T[r - 1][c - 1]
                else:
                    # If not: 1 + insert (left), delete (up) and replace (up-left).
                    T[r][c] = 1 + min(T[r][c - 1], T[r - 1][c], T[r - 1][c - 1])

        return T[-1][-1]


def main():
    import time

    # Ans: 3.
    word1 = "horse"
    word2 = "ros"

    start_time = time.time()
    print 'By naive recur:', SolutionRecurNaive().minDistance(word1, word2)
    print 'Time:', time.time() - start_time

    start_time = time.time()
    print 'By recur w/ pointer:', SolutionRecurPointer().minDistance(word1, word2)
    print 'Time:', time.time() - start_time

    start_time = time.time()
    print 'By memo:', SolutionMemo().minDistance(word1, word2)
    print 'Time:', time.time() - start_time

    start_time = time.time()
    print 'By DP: ', SolutionDP().minDistance(word1, word2)
    print 'Time:', time.time() - start_time

    # Ans: 5.
    word1 = "intention"
    word2 = "execution"

    start_time = time.time()
    print 'By naive recur:', SolutionRecurNaive().minDistance(word1, word2)
    print 'Time:', time.time() - start_time

    start_time = time.time()
    print 'By recur w/ pointer:', SolutionRecurPointer().minDistance(word1, word2)
    print 'Time:', time.time() - start_time

    start_time = time.time()
    print 'By memo:', SolutionMemo().minDistance(word1, word2)
    print 'Time:', time.time() - start_time

    start_time = time.time()
    print 'By DP: ', SolutionDP().minDistance(word1, word2)
    print 'Time:', time.time() - start_time


if __name__ == '__main__':
    main()
