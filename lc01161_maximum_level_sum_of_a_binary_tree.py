"""Leetcode 1161. Maximum Level Sum of a Binary Tree
Medium

URL: https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

Given the root of a binary tree, the level of its root is 1, 
the level of its children is 2, and so on.

Return the smallest level X such that the sum of all the values of nodes
at level X is maximal.

Example 1:
Input: [1,7,0,7,-8,null,null]
     1
    / \
   7   0
  / \
 7  -8
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
 
Note:
- The number of nodes in the given tree is between 1 and 10^4.
- -10^5 <= node.val <= 10^5
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class SolutionLevelBFS(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Track current max sum and level id.
        max_sum = -float('inf')
        max_level = 0

        # Use queue for level BFS.
        queue = [root]
        cur_level = 0

        while queue:
            # Accumulate level sum.
            cur_level += 1
            level_sum = 0
            for i in range(len(queue)):
                current = queue.pop()
                level_sum += current.val

                # Insert left/right for further level BFS.
                if current.left:
                    queue.insert(0, current.left)
                if current.right:
                    queue.insert(0, current.right)  

            # Compare level sum and max sum, update the latter if needed.
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = cur_level             

        return max_level


def main():
    # Input: [1,7,0,7,-8,null,null]
    #      1
    #     / \
    #    7   0
    #   / \
    #  7  -8
    # Output: 2
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(0)
    root.left.left = TreeNode(7)
    root.left.right = TreeNode(-8)

    print SolutionLevelBFS().maxLevelSum(root)


if __name__ == '__main__':
    main()
