"""Leetcode 739. Daily Temperatures
Medium

URL: https://leetcode.com/problems/daily-temperatures

Given a list of daily temperatures T, return a list such that, for each day 
in the input, tells you how many days you would have to wait until a warmer 
temperature. If there is no future day for which this is possible, put 0 
instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], 
your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each 
temperature will be an integer in the range [30, 100].
"""

class SolutionBrute(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]

        Time complexity: O(n^2).
        Space complexity: O(n).
        """
        days = [0] * len(T)

        for i, t in enumerate(T):
            for j in range(i + 1, len(T)):
                if T[j] > t:
                    days[i] = j - i
                    break

        return days


class SolutionStack(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]

        Time complexity: O(n).
        Space complexity: O(n).
        """
        days = [0] * len(T)

        # Create a stack to track posisions to be filled.
        fill_pos_stack = []

        for pos, t in enumerate(T):
            # Everytime a higher temperature is found, 
            # update days by position stack' peak.
            while fill_pos_stack and T[fill_pos_stack[-1]] < t:
                prev_pos = fill_pos_stack.pop()
                days[prev_pos] = pos - prev_pos

            fill_pos_stack.append(pos)

        return days


def main():
    import time

    T = [73, 74, 75, 71, 69, 72, 76, 73]
    # Ans: [1, 1, 4, 2, 1, 1, 0, 0]
  
    start_time = time.time()
    print 'By brute force: {}'.format(SolutionBrute().dailyTemperatures(T))
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'By stack: {}'.format(SolutionStack().dailyTemperatures(T))
    print 'Time: {}'.format(time.time() - start_time)


if __name__ == '__main__':
    main()
