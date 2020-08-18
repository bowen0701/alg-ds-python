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


class SolutionMinMaxRecur(object):
    def _isValidBSTRecur(self, root, min_val, max_val):
        if not root:
            return True
        
        # Validate root's val
        if root.val <= min_val or root.val >= max_val:
            return False

        # Validate left and right subtrees.
        return (self._isValidBSTRecur(root.left, min_val, root.val) and
                self._isValidBSTRecur(root.right, root.val, max_val))

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool

        Time complexity: O(n).
        Space complexity: O(logn) for balanced tree; O(n) for single sided tree.
        """
        # Check if current val is in range (min, max).
        min_val, max_val = -float('inf'), float('inf')
        return self._isValidBSTRecur(root, min_val, max_val)


class SolutionMinMaxIter(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool

        Time complexity: O(n).
        Space complexity: O(logn) for balanced tree; O(n) for single sided tree.
        """
        # Check if current val is in range (min, max).
        if not root:
            return True

        # Use stack for DFS.
        min_val, max_val = -float('inf'), float('inf')
        stack = [(root, min_val, max_val)]

        while stack:
            current, min_val, max_val = stack.pop()
            if current.val <= min_val or current.val >= max_val:
                return False

            if current.right:
                stack.append([current.right, current.val, max_val])
            if current.left:
                stack.append([current.left, min_val, current.val])

        return True


class SolutionInorderRecur(object):
    def _isValidBSTRecur(self, root):
        if not root:
            return True
 
        # Traverse left tree.
        if not self._isValidBSTRecur(root.left):
            return False

        # Check if root val < previous val.
        if self.previous and self.previous.val >= root.val:
            return False

        # Update previous by root node.
        self.previous = root

        # Traverse right tree.
        if not self._isValidBSTRecur(root.right):
            return False

        return True

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool

        Time complexity: O(n).
        Space complexity: O(logn) for balanced tree; O(n) for single sided tree.
        """
        # Check if inorder traversal sees values in an increasing fashion.
        self.previous = None
        return self._isValidBSTRecur(root)


class SolutionInorderIter(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool

        Time complexity: O(n).
        Space complexity: O(logn) for balanced tree; O(n) for single sided tree.
        """
        # Check if inorder traversal sees values in an increasing fashion.
        if not root:
            return True

        previous = None
        current = root

        # Use stack for inorder traversal.
        stack = []

        while current or stack:
            while current:
                # If current exists, push to stack and visit leftmost node.
                stack.append(current)
                current = current.left

            # If current does not exist, pop stack as current.
            current = stack.pop()

            # Check if current val < previous val.
            if previous and previous.val >= current.val:
                return False

            # Update current and previous by inorder traversal.
            previous = current
            current = current.right

        return True


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
    print 'By MinMaxIter: {}'.format(SolutionMinMaxIter().isValidBST(root))
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'By InorderRecur: {}'.format(SolutionInorderRecur().isValidBST(root))
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'By InorderIter: {}'.format(SolutionInorderIter().isValidBST(root))
    print 'Time: {}'.format(time.time() - start_time)
    print '---'

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
    print 'By MinMaxIter: {}'.format(SolutionMinMaxIter().isValidBST(root))
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'By InorderRecur: {}'.format(SolutionInorderRecur().isValidBST(root))
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'By InorderIter: {}'.format(SolutionInorderIter().isValidBST(root))
    print 'Time: {}'.format(time.time() - start_time)
    print '---'

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
    print 'By MinMaxIter: {}'.format(SolutionMinMaxIter().isValidBST(root))
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'By InorderRecur: {}'.format(SolutionInorderRecur().isValidBST(root))
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'By InorderIter: {}'.format(SolutionInorderIter().isValidBST(root))
    print 'Time: {}'.format(time.time() - start_time)
    print '---'

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
    print 'By MinMaxIter: {}'.format(SolutionMinMaxIter().isValidBST(root))
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'By InorderRecur: {}'.format(SolutionInorderRecur().isValidBST(root))
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'By InorderIter: {}'.format(SolutionInorderIter().isValidBST(root))
    print 'Time: {}'.format(time.time() - start_time)


if __name__ == '__main__':
    main()
