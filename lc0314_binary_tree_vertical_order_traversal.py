"""Leetcode 314. Binary Tree Vertical Order Traversal
Medium

URL: https://leetcode.com/problems/binary-tree-vertical-order-traversal/

Given a binary tree, return the vertical order traversal of its nodes' values.
(ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to
right.

Examples 1:
Input: [3,9,20,null,null,15,7]
   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7
Output:
[
  [9],
  [3,15],
  [20],
  [7]
]

Examples 2:
Input: [3,9,8,4,0,1,7]

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
Output:
[
  [4],
  [9],
  [3,0,1],
  [8],
  [7]
]

Examples 3:
Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left
child is 5)
     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
    /\
   /  \
   5   2
Output:
[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class SolutionOrderValsDictQueue(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]

        Time complexity: O(n).
        Space complexity: O(n).
        """
        from collections import defaultdict
        from collections import deque

        if not root:
            return []

        # Create dict: vertical order->list(node values).
        vorder_vals_d = defaultdict(list)

        # Use queue to add root and left/right with their orders to dict.
        queue = deque([(root, 0)])

        while queue:
            current, vorder = queue.pop()
            vorder_vals_d[vorder].append(current.val)

            if current.left:
                queue.appendleft((current.left, vorder - 1))
            if current.right:
                queue.appendleft((current.right, vorder + 1))

        # Return sorted list(node values) based on vertical order.
        vorder_vals = [vals for vorder, vals in sorted(vorder_vals_d.items())]
        return vorder_vals


def main():
    #    3
    #   /\
    #  /  \
    #  9  20
    #     /\
    #    /  \
    #   15   7
    # Output:
    # [
    #   [9],
    #   [3,15],
    #   [20],
    #   [7]
    # ]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(17)
    print SolutionOrderValsDictQueue().verticalOrder(root)

    #      3
    #     /\
    #    /  \
    #    9   8
    #   /\  /\
    #  /  \/  \
    #  4  01   7
    # Output:
    # [
    #   [4],
    #   [9],
    #   [3,0,1],
    #   [8],
    #   [7]
    # ]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(8)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(0)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(7)
    print SolutionOrderValsDictQueue().verticalOrder(root)

    #     3
    #    /\
    #   /  \
    #   9   8
    #  /\  /\
    # /  \/  \
    # 4  01   7
    #    /\
    #   /  \
    #   5   2
    # Output:
    # [
    #   [4],
    #   [9,5],
    #   [3,0,1],
    #   [8,2],
    #   [7]
    # ]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(8)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(0)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(7)
    root.left.right.right = TreeNode(2)
    root.right.left.left = TreeNode(5)
    print SolutionOrderValsDictQueue().verticalOrder(root)


if __name__ == '__main__':
    main()
