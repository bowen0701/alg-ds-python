"""Leetcode 429. N-ary Tree Level Order Traversal
Easy

URL: https://leetcode.com/problems/n-ary-tree-level-order-traversal/

Given an n-ary tree, return the level order traversal of its nodes' values.
(ie, from left to right, level by level).

For example, given a 3-ary tree:
      1
    / | \
   3  2  4
  / \
 5   6
We should return its level order traversal:
[
     [1],
     [3,2,4],
     [5,6]
]

Note:
- The depth of the tree is at most 1000.
- The total number of nodes is at most 5000.
"""

# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class SolutionBFS(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]

        Time complexity: O(n).
        Space complexity: O(n).
        """
        # Apply BFS with queue.
        if not root:
            return []

        vals = []
        queue = [root]

        while queue:
            # Collect values in level.
            level = []

            # Iterate over nodes in a level.
            for i in range(len(queue)):
                current = queue.pop()
                level.append(current.val)

                # Insert current's children into queue for further BFS.
                for child in current.children:
                    queue.insert(0, child)

            vals.append(level)

        return vals


def main():
    # For example, given a 3-ary tree:
    #       1
    #     / | \
    #    3  2  4
    #   / \
    #  5   6
    # Return its level-order traversal as: [[1], [3,2,4], [5,6]].
    root = Node(1, [])
    root.children.append(Node(3, []))
    root.children.append(Node(2, []))
    root.children.append(Node(4, []))
    root.children[0].children.append(Node(5, []))
    root.children[0].children.append(Node(6, []))

    print SolutionBFS().levelOrder(root)


if __name__ == '__main__':
    main()
