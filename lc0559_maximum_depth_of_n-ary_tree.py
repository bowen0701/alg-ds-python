"""Leetcode 559. Maximum Depth of N-ary Tree
Easy

URL: https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node
down to the farthest leaf node.

For example, given a 3-ary tree:
      1
    / | \
   3  2  4
  / \
 5   6
We should return its max depth, which is 3.

Note:
- The depth of the tree is at most 1000.
- The total number of nodes is at most 5000.
"""

# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        """
        :type val: int
        :type children: list
        :rtype: int
        """
        self.val = val
        self.children = children


class SolutionDFSRecur(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(n) for the worst case.
        """
        # Apply recursive DFS in preorder traversal fashion.
        if not root:
            return 0

        # Update child_depth for all children nodes.
        child_depth = 0
        for child in root.children:
            child_depth = max(child_depth, self.maxDepth(child))

        # Return single node depth (1) + child depth.
        return 1 + child_depth


class SolutionBFS(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(n) for the worst case.
        """
        # Apply (iterative) BFS to visit level in preorder traversal fashion.
        if not root:
            return 0

        depth = 0
        queue = [root]

        while queue:
            # Increment depth due to there is node in this level.
            depth += 1

            # Visit all nodes in the same level.
            for i in range(len(queue)):
                current = queue.pop()

                for child in current.children:
                    queue.insert(0, child)

        return depth


def main():
    # Output: 3
    root = Node(1, [])
    root.children.append(Node(3, []))
    root.children.append(Node(2, []))
    root.children.append(Node(4, []))
    root.children[0].children.append(Node(5, []))
    root.children[0].children.append(Node(6, []))

    print SolutionDFSRecur().maxDepth(root)
    print SolutionDFSRecur().maxDepth(root)


if __name__ == '__main__':
    main()
