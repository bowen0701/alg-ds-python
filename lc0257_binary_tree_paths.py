"""Leetcode 257. Binary Tree Paths
Easy

URL: https://leetcode.com/problems/binary-tree-paths/

Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:
Input:
   1
 /   \
2     3
 \
  5
Output: ["1->2->5", "1->3"]
Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class SolutionDFS(object):
    def _dfs(self, root, cur_path, paths):
        # Concat root's value.
        cur_path += str(root.val)

        # Check if root is leaf or not.
        if not root.left and not root.right:
            paths.append(cur_path)

        # Start DFS for left and right nodes respectively.
        if root.left:
            self._dfs(root.left, cur_path + '->', paths)
        if root.right:
            self._dfs(root.right, cur_path + '->', paths)

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]

        Time complexity: O(n).
        Space complexity: O(logn) for balanced tree; O(n) for singly-linked list.
        """
        # Check base case.
        if not root:
            return []

        # Apply DFS to collect paths.
        paths = []
        cur_path = ''
        self._dfs(root, cur_path, paths)
        return paths


def main():
    # Input:
    #    1
    #  /   \
    # 2     3
    #  \
    #   5
    # Output: ["1->2->5", "1->3"]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)

    print SolutionDFS().binaryTreePaths(root)


if __name__ == '__main__':
    main()
