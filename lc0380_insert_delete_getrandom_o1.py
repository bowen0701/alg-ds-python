"""Leetcode 380. Insert Delete GetRandom O(1)
Medium

URL: https://leetcode.com/problems/insert-delete-getrandom-o1/

Design a data structure that supports all following operations in average O(1)
time.
- insert(val): Inserts an item val to the set if not already present.
- remove(val): Removes an item val from the set if present.
- getRandom: Returns a random element from current set of elements. Each element
must have the same probability of being returned.

Example:
// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();

Your RandomizedSet object will be instantiated and called as such:
randomSet = RandomizedSet()
randomSet = randomSet.insert(val)
randomSet = randomSet.remove(val)
randomSet = randomSet.getRandom()
"""

class RandomizedSetNumsAndNumPosDict(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import defaultdict

        # Use list to store nums and dict num->pos.
        self.nums = []
        self.num_pos = defaultdict()

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not
        already contain the specified element.

        :type val: int
        :rtype: bool

        Time complexity: O(1).
        Space complexity: O(n).
        """
        if val not in self.num_pos:
            self.nums.append(val)
            self.num_pos[val] = len(self.nums) - 1
            return True

        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained
        the specified element.

        :type val: int
        :rtype: bool

        Time complexity: O(1).
        Space complexity: O(n).
        """
        if val in self.num_pos:
            # Get val's position.
            val_pos = self.num_pos[val]

            # Replace val by the last num.
            last_num = self.nums[-1]
            self.nums[val_pos] = last_num
            self.num_pos[last_num] = val_pos

            # Remove val from nums and num_pos.
            self.nums.pop()
            del self.num_pos[val]

            return True

        return False

    def getRandom(self):
        """
        Get a random element from the set.

        :rtype: int

        Time complexity: O(1).
        Space complexity: O(1).
        """
        import random
        return random.choice(self.nums)


def main():
    randomSet = RandomizedSetNumsAndNumPosDict()

    # Inserts 1 to the set. Returns true as 1 was inserted successfully.
    print randomSet.insert(1);

    # Returns false as 2 does not exist in the set.
    print randomSet.remove(2);

    # Inserts 2 to the set, returns true. Set now contains [1,2].
    print randomSet.insert(2);

    # getRandom should return either 1 or 2 randomly.
    print randomSet.getRandom();

    # Removes 1 from the set, returns true. Set now contains [2].
    print randomSet.remove(1);

    # 2 was already in the set, so return false.
    print randomSet.insert(2);

    # Since 2 is the only number in the set, getRandom always return 2.
    print randomSet.getRandom();
    print randomSet.getRandom();


if __name__ == '__main__':
    main()
