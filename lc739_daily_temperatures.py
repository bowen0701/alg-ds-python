"""Leetcode 739. Daily Temperatures
Medium

Given a list of daily temperatures T, return a list such that, for each day 
in the input, tells you how many days you would have to wait until a warmer 
temperature. If there is no future day for which this is possible, put 0 
instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], 
your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each 
temperature will be an integer in the range [30, 100].
"""

class SolutionNaive(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]

        Time complexity: O(n^2).
        Space complexity: O(n).
        """
        D = [0 for _ in range(len(T))]
        for i, t in enumerate(T):
            for j in range(i + 1, len(T)):
                if T[j] > t:
                    D[i] = j - i
                    break
        return D


class Solution(object):
    def dailyTemperature(self, T):
        """
        :type T: List[int]
        :rtype: List[int]

        Time complexity: ??
        Space complexity: ??
        """
        pass


def main():
    import time

    T = [73, 74, 75, 71, 69, 72, 76, 73]
    # Ans: [1, 1, 4, 2, 1, 1, 0, 0]
  
    print SolutionNaive().dailyTemperatures(T)

    T = [73, 73, 75, 71, 69, 70, 76, 77]
    # Ans: [2, 1, 4, 3, 1, 1, 1, 0]

    print SolutionNaive().dailyTemperatures(T)


if __name__ == '__main__':
    main()
