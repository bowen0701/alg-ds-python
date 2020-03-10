"""Leetcode 346. Moving Average from Data Stream (Premium)
Easy

Given a stream of integers and a window size,
calculate the moving average of all integers in the sliding window.

For example,
MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
"""

class MovingAverageQueue(object):
    def __init__(self, size):
        from collections import deque

        self.size = size

        # Apply queue to collect stream of specific length.
        self.queue = deque()
        self.sum = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float

        Time complexity: O(1).
        Space complexity: O(1).
        """
        # First check if queue is full, if yes, pop the first-in.
        if len(self.queue) == self.size:
            self.sum -= self.queue.popleft()

        self.queue.append(val)
        self.sum += val

        # Note queue len is dynamic for first few elements.
        return self.sum / float(len(self.queue))


def main():
    moving_avg = MovingAverageQueue(3)
    print moving_avg.next(1)
    print moving_avg.next(10)
    print moving_avg.next(3)
    print moving_avg.next(5)


if __name__ == '__main__':
    main()
