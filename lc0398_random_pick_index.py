"""Leetcode 398. Random Pick Index
Medium

URL: https://leetcode.com/problems/random-pick-index/

Given an array of integers with possible duplicates, randomly output the index
of a given target number. You can assume that the given target number must
exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will
not pass the judge.

Example:
int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);
// pick(3) should return either index 2, 3, or 4 randomly. Each index should
// have equal probability of returning.
solution.pick(3);
// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);
"""

class SolutionNumPosDictRandomSample(object):
    def __init__(self, nums):
        """
        :type nums: List[int]

        Time complexity: O(n).
        Space complexity: O(n).
        """
        from collections import defaultdict

        # Store in dict: num->list(pos).
        num_pos_d = defaultdict(list)
        for pos, num in enumerate(nums):
            num_pos_d[num].append(pos)

        self.num_pos_d = num_pos_d

    def pick(self, target):
        """
        :type target: int
        :rtype: int

        Time complexity: O(1).
        Space complexity: O(n).
        """
        import random

        # Get target's positions.
        pos_list = self.num_pos_d[target]

        # Randomly sample a pos.
        n = len(pos_list)
        if n == 1:
            return pos_list[0]
        else:
            u = random.uniform(0, 1)
            return pos_list[int(n * u)]


def main():
    nums = [1,2,3,3,3]
    obj = SolutionNumPosDictRandomSample(nums)
    print obj.pick(3)
    print obj.pick(1)


if __name__ == '__main__':
    main()
