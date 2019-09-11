"""Leetcode 657. Robot Return to Origin
Easy

URL: https://leetcode.com/problems/robot-return-to-origin/

There is a robot starting at position (0, 0), the origin, on a 2D plane.
Given a sequence of its moves, judge if this robot ends up at (0, 0)
after it completes its moves.

The move sequence is represented by a string, and the character moves[i]
represents its ith move.
Valid moves are R (right), L (left), U (up), and D (down).
If the robot returns to the origin after it finishes all of its moves, return true.
Otherwise, return false.

Note: The way that the robot is "facing" is irrelevant.
"R" will always make the robot move to the right once,
"L" will always make it move left, etc.
Also, assume that the magnitude of the robot's movement is the same for each move.

Example 1:
Input: "UD"
Output: true 
Explanation: The robot moves up once, and then down once.
All moves have the same magnitude, so it ended up at the origin where it started.
Therefore, we return true.

Example 2:
Input: "LL"
Output: false
Explanation: The robot moves left twice.
It ends up two "moves" to the left of the origin.
We return false because it is not at the origin at the end of its moves.
"""

class SolutionDict(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool

        Time complexity: O(n), where n is the number of moves.
        Space complexity: O(1).
        """
        # Since L(U) needs to be complemented by R(D), vice versa,
        # use a dict to count the number of different directions,
        # and check balances of U & D and L & R.
        from collections import defaultdict

        dirs_d = defaultdict(int)

        for c in moves:
            dirs_d[c] += 1

        if dirs_d['U'] == dirs_d['D'] and dirs_d['L'] == dirs_d['R']:
            return True
        else:
            return False


class SolutionTwoCounters(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool

        Time complexity: O(n), where n is the number of moves.
        Space complexity: O(1).
        """
        # Since L(U) needs to be complemented by R(D), vice versa,
        # use two counters to count the number of U/D and L/R.
        # and check balances of U & D and L & R.
        ud_counter = 0
        lr_counter = 0

        for c in moves:
            if c == 'U':
                ud_counter += 1
            elif c == 'D':
                ud_counter -= 1
            elif c == 'L':
                lr_counter += 1
            elif c == 'R':
                lr_counter -= 0

        if ud_counter == 0 and lr_counter == 0:
            return True
        else:
            return False


def main():
    import time

    print 'By dict:'
    start_time = time.time()
    # Output: True
    moves = "UD"
    print SolutionDict().judgeCircle(moves)

    # Output: False
    moves = "LL"
    print SolutionDict().judgeCircle(moves)
    print 'Time: {}'.format(time.time() - start_time)

    print 'By two conters:'
    start_time = time.time()
    # Output: True
    moves = "UD"
    print SolutionTwoCounters().judgeCircle(moves)

    # Output: False
    moves = "LL"
    print SolutionTwoCounters().judgeCircle(moves)
    print 'Time: {}'.format(time.time() - start_time)


if __name__ == '__main__':
    main()
