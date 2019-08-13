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


class SolutionRecur(object):
    def _kthSmallestUtil(self, root):
        if root:
            self._kthSmallestUtil(root.left)

            # Decrement k and check if k is 0, 
            # then current node's val is the kth smallest value.
            self.k -= 1
            if self.k == 0:
                 self.k_smallest = root.val

            self._kthSmallestUtil(root.right)

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(1).
        """
        self.k = k
        self.k_smallest = None

        self._kthSmallestUtil(root)
        return self.k_smallest


class SolutionIter(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int

        Time complexity: O(k).
        Space complexity: O(1).
        """
        previous = None
        current = root

        stack = []

        while current or stack:
            if current:
                # If current exists, push to stack and visit left node.
                stack.append(current)
                current = current.left
            else:
                # If not, pop stack as current.
                current = stack.pop()

                # Decrement k and check if k is 0, 
                # then current node's value is the kth smallest.
                k -= 1
                if k == 0:
                    break

                # Update previous & current by current & current.right.
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

    print 'By recur: {}'.format(SolutionRecur().kthSmallest(root, k))
    print 'By iter: {}'.format(SolutionIter().kthSmallest(root, k))

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

    print 'By recur: {}'.format(SolutionRecur().kthSmallest(root, k))
    print 'By iter: {}'.format(SolutionIter().kthSmallest(root, k))


if __name__ == '__main__':
    main()
