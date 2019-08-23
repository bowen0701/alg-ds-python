"""Leetcode 116. Populating Next Right Pointers in Each Node
Medium

URL: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

You are given a perfect binary tree where all leaves are on the same level,
and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node.
If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Input: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":{"$id":"6","left":null,"next":null,"right":null,"val":6},"next":null,"right":{"$id":"7","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}
Output: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4","left":null,"next":{"$id":"5","left":null,"next":{"$id":"6","left":null,"next":null,"right":null,"val":7},"right":null,"val":6},"right":null,"val":5},"right":null,"val":4},"next":{"$id":"7","left":{"$ref":"5"},"next":null,"right":{"$ref":"6"},"val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"7"},"val":1}

Explanation: Given the above perfect binary tree (Figure A),
your function should populate each next pointer to point to its next right node,
just like in Figure B.

Note:
- You may only use constant extra space.
- Recursive approach is fine, implicit stack space does not count as extra space
  for this problem.
"""

# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class SolutionRecur(object):
    def _preorder(self, node):
        if node and node.left:
            node.left.next = node.right
            
            if node.next:
                node.right.next = node.next.left
        
            self.connect(node.left)
            self.connect(node.right)

    def connect(self, root):
        """
        :type root: Node
        :rtype: Node

        Time complexity: O(n).
        Space complexity: O(1).
        """
        # Apply preorder traversal: root->left->right.
        self._preorder(root)
        return root


def main():
    root = Node(1, None, None, None)
    root.left = Node(2, None, None, None)
    root.right = Node(3, None, None, None)
    root.left.left = Node(4, None, None, None)
    root.left.right = Node(5, None, None, None)
    root.right.left = Node(6, None, None, None)
    root.right.right = Node(7, None, None, None)
    
    SolutionRecur().connect(root)

    print root.next                 # Ans: None
    print root.left.next.val        # Ans: 3
    print root.right.next           # Ans: None
    print root.left.left.next.val   # Ans: 5
    print root.left.right.next.val  # Ans: 6
    print root.right.left.next.val  # Ans: 7
    print root.right.right.next     # Ans: None  


if __name__ == '__main__':
    main()
