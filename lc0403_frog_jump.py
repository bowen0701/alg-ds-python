"""Leetcode 403. Frog Jump
Hard

URL: https://leetcode.com/problems/frog-jump/

A frog is crossing a river. The river is divided into x units and at each unit
there may or may not exist a stone. The frog can jump on a stone, but it must
not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, determine
if the frog is able to cross the river by landing on the last stone. Initially,
the frog is on the first stone and assume the first jump must be 1 unit.

If the frog's last jump was k units, then its next jump must be either
k - 1, k, or k + 1 units. Note that the frog can only jump in the forward direction.

Note:
- The number of stones is >= 2 and is < 1,100.
- Each stone's position will be a non-negative integer < 231.
- The first stone's position is always 0.

Example 1:
[0,1,3,5,6,8,12,17]
There are a total of 8 stones.
The first stone at the 0th unit, second stone at the 1st unit,
third stone at the 3rd unit, and so on...
The last stone at the 17th unit.
Return true. The frog can jump to the last stone by jumping 
1 unit to the 2nd stone, then 2 units to the 3rd stone, then 
2 units to the 4th stone, then 3 units to the 6th stone, 
4 units to the 7th stone, and 5 units to the 8th stone.

Example 2:
[0,1,2,3,4,8,9,11]
Return false. There is no way to jump to the last stone as 
the gap between the 5th and 6th stone is too large.
"""

class SolutionDP(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool

        Apply DP with cache for stone->set(steps).

        Time complexity: O(n^2).
        Space complexity: O(n^2).
        """
        # Since 1st jump must be 1 unit.
        if stones[1] != 1:
            return False

        n = len(stones)

        # Cache stone's steps by dict, with 1st jump in 1 unit.
        stone_jumps = {stone: set() for stone in stones}
        stone_jumps[1].add(1)

        for i, stone in enumerate(stones):
            # Skip last stone since it's destination.
            if i <= n - 2:
                for j in stone_jumps[stone]:
                    for jump in [j - 1, j, j + 1]:
                        # Check if next jump is on a stone.
                        if jump > 0 and stone + jump in stone_jumps:
                            stone_jumps[stone + jump].add(jump)

        # Return if there are jumps on the last stone.
        return bool(stone_jumps[stones[-1]])


def main():
    # Output: True
    stones = [0,1,3,5,6,8,12,17]
    print SolutionDP().canCross(stones)

    # Output: False
    stones = [0,1,2,3,4,8,9,11]
    print SolutionDP().canCross(stones)


if __name__ == '__main__':
    main()
