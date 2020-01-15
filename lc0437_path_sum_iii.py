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


class SolutionLeadRecur(object):
    def _leadPathSum(self, root, sum):
        if not root:
            return 0

        # Single root val is sum.
        if root.val == sum:
            is_sum = 1
        else:
            is_sum = 0

        # With root val, count path sum leading by left/right node. 
        left_lead_paths = self._leadPathSum(root.left, sum - root.val)
        right_lead_paths = self._leadPathSum(root.right, sum - root.val)

        return is_sum + left_lead_paths + right_lead_paths

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int

        Time complexity: O(n*logn), for balanced tree; O(n^2) for single sided.
        Space complexity: O(logn) for balanced tree; O(n) for single sided.
        """
        # Sum lead path sum (with root) and path sums for left/right.

        if not root:
            return 0

        # Count path sum leading by root.
        lead_paths = self._leadPathSum(root, sum)

        # Recursively get path sum starting from left/right node.
        left_paths = self.pathSum(root.left, sum)
        right_paths = self.pathSum(root.right, sum)
        
        return lead_paths + left_paths + right_paths


class SolutionSumFreqMemo(object):
    def _dfs(self, root, sum, sum_freq_d, cur_sum):
        # Apply DFS in a preorder traversal fashion.
        if not root:
            return None

        # Accumulate current sum.
        cur_sum += root.val

        # Compute complemented path sum.
        complement_sum = cur_sum - sum

        # Update num of paths if complemented path sum exists.
        self.n_paths += sum_freq_d[complement_sum]

        # Update current path sum frequency.
        sum_freq_d[cur_sum] += 1

        # DFS for left/right nodes.
        self._dfs(root.left, sum, sum_freq_d, cur_sum)
        self._dfs(root.right, sum, sum_freq_d, cur_sum)

        # Backtrack when switch to another branch.
        sum_freq_d[cur_sum] -= 1

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int

        Time complexity: O(n), as traverse once.
        Space complexity: O(n), as extra space for memoization.
        """
        # Apply memoization to cache sum frequences.
        from collections import defaultdict

        self.n_paths = 0

        # Memoization by dict: sum->freq, similar with that for two-sum problem.
        sum_freq_d = defaultdict(int)
        sum_freq_d[0] = 1

        # Apply DFS with initial current sum 0.
        cur_sum = 0
        self._dfs(root, sum, sum_freq_d, cur_sum)
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

    print SolutionLeadRecur().pathSum(root, sum)
    print SolutionSumFreqMemo().pathSum(root, sum)


if __name__ == '__main__':
    main()
