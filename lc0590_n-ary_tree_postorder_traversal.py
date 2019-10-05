"""Leetcode 590. N-ary Tree Postorder Traversal
Easy

URL: https://leetcode.com/problems/n-ary-tree-postorder-traversal/

Given an n-ary tree, return the postorder traversal of its nodes' values.

For example, given a 3-ary tree:
      1
    / | \
   3  2  4
  / \
 5   6
Return its postorder traversal as: [5,6,3,2,4,1].

Note:
Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class SolutionRecur(object):
    def _postorderRrecur(self, root, vals):
        if not root:
            return None

        # Collect children nodes's vals first.
        for child in root.children:
            self._postorderRrecur(child, vals)

        # Collect root node's val.
        vals.append(root.val)

    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]

        Time complexity: O(n).
        Space complexity: O(n).
        """
        # Apply recursive postorder traversal.
        if not root:
            return []

        vals = []
        self._postorderRrecur(root, vals)
        return vals



def main():
    # For example, given a 3-ary tree:
    #       1
    #     / | \
    #    3  2  4
    #   / \
    #  5   6
    # Return its postorder traversal as: [5,6,3,2,4,1].
    root = Node(1, [])
    root.children.append(Node(3, []))
    root.children.append(Node(2, []))
    root.children.append(Node(4, []))
    root.children[0].children.append(Node(5, []))
    root.children[0].children.append(Node(6, []))
    print SolutionRecur().postorder(root)


if __name__ == '__main__':
    main()
