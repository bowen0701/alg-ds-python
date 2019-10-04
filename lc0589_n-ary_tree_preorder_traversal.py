"""Leetcode 589. N-ary Tree Preorder Traversal
Easy

URL: https://leetcode.com/problems/n-ary-tree-preorder-traversal/

Given an n-ary tree, return the preorder traversal of its nodes' values.

For example, given a 3-ary tree:
      1
    / | \
   3  2  4
  / \
 5   6
Return its preorder traversal as: [1,3,5,6,2,4].

Note:
Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class SolutionRecur(object):
    def _preorderRecur(self, root, vals):
        if not root:
            return None
        
        vals.append(root.val)
        for child in root.children:
            self._preorderRecur(child, vals)

    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]

        Time complexity: O(n).
        Space complexity: O(h), where h is the height of tree.
        """
        # Apply recursive preorder traversal.
        if not root:
            return []

        vals = []
        self._preorderRecur(root, vals)
        return vals

  
def main():
    root = Node(1, [])
    root.children.append(Node(3, []))
    root.children.append(Node(2, []))
    root.children.append(Node(4, []))
    root.children[0].children.append(Node(5, []))
    root.children[0].children.append(Node(6, []))

    print SolutionRecur().preorder(root)


if __name__ == '__main__':
    main()
