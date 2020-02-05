"""Leetcode 199. Binary Tree Right Side View
Medium

URL: https://leetcode.com/problems/binary-tree-right-side-view/

Given a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

Example:
Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class SolutionLevelTraversalLast(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]

        Time complexity: O(n).
        Space complexity: O(n).
        """
        from collections import deque

        # Base case.
        if not root:
            return []

        right_vals = []

        # Apply level traversal to collect right side values.
        queue = deque([root])

        while queue:
            size = len(queue)
            for i in range(size):
                current = queue.pop()
                if i == size - 1:
                    right_vals.append(current.val)

                # Add current's left/right to queue if existed.
                if current.left:
                    queue.appendleft(current.left)
                if current.right:
                    queue.appendleft(current.right)

        return right_vals


def main():
    # Input:
    #    1
    #  /   \
    # 2     3
    #  \     \
    #   5     4
    # Output: [1, 3, 4]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)

    print SolutionLevelTraversalLast().rightSideView(root)


if __name__ == '__main__':
    main()
