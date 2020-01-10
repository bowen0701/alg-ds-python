"""Leetcode 230. Kth Smallest Element in a BST
Medium

URL: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Given a binary search tree, write a function kthSmallest to find the 
kth smallest element in it.

Note: 
You may assume k is always valid, 1 <= k <= BST's total elements.

Example 1:
Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3

Follow up:
What if the BST is modified (insert/delete operations) often and 
you need to find the kth smallest frequently? 
How would you optimize the kthSmallest routine?
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class SolutionInorderRecur(object):
    def _inorder(self, root):
        # Base case.
        if not root:
            return None

        # Inorder traversal: left->node->right.
        self._inorder(root.left)

        # Decrement k to 0 to get the kth smallest value.
        self.k -= 1
        if self.k == 0:
             self.kth_smallest = root.val
             return None

        self._inorder(root.right)

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int

        Time complexity: O(k).
        Space complexity: O(logn) for balanced tree; O(n) for single sided.
        """
        # Apply recursive inorder traversal.
        self.k = k
        self.kth_smallest = None

        self._inorder(root)
        return self.kth_smallest


class SolutionInorderIter(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int

        Time complexity: O(k).
        Space complexity: O(logn) for balanced tree; O(n) for single sided.
        """
        # Apply iterative inorder traversal.
        previous = None
        current = root

        stack = []

        while current or stack:
            # Continuously push current to stack and visit left node.
            while current:
                stack.append(current)
                current = current.left

            # Pop stack as current, which is left.
            current = stack.pop()

            # Decrement k to 0 to get the kth smallest value.
            k -= 1
            if k == 0:
                break

            # Then visit right.
            previous = current
            current = current.right

        return current.val

        
def main():
    # Input: root = [3,1,4,null,2], k = 1
    #    3
    #   / \
    #  1   4
    #   \
    #    2
    # Output: 1
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)
    k = 1

    print 'By recur: {}'.format(SolutionInorderRecur().kthSmallest(root, k))
    print 'By iter: {}'.format(SolutionInorderIter().kthSmallest(root, k))

    # Input: root = [5,3,6,2,4,null,null,1], k = 3
    #        5
    #       / \
    #      3   6
    #     / \
    #    2   4
    #   /
    #  1
    # Output: 3
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)
    k = 3

    print 'By recur: {}'.format(SolutionInorderRecur().kthSmallest(root, k))
    print 'By iter: {}'.format(SolutionInorderIter().kthSmallest(root, k))


if __name__ == '__main__':
    main()
