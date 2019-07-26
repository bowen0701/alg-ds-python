"""Leetcode 98. Validate Binary Search Tree

URL: https://leetcode.com/problems/validate-binary-search-tree/

Medium

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


class SolutionMinMaxRecur(object):
    def isValidBSTUtil(self, node, min_val, max_val):
        if not node:
            return True
        
        if node.val <= min_val or node.val >= max_val:
            return False

        return (self.isValidBSTUtil(node.left, min_val, node.val) and
                self.isValidBSTUtil(node.right, node.val, max_val))

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool

        Time complexity: O(n).
        Space complexity: O(n).
        """
        min_val, max_val = float('-inf'), float('inf')
        return self.isValidBSTUtil(root, min_val, max_val)


class SolutionInorderRecur(object):
    def isValidBSTUtil(self, node):
        if not node:
            return True
 
        # Start inorder traversal in an increasing fashion.
        # Traverse left tree.
        if not self.isValidBSTUtil(node.left):
            return False

        # Compare root with its previous.
        if self.previous and self.previous.val >= node.val:
            return False
        else:
            # Keep updating previous by current node.
            self.previous = node

        # Traverse right tree.
        if not self.isValidBSTUtil(node.right):
            return False

        return True

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool

        Time complexity: O(n).
        Space complexity: O(n).
        """
        self.previous = None
        return self.isValidBSTUtil(root)


def main():
    import time

    # Input: [2,1,3]
    #    2
    #   / \
    #  1   3
    # Output: true
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    start_time = time.time()
    print 'By MinMaxRecur: {}'.format(SolutionMinMaxRecur().isValidBST(root))
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'By InorderRecur: {}'.format(SolutionInorderRecur().isValidBST(root))
    print 'Time: {}'.format(time.time() - start_time)

    # Input: [5,1,4,null,null,3,6]
    #    5
    #   / \
    #  1   4
    #     / \
    #    3   6
    # Output: false
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)

    start_time = time.time()
    print 'By MinMaxRecur: {}'.format(SolutionMinMaxRecur().isValidBST(root))
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'By InorderRecur: {}'.format(SolutionInorderRecur().isValidBST(root))
    print 'Time: {}'.format(time.time() - start_time)

    # Input: [10,5,15,null,null,6,20]
    #      10
    #     /  \
    #    5   15
    #       /  \
    #      6   20
    # Output: false
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(20)

    start_time = time.time()
    print 'By MinMaxRecur: {}'.format(SolutionMinMaxRecur().isValidBST(root))
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'By InorderRecur: {}'.format(SolutionInorderRecur().isValidBST(root))
    print 'Time: {}'.format(time.time() - start_time)

    # Input:
    #      10
    #     /  \
    #    5   15
    #       /  \
    #      12   20
    #      /\
    #     6 14
    # Output: false
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(20)
    root.right.left.left = TreeNode(6)
    root.right.left.right = TreeNode(14)

    start_time = time.time()
    print 'By MinMaxRecur: {}'.format(SolutionMinMaxRecur().isValidBST(root))
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'By InorderRecur: {}'.format(SolutionInorderRecur().isValidBST(root))
    print 'Time: {}'.format(time.time() - start_time)


if __name__ == '__main__':
    main()
