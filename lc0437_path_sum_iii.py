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
            is_lead_sum = 1
        else:
            is_lead_sum = 0

        # With root val, count path sum leading by left/right node. 
        lead_left_path_sum = self._leadPathSum(root.left, sum - root.val)
        lead_right_path_sum = self._leadPathSum(root.right, sum - root.val)

        return is_lead_sum + lead_left_path_sum + lead_right_path_sum

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
        lead_path_sum = self._leadPathSum(root, sum)

        # Recursively get path sum starting from left/right node.
        left_path_sum = self.pathSum(root.left, sum)
        right_path_sum = self.pathSum(root.right, sum)
        
        return lead_path_sum + left_path_sum + right_path_sum


class SolutionSumFreqMemo(object):
    def _dfs(self, root, sum, sum_freqs, cur_path_sum):
        # Apply DFS in a preorder traversal fashion.
        if not root:
            return None

        # Accumulate current sum.
        cur_path_sum += root.val

        # Compute complemented path sum.
        comp_path_sum = cur_path_sum - sum

        # Update n_path_sums if complemented path sum exists.
        self.n_path_sums += sum_freqs[comp_path_sum]

        # Update current path sum frequency.
        sum_freqs[cur_path_sum] += 1

        # DFS for left/right nodes.
        self._dfs(root.left, sum, sum_freqs, cur_path_sum)
        self._dfs(root.right, sum, sum_freqs, cur_path_sum)

        # When switch to another branch, backtrack.
        sum_freqs[cur_path_sum] -= 1

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int

        Time complexity: O(n), as traverse once.
        Space complexity: O(n), as extra space for memoization.
        """
        from collections import defaultdict

        # Apply memoization to cache sum frequences.
        self.n_path_sums = 0

        # Memoization for sum frequences, initialized for sum=0->freq=1.
        # This technique is similar with the one for two sum problem.
        sum_freqs = defaultdict(int)
        sum_freqs[0] = 1

        # Initialize current sum.
        cur_path_sum = 0

        # Apply DFS with 
        self._dfs(root, sum, sum_freqs, cur_path_sum)

        return self.n_path_sums


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
