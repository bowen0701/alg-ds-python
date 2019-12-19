"""Leetcode 404. Sum of Left Leaves
Easy

URL: https://leetcode.com/problems/sum-of-left-leaves/

Find the sum of all left leaves in a given binary tree.

Example:
    3
   / \
  9  20
    /  \
   15   7
There are two left leaves in the binary tree, with values 9 and 15 respectively. 
Return 24.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class SolutionRecur(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(logn) for balanced tree; O(n) for singly linked list.
        """
        # Base case.
        if not root:
            return 0

        if root.left and (not root.left.left and not root.left.right):
            return root.left.val + self.sumOfLeftLeaves(root.right)
        else:
            return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)


class SolutionIter(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(logn) for balanced tree; O(n) for singly linked list.
        """
        # Base case.
        if not root:
            return 0

        # Use stack for iteratively accumulate left leave sum.
        result = 0
        stack = [root]

        while stack:
            current = stack.pop()

            if current.left:
                if not current.left.left and not current.left.right:
                    # Accumualte result if it is a left leave.
                    result += current.left.val
                else:
                    # If not, add left node to stack.
                    stack.append(current.left)

            if current.right:
                if current.right.left or current.right.right:
                    # If right node is not a leave, add it to stack.
                    stack.append(current.right)

        return result


def main():
    # Output: 20.
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print SolutionRecur().sumOfLeftLeaves(root)
    print SolutionIter().sumOfLeftLeaves(root)


if __name__ == '__main__':
    main()
