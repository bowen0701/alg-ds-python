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
    def _kth_smallest_util(self, root):
        if root:
            self.kth_smallest_util(root.left)
            if k == 0:
                print root.val
            k -= 1
            self.kth_smallest_util(root.right)

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        self.kth_smallest_util(root)
        return root.val

        
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



if __name__ == '__main__':
    main()
