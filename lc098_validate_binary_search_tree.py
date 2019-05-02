"""Leetcode 98. Validate Binary Search Tree
Medium

URL: https://leetcode.com/problems/validate-binary-search-tree/

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the 
node's key. The right subtree of a node contains only nodes with keys 
greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 
Example 1:
    2
   / \
  1   3
Input: [2,1,3]
Output: true

Example 2:
    5
   / \
  1   4
     / \
    3   6
Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Definition for a binary tree.
class BinaryTree(object):
    def __init__(self):
        self.root = None

    def insert(self, a_list):
        self.root = TreeNode(a_list[0])

        stack = []
        stack.insert(0, self.root)

        for i in range(1, len(a_list)):
            # Update current node after inserting left and right nodes.
            if i % 2 == 1:
                current = stack.pop()

            # Left node.
            if i % 2 == 1:
                if a_list[i]:
                    current.left = TreeNode(a_list[i])
                    stack.insert(0, current.left)
                else:
                    current.left = None
            # Right node.
            elif i % 2 == 0:
                if a_list[i]:
                    current.right = TreeNode(a_list[i])
                    stack.insert(0, current.right)
                else:
                    current.right = None


class SolutionMinMax(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        min_val, max_val = float('-inf'), float('inf')
        return self.isValidBSTUtil(root, min_val, max_val)

    def isValidBSTUtil(self, root, min_val, max_val):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        if root.val <= min_val or root.val >= max_val:
            return False

        return (self.isValidBSTUtil(root.left, min_val, root.val) and
                self.isValidBSTUtil(root.right, root.val, max_val))


def main():
    # Input: [2,1,3]
    # Output: true
    bt = BinaryTree()
    bt.insert([2, 1, 3])
    print 'BT:', (bt.root.val, bt.root.left.val, bt.root.right.val)
    print 'isValidBST:', SolutionMinMax().isValidBST(bt.root)

    # Input: [5,1,4,null,null,3,6]
    # Output: false
    bt = BinaryTree()
    bt.insert([5, 1, 4, None, None, 3, 6])
    print 'BT:', (
        bt.root.val, bt.root.left.val, bt.root.right.val, None, None,
        bt.root.right.left.val, bt.root.right.right.val)
    print 'isValidBST:', SolutionMinMax().isValidBST(bt.root)

    # Input: [10,5,15,null,null,6,20]
    # Output: false
    bt = BinaryTree()
    bt.insert([10, 5, 15, None, None, 6, 20])
    print 'BT:', (
        bt.root.val, bt.root.left.val, bt.root.right.val, None, None,
        bt.root.right.left.val, bt.root.right.right.val)
    print 'isValidBST:', SolutionMinMax().isValidBST(bt.root)
    

if __name__ == '__main__':
    main()
