"""Leetcode 403. Frog Jump
Hard

URL: https://leetcode.com/problems/frog-jump/

A frog is crossing a river. The river is divided into x units and at each unit
there may or may not exist a stone. The frog can jump on a stone, but it must
not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, 
determine if the frog is able to cross the river by landing on the last stone.
Initially, the frog is on the first stone and assume the first jump must be 1 unit.

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

class SolutionStoneJumpDictDP(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool

        Time complexity: O(n^2).
        Space complexity: O(n^2).
        """
        if stones[1] != 1:
            return False

        # Apply DP with dict: stone->set(steps), with 1st jump in 1 unit.
        stone_jumps_d = {stone: set() for stone in stones}
        stone_jumps_d[1].add(1)

        for i, stone in enumerate(stones):
            # i is up to n - 2 since it is the last jump start.
            if i == len(stones) - 1:
                continue

            for jump in stone_jumps_d[stone]:
                for next_jump in [jump - 1, jump, jump + 1]:
                    # Check if next jump is on a stone.
                    if next_jump > 0 and stone + next_jump in stone_jumps_d:
                        stone_jumps_d[stone + next_jump].add(next_jump)

        # Return True if there are jumps on the last stone.
        return bool(stone_jumps_d[stones[-1]])


class SolutionPositionJumpStacksDP(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool

        Time complexity: O(n^2).
        Space complexity: O(n^2).
        """
        if stones[1] != 1:
            return False

        for i in range(3, len(stones)):
            if stones[i] > stones[i - 1] * 2:
                return False

        # Use stone set for quickly check position.
        stones_set = set(stones)

        # Track positions and jumps, with initial jump = 0 due to 1st jump.
        position_stack = [0]
        jump_stack = [0]

        while position_stack:
            position = position_stack.pop()
            jump = jump_stack.pop()
            next_jumps = [jump - 1, jump, jump + 1]

            for next_jump in next_jumps:
                if next_jump <= 0:
                    continue

                next_position = position + next_jump
                if next_position == stones[-1]:
                    return True
                elif next_position in stones_set:
                    position_stack.append(next_position)
                    jump_stack.append(next_jump)

        return False


def main():
    # Output: True
    stones = [0,1,3,5,6,8,12,17]
    print SolutionStoneJumpDictDP().canCross(stones)
    print SolutionPositionJumpStacksDP().canCross(stones)

    # Output: False
    stones = [0,1,2,3,4,8,9,11]
    print SolutionStoneJumpDictDP().canCross(stones)
    print SolutionPositionJumpStacksDP().canCross(stones)

    # Output: True
    stones = [0,1]
    print SolutionStoneJumpDictDP().canCross(stones)
    print SolutionPositionJumpStacksDP().canCross(stones)


if __name__ == '__main__':
    main()
