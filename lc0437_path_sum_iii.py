"""Leetcode 437. Path Sum III
Easy (?)

URL: https://leetcode.com/problems/path-sum-iii/

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf,
but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range
-1,000,000 to 1,000,000.

Example:
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1
Return 3. The paths that sum to 8 are:
1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class SolutionLeadPathSumRecur(object):
    def _leadPathSum(self, root, sum):
        if not root:
            return 0

        # Single root val is sum.
        if root.val == sum:
            is_root_sum = 1
        else:
            is_root_sum = 0

        # Including root val, count path sum leading by left/right node.
        return (is_root_sum
                + self._leadPathSum(root.left, sum - root.val)
                + self._leadPathSum(root.right, sum - root.val))

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int

        Time complexity: O(n*logn), for balanced tree; O(n^2) for single sided.
        Space complexity: O(logn) for balanced tree; O(n) for single sided.
        """
        if not root:
            return 0
        
        return (self._leadPathSum(root, sum)
                + self.pathSum(root.left, sum)
                + self.pathSum(root.right, sum))


class SolutionSumCountDictBacktracking(object):
    def _backtrack(self, root, sum, sum_count_d, cusum):
        # Apply DFS in a preorder traversal fashion.
        if not root:
            return None

        # Update num of paths if complemented path sum exists.
        cusum += root.val
        self.n_paths += sum_count_d[cusum - sum]

        # Update path sum count.
        sum_count_d[cusum] += 1

        # DFS for left/right nodes.
        self._backtrack(root.left, sum, sum_count_d, cusum)
        self._backtrack(root.right, sum, sum_count_d, cusum)

        # Backtrack when switch to another branch.
        sum_count_d[cusum] -= 1

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int

        Time complexity: O(n), as traverse once.
        Space complexity: O(n), as extra space for memoization.
        """
        from collections import defaultdict

        # Use dict: sum->count, similar with two-sum problem.
        sum_count_d = defaultdict(int)
        sum_count_d[0] = 1

        # Apply DFS with initial current sum 0.
        self.n_paths = 0
        cusum = 0
        self._backtrack(root, sum, sum_count_d, cusum)
        return self.n_paths


def main():
    #       10
    #      /  \
    #     5   -3
    #    / \    \
    #   3   2   11
    #  / \   \
    # 3  -2   1
    # Output: 3
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(-3)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(2)
    root.right.right = TreeNode(11)
    root.left.left.left = TreeNode(3)
    root.left.left.right = TreeNode(-2)
    root.left.right.right = TreeNode(1)
    sum = 8

    print SolutionLeadPathSumRecur().pathSum(root, sum)
    print SolutionSumCountDictBacktracking().pathSum(root, sum)


if __name__ == '__main__':
    main()
