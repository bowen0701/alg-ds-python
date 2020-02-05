"""Leetcode 987. Vertical Order Traversal of a Binary Tree
Medium

URL: https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

Given a binary tree, return the vertical order traversal of its nodes values.

For each node at position (X, Y), its left and right children respectively will be
at positions (X-1, Y-1) and (X+1, Y-1).

Running a vertical line from X = -infinity to X = +infinity, whenever the vertical 
line touches some nodes, we report the values of the nodes in order from top to
bottom (decreasing Y coordinates).

If two nodes have the same position, then the value of the node that is reported
first is the value that is smaller.

Return an list of non-empty reports in order of X coordinate.
Every report will have a list of values of nodes.

Example 1:
     3
    / \
   9  20
      / \
     15  7
Input: [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation: 
Without loss of generality, we can assume the root node is at position (0, 0):
Then, the node with value 9 occurs at position (-1, -1);
The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
The node with value 20 occurs at position (1, -1);
The node with value 7 occurs at position (2, -2).

Example 2:
      1
    /   \
   2     3
  / \   / \
 4   5 6   7
Input: [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation: 
The node with value 5 and the node with value 6 have the same position according to the given scheme.
However, in the report "[1,5,6]", the node value of 5 comes first since 5 is smaller than 6.
 
Note:
- The tree will have between 1 and 1000 nodes.
- Each node's value will be between 0 and 1000.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class SolutionOrderValsDictSortedLevelOrderValsDict(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]

        Time complexity: O(n+n*logn), where n is number of nodes.
        Space complexity: O(n).
        """
        from collections import defaultdict
        from collections import deque

        # Create dict: vertical order->list(vals).
        vorder_vals_d = defaultdict(list)

        # Apply level traversal by queue.
        queue = deque([(root, 0)])

        while queue:
            # Create dict: level vertical order->list(vals) 
            level_vorder_vals_d = defaultdict(list)

            for i in range(len(queue)):
                current, vorder = queue.pop()
                level_vorder_vals_d[vorder].append(current.val)

                if current.left:
                    queue.appendleft((current.left, vorder - 1))
                if current.right:
                    queue.appendleft((current.right, vorder + 1))

            # After level traversal, append sorted vals to vorder_vals_d.
            for vorder, vals in level_vorder_vals_d.items():
                vorder_vals_d[vorder].extend(sorted(vals))

        # Sort dict by vertical order to return vals.
        return [vals for vorder, vals in sorted(vorder_vals_d.items())]


def main():
    # Input: [3,9,20,null,null,15,7]
    # Output: [[9],[3,15],[20],[7]]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print SolutionOrderValsDictSortedLevelOrderValsDict().verticalTraversal(root)

    # Input: [1,2,3,4,5,6,7]
    # Output: [[4],[2],[1,5,6],[3],[7]]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print SolutionOrderValsDictSortedLevelOrderValsDict().verticalTraversal(root)

    # Input: [0,2,1,3,null,null,null,4,5,null,7,6,null,10,8,11,9]
    # Output: [[4,10,11],[3,6,7],[2,5,8,9],[0],[1]]
    root = TreeNode(0)
    root.left = TreeNode(2)
    root.right = TreeNode(1)
    root.left.left = TreeNode(3)
    root.left.right = None
    root.right.left = None
    root.right.right = None
    root.left.left.left = TreeNode(4)
    root.left.left.right = TreeNode(5)
    root.left.left.left.right = TreeNode(7)
    root.left.left.right.left = TreeNode(6)
    root.left.left.left.right.left = TreeNode(10)
    root.left.left.left.right.right = TreeNode(8)
    root.left.left.right.left.left = TreeNode(11)
    root.left.left.right.left.right = TreeNode(9)
    print SolutionOrderValsDictSortedLevelOrderValsDict().verticalTraversal(root)


if __name__ == '__main__':
    main()
