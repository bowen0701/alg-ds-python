"""Leetcode 904. Fruit Into Baskets
Medium

URL: https://leetcode.com/problems/fruit-into-baskets/

In a row of trees, the i-th tree produces fruit with type tree[i].

You start at any tree of your choice, then repeatedly perform the following steps:
  1. Add one piece of fruit from this tree to your baskets. If you cannot, stop.
  2. Move to the next tree to the right of the current tree.
If there is no tree to the right, stop.
Note that you do not have any choice after the initial choice of starting tree:
you must perform step 1, then step 2, then back to step 1, then step 2,
and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit,
but you want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?

Example 1:
Input: [1,2,1]
Output: 3
Explanation: We can collect [1,2,1].

Example 2:
Input: [0,1,2,2]
Output: 3
Explanation: We can collect [1,2,2].
If we started at the first tree, we would only collect [0, 1].

Example 3:
Input: [1,2,3,2,2]
Output: 4
Explanation: We can collect [2,3,2,2].
If we started at the first tree, we would only collect [1, 2].

Example 4:
Input: [3,3,3,1,2,1,1,2,3,3,4]
Output: 5
Explanation: We can collect [1,2,1,1,2].
If we started at the first tree or the eighth tree, we would only collect 4 fruits.

Note:
- 1 <= tree.length <= 40000
- 0 <= tree[i] < tree.length
"""

class SolutionDictTwoPointers(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int

        Note: This problem is longest subsequence with only two characters.

        Time complexity: O(n).
        Space complexity: O(1).
        """
        from collections import defaultdict

        # Use dict to mimic fruit baskets with counts.
        fruit_count_d = defaultdict(int)
        max_len = 0

        # Apply two pointers method with left i & right j.
        i = 0
        for j, f in enumerate(tree):
            fruit_count_d[f] += 1

            # If more than 2 types, remove one fruit from the left. 
            while len(fruit_count_d) > 2:
                fruit_count_d[tree[i]] -= 1

                if fruit_count_d[tree[i]] == 0:
                    del fruit_count_d[tree[i]]

                i += 1

            max_len = max(max_len, j - i + 1)

        return max_len


def main():
    # Output: 3
    tree = [1,2,1]
    print SolutionDictTwoPointers().totalFruit(tree)

    # Output: 3
    tree = [0,1,2,2]
    print SolutionDictTwoPointers().totalFruit(tree)

    # Output: 4
    tree = [1,2,3,2,2]
    print SolutionDictTwoPointers().totalFruit(tree)

    # Output: 5.
    tree = [3,3,3,1,2,1,1,2,3,3,4]
    print SolutionDictTwoPointers().totalFruit(tree)    


if __name__ == '__main__':
    main()
