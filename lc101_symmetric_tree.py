"""Leetcode 101. Symmetric Tree
Easy

URL: https://leetcode.com/problems/symmetric-tree/

Given a binary tree, check whether it is a mirror of itself 
(ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
    1
   / \
  2   2
 / \ / \
3  4 4  3

But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3

Note:
Bonus points if you could solve it both recursively and iteratively.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self):
        self.root = None

    def insert(self, a_list):
        self.root = TreeNode(a_list[0])

        # Use queue to track current node.
        queue = []
        queue.insert(0, self.root)

        for i in range(1, len(a_list)):
            # Update the current node after inserting left and right nodes.
            if i % 2 == 1:
                current = queue.pop()

            # Insert to left node.
            if i % 2 == 1:
                if a_list[i]:
                    current.left = TreeNode(a_list[i])
                    queue.insert(0, current.left)
                else:
                    current.left = None
            # Insert to right node.
            elif i % 2 == 0:
                if a_list[i]:
                    current.right = TreeNode(a_list[i])
                    queue.insert(0, current.right)
                else:
                    current.right = None


class SolutionRecur(object):
    def isMirror(self, left, right):
        # Check left & right nodes' existence.
        if not left and not right:
            return True
        elif not left or not right:
            return False

        # Check left & right nodes' values and their children's mirroring.
        if left.val != right.val:
            return False
        else:
            out_pair = self.isMirror(left.left, right.right)
            in_pair = self.isMirror(left.right, right.left)
            return out_pair and in_pair

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool

        Time complexity: O(n).
        Space complexity: O(1).
        """
        if not root:
            return True

        return self.isMirror(root.left, root.right)


class SolutionIter(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        pass


def main():
    a_list = [1, 2, 2, 3, 4, 4, 3]
    # Output: True.
    bt = BinaryTree()
    bt.insert(a_list)
    print (bt.root.val, bt.root.left.val, bt.root.right.val,
           bt.root.left.left.val, bt.root.left.right.val,
           bt.root.right.left.val, bt.root.right.right.val)
    print SolutionRecur().isSymmetric(bt.root)

    a_list = [1, 2, 2, None, 3, None, 3]
    # Output: False.
    bt = BinaryTree()
    bt.insert(a_list)
    print (bt.root.val, bt.root.left.val, bt.root.right.val,
           None, bt.root.left.right.val,
           None, bt.root.right.right.val)
    print SolutionRecur().isSymmetric(bt.root)


if __name__ == '__main__':
    main()
