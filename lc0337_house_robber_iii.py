"""Leetcode 337. House Robber III
Medium

URL: https://leetcode.com/problems/house-robber-iii/

The thief has found himself a new place for his thievery again. There is
only one entrance to this area, called root.

Besides the root, each house has one and only one parent house. After a
tour, the smart thief realized that all houses in this place form a binary
tree. It will automatically contact the police if two directly-linked
houses were broken into on the same night.

Given the root of the binary tree, return the maximum amount of money the
thief can rob without alerting the police.

Example 1:
Input: root = [3,2,3,null,3,null,1]
Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Example 2:
Input: root = [3,4,5,1,3,null,1]
Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- 0 <= Node.val <= 10^4
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionRecur:
    def _recur(self, root):
        if not root:
            return 0

        # Rob root: skip children, rob grandchildren.
        amount_in = root.val
        if root.left:
            amount_in += self._recur(root.left.left) + self._recur(root.left.right)
        if root.right:
            amount_in += self._recur(root.right.left) + self._recur(root.right.right)

        # Skip root: rob children.
        amount_ex = self._recur(root.left) + self._recur(root.right)

        return max(amount_in, amount_ex)

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int

        Time complexity: O(2^n).
        Space complexity: O(n).
        """
        # Apply top-down recursion.
        return self._recur(root)


class SolutionMemo:
    def _recur(self, root, T):
        if not root:
            return 0

        if root in T:
            return T[root]

        # Rob root: skip children, rob grandchildren.
        amount_in = root.val
        if root.left:
            amount_in += self._recur(root.left.left, T) + self._recur(root.left.right, T)
        if root.right:
            amount_in += self._recur(root.right.left, T) + self._recur(root.right.right, T)

        # Skip root: rob children.
        amount_ex = self._recur(root.left, T) + self._recur(root.right, T)

        T[root] = max(amount_in, amount_ex)
        return T[root]

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(n).
        """
        # Apply top-down recursion with memoization.
        T = {}
        return self._recur(root, T)


class SolutionPostorder:
    def _postOrder(self, root):
        """Return (rob_root, skip_root) for the subtree."""
        if not root:
            return (0, 0)

        left_in, left_ex = self._postOrder(root.left)
        right_in, right_ex = self._postOrder(root.right)

        # Rob root: must skip both children.
        amount_in = root.val + left_ex + right_ex

        # Skip root: take the best of each child (rob or skip).
        left = max(left_in, left_ex)
        right = max(right_in, right_ex)
        amount_ex = left + right

        return (amount_in, amount_ex)

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(n).
        """
        # (Only) Postorder returning (rob, skip) tuple eliminates redundant subtree visits.
        return max(self._postOrder(root))


def main():
    # Output: 7.
    #     3
    #    / \
    #   2   3
    #    \   \
    #     3   1
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(1)
    print(SolutionRecur().rob(root))
    print(SolutionMemo().rob(root))
    print(SolutionPostorder().rob(root))

    # Output: 9.
    #     3
    #    / \
    #   4   5
    #  / \   \
    # 1   3   1
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(1)
    print(SolutionRecur().rob(root))
    print(SolutionMemo().rob(root))
    print(SolutionPostorder().rob(root))


if __name__ == '__main__':
    main()
