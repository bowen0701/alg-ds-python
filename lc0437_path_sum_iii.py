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

from typing import Optional, Dict


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionPreorderLeadPathSumRecur(object):
    def _leadPathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # Check path sum leading by root.
        # Base case.
        if not root:
            return 0

        # Single root value matches sum.
        if root.val == targetSum:
            lead_sum = 1
        else:
            lead_sum = 0

        # Root path + path sum leading by left/right node.
        return (lead_sum
                + self._leadPathSum(root.left, targetSum - root.val)
                + self._leadPathSum(root.right, targetSum - root.val))

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        Time complexity: O(n*logn), for balanced tree; O(n^2) for single sided.
        Space complexity: O(logn) for balanced tree; O(n) for single sided.
        """
        # Check path sum within the tree under root.
        # Base case.
        if not root:
            return 0
        
        return (self._leadPathSum(root, targetSum)
                + self.pathSum(root.left, targetSum)
                + self.pathSum(root.right, targetSum))


class SolutionSumCountDictBacktracking(object):
    def _backtrack(
        self, 
        root: Optional[TreeNode], 
        targetSum: int, 
        sum_count_d: Dict[int, int], 
        cusum: int
    ) -> None:
        # Base case.
        if not root:
            return None

        # Preorder traversal with backtracking: root->left->right.
        # Update result if complemented path sum exists.
        cusum += root.val
        self.result += sum_count_d[cusum - targetSum]
        sum_count_d[cusum] += 1

        self._backtrack(root.left, targetSum, sum_count_d, cusum)
        self._backtrack(root.right, targetSum, sum_count_d, cusum)

        # Backtrack when switch to another branch.
        sum_count_d[cusum] -= 1

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        Time complexity: O(n), as traverse once.
        Space complexity: O(n), as extra space for memoization.
        """
        from collections import defaultdict

        # Use dict: sum->count, similar with two-sum problem.
        sum_count_d = defaultdict(int)
        sum_count_d[0] = 1

        # Apply DFS with initial current sum 0.
        self.result = 0
        cusum = 0
        self._backtrack(root, targetSum, sum_count_d, cusum)
        return self.result


def main():
    # Tree: [10,5,-3,3,2,null,11,3,-2,null,1]
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
    targetSum = 8

    print(SolutionPreorderLeadPathSumRecur().pathSum(root, targetSum))
    print(SolutionSumCountDictBacktracking().pathSum(root, targetSum))

    # Tree: [5,4,8,11,null,13,4,7,2,null,null,5,1]
    #       5
    #      /  \
    #     4    8
    #    /    /  \
    #  11    13   4
    #  / \       / \
    # 7   2     5   1
    # Output: 3
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)
    targetSum = 22

    print(SolutionPreorderLeadPathSumRecur().pathSum(root, targetSum))
    print(SolutionSumCountDictBacktracking().pathSum(root, targetSum))


if __name__ == '__main__':
    main()
