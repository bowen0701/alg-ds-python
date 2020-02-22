"""Leetcode 780. Reaching Points
Hard

URL: https://leetcode.com/problems/reaching-points/

A move consists of taking a point (x, y) and transforming it to either
(x, x+y) or (x+y, y).

Given a starting point (sx, sy) and a target point (tx, ty),
return True if and only if a sequence of moves exists to transform the point
(sx, sy) to (tx, ty). Otherwise, return False.

Examples:
Input: sx = 1, sy = 1, tx = 3, ty = 5
Output: True
Explanation:
One series of moves that transforms the starting point to the target is:
(1, 1) -> (1, 2)
(1, 2) -> (3, 2)
(3, 2) -> (3, 5)

Input: sx = 1, sy = 1, tx = 2, ty = 2
Output: False

Input: sx = 1, sy = 1, tx = 1, ty = 1
Output: True

Note:
sx, sy, tx, ty will all be integers in the range [1, 10^9].
"""

class SolutionTopDownRecur(object):
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool

        Apply top-dow recursion.
        Note: Time limit exceeded.

        Time complexity: O(2^n), where n = max(tx, ty).
        Space complexity: O(n).
        """
        # Base case: when start meets target.
        if sx == tx and sy == ty:
            return True

        # Out of boundary cases.
        if sx > tx or sy > ty:
            return False

        return (self.reachingPoints(sx + sy, sy, tx, ty) or
                self.reachingPoints(sx, sx + sy, tx, ty))


class SolutionBottomUpRecur(object):
    def _recur(self, sx, sy, tx, ty):
        if tx == sx and ty == sy:
            return True

        if tx < sx or ty < sy:
            return False

        if tx == sx:
            # Since tx=sx, ty can traverse back to sy if (ty-sy)%sx=0.
            if (ty - sy) % sx == 0:
                return True
            else:
                return False

        if ty == sy:
            # Since ty=sy, tx can traverse back to sx if (tx-sx)%sy=0.
            if (tx - sx) % sy == 0:
                return True
            else:
                return False

        return (self._recur(sx, sy, tx - ty, ty) or
                self._recur(sx, sy, tx, ty - tx))

    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool

        Apply bottom-up recursion.

        Time complexity: O(log(max(tx, ty))).
        Space complexity: O(log(max(tx, ty))).
        """
        return self._recur(sx, sy, tx, ty)


class SolutionBottomUpIter(object):
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool

        Apply bottom-up recursion.

        Time complexity: O(log(max(tx, ty))).
        Space complexity: O(1).
        """
        while tx > sx and ty > sy:
            if tx < ty:
                ty %= tx
            else:
                tx %= ty

        return ((tx == sx and ty >= sy and (ty - sy) % sx == 0) or
                (ty == sy and tx >= sx and (tx - sx) % sy == 0))


def main():
    # Output: True
    sx, sy, tx, ty = 1, 1, 3, 5
    print SolutionTopDownRecur().reachingPoints(sx, sy, tx, ty)
    print SolutionBottomUpRecur().reachingPoints(sx, sy, tx, ty)
    print SolutionBottomUpIter().reachingPoints(sx, sy, tx, ty)

    # Output: False
    sx, sy, tx, ty = 1, 1, 2, 2
    print SolutionTopDownRecur().reachingPoints(sx, sy, tx, ty)
    print SolutionBottomUpRecur().reachingPoints(sx, sy, tx, ty)
    print SolutionBottomUpIter().reachingPoints(sx, sy, tx, ty)

    # Output: True
    sx, sy, tx, ty = 1, 1, 1, 1
    print SolutionTopDownRecur().reachingPoints(sx, sy, tx, ty)
    print SolutionBottomUpRecur().reachingPoints(sx, sy, tx, ty)
    print SolutionBottomUpIter().reachingPoints(sx, sy, tx, ty)


if __name__ == '__main__':
    main()
