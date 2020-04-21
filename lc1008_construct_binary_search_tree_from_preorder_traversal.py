"""Leetcode 1008. Construct Binary Search Tree from Preorder Traversal
Medium

URL: https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

Return the root node of a binary search tree that matches the given
preorder traversal.

(Recall that a binary search tree is a binary tree where for every node,
any descendant of node.left has a value < node.val, and any descendant of
node.right has a value > node.val.  Also recall that a preorder traversal
displays the value of the node first, then traverses node.left, then
traverses node.right.)

Example 1:
Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]
     8
   /   \
  5    10
 / \     \
1   7    12

Note:
- 1 <= preorder.length <= 100
- The values of preorder are distinct.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class SolutionInsertBSTRecur(object):
    def _insertBSTRecur(self, val, root):
        new = TreeNode(val)

        if val < root.val:
            if not root.left:
                root.left = new
                return None
            else:
                self._insertBSTRecur(val, root.left)
        else:
            if not root.right:
                root.right = new
                return None
            else:
                self._insertBSTRecur(val, root.right)

    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode

        Time complexity: O(n*logn).
        Space complexity: O(logn).
        """
        # Edge case with one node.
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        # Convert preorder to deque for quick left-popping.
        val = preorder[0]
        root = TreeNode(val)

        # Iterate through all the remaining preorder vals to insert to BST.
        for i in range(1, len(preorder)):
            val = preorder[i]
            self._insertBSTRecur(val, root)
        return root


class SolutionBinarySearchRecur(object):
    def _binarySearchRecur(self, left, right):
        import bisect

        if left == right:
            return None

        # Use left to create root.
        val = self.preorder[left]
        root = TreeNode(val)

        # Apply binary search to find root't position to get left/right.
        mid = bisect.bisect(self.preorder, val, left + 1, right)
        root.left = self._binarySearchRecur(left + 1, mid)
        root.right = self._binarySearchRecur(mid, right)
        return root

    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode

        Time complexity: O(n*logn).
        Space complexity: O(logn).
        """
        self.preorder = preorder

        # Apply recursive binary search to find left & right subtrees.
        left, right = 0, len(preorder)
        return self._binarySearchRecur(left, right)



def main():
    import time

    # Input: [8,5,1,7,10,12]
    # Output: [8,5,10,1,7,null,12]
    #      8
    #    /   \
    #   5    10
    #  / \     \
    # 1   7    12
    preorder = [8,5,1,7,10,12]

    start_time = time.time()
    root = SolutionInsertBSTRecur().bstFromPreorder(preorder)
    print [root.val, 
           root.left.val, root.right.val,
           root.left.left.val, root.left.right.val,
           root.right.left, root.right.right.val]
    print 'Time for SolutionInsertBSTRecur: {}'.format(time.time() - start_time)

    start_time = time.time()
    root = SolutionBinarySearchRecur().bstFromPreorder(preorder)
    print [root.val, 
           root.left.val, root.right.val,
           root.left.left.val, root.left.right.val,
           root.right.left, root.right.right.val]
    print 'Time for SolutionBinarySearchRecur: {}'.format(time.time() - start_time)


if __name__ == '__main__':
    main()
