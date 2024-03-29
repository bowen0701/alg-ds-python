"""Leetcode 572. Subtree of Another Tree
Easy

URL: https://leetcode.com/problems/subtree-of-another-tree/

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure 
and node values with a subtree of s. 
A subtree of s is a tree consists of a node in s and all of this node's descendants.
The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:
     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.

Example 2:
Given tree s:
     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionPreorderSubtreeTreeMatchRecur:
    def _isTreeMatch(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base case.
        if (root and not subRoot) or (not root and subRoot):
            return False

        if not root and not subRoot:
            return True

        # Preorder traversal: root->left->right, to check root and left/right tree matches.
        if root.val != subRoot.val:
            return False

        return (self._isTreeMatch(root.left, subRoot.left)
                and self._isTreeMatch(root.right, subRoot.right))

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Time complexity: O(m*n), where m, n is the number of nodes in T and S.
        Space complexity: O(logm+logn), for balanced tree, O(m+n) for single sided tree.
        """
        # Base case.
        if not root:
            return False

        # Check tree match first: if yes return True, if not, start checking left/right subtrees.
        # Preorder traversal: root->left->right, check if matches or subtree of left or right.
        if self._isTreeMatch(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot)
                or self.isSubtree(root.right, subRoot))


class SolutionTreeSerializationBruteForceSubstringSearch:
    def _serialize(self, root: Optional[TreeNode], root_chars: List[Optional[int]]) -> None:
        # Base cases.
        if not root:
            root_chars.append('#')
            return None

        # Apply preorder traversal: root->left->right, to serialize tree.
        root_chars.append(str(root.val))
        self._serialize(root.left, root_chars)
        self._serialize(root.right, root_chars)

    def _substring_search(self, root_strs: List[str], sub_root_strs: List[str]) -> int:
        n_root = len(root_strs)
        n_sub_root = len(sub_root_strs)

        for i in range(n_root - n_sub_root):
            for j in range(n_sub_root):
                if root_strs[i + j] != sub_root_strs[j]:
                    break
                if j == n_sub_root - 1:
                    # Substring is matched.
                    return i

        # Substring is not matched.
        return n_root

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Time complexity: O(m*n + m + n) = O(m*n)
        Space complexity: O(m + n)
        """
        # Edge cases.
        if not root:
            return False

        # Apply preorder traversal for tree & subTree serialization.
        root_strs = []
        self._serialize(root, root_strs)

        sub_root_strs = []
        self._serialize(subRoot, sub_root_strs)

        # Apply substring search brute force algorithm.
        result = self._substring_search(root_strs, sub_root_strs)
        if result == len(root_strs):
            return False
        else:
            return True


class SolutionTreeSerializationKMPSubstringSearch:
    def _serialize(self, root: Optional[TreeNode], root_vals: List[str]) -> None:
        """
        Time complexity: O(n), where n is the number of nodes in tree.
        Space complexity: O(n).
        """
        # Base cases.
        if not root:
            root_vals.append("#")
            return None

        # Apply preorder traversal: root->left->right, to serialize tree.
        root_vals.append(str(root.val))
        self._serialize(root.left, root_vals)
        self._serialize(root.right, root_vals)

    def _kmp_preprocess(self, subroot_strs: List[str]) -> List[int]:
        """
        Time complexity: O(m), where m is the number of nodes in subtree.
        Space complexity: O(m).
        """
        m = len(subroot_strs)

        lps = [0] * m

        length = 0
        j = 1

        while j < m:
            if subroot_strs[j] == subroot_strs[length]:
                length += 1
                lps[j] = length
                j += 1
            elif length:
                length = lps[length - 1]
            else:
                lps[j] = 0
                j += 1

        return lps

    def _kmp_substring_search(self, root_strs: str, subroot_strs: str) -> int:
        """
        Time complexity: O(n + m).
        Space complexity: O(m), where m is the number of nodes in subtree. 
        """
        # Edge case.
        if not subroot_strs:
            return False

        n, m = len(root_strs), len(subroot_strs)

        # KMP preprocess to get the longest prefix suffix.
        lps = self._kmp_preprocess(subroot_strs)

        # KMP substring search.
        i = j = 0
        while i < n:
            if root_strs[i] == subroot_strs[j]:
                i += 1
                j += 1

            if j == m:
                return True
            elif i < n and root_strs[i] != subroot_strs[j]:
                # Mismatch after j matches.
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Time complexity: O(m + n).
        Space complexity: O(m + n).
        """
        # Edge cases.
        if not root:
            return False

        # Apply preorder traversal for tree serialization.
        root_strs, subroot_strs = [], []
        self._serialize(root, root_strs)
        self._serialize(subRoot, subroot_strs)

        # Apply KMP algorithm for string matching; see Leetcode 28. Implement strStr().
        return self._kmp_substring_search(root_strs, subroot_strs)


def main():
    import time

    # Given tree s:
    #      3
    #     / \
    #    4   5
    #   / \
    #  1   2
    # Given tree t:
    #    4 
    #   / \
    #  1   2
    # Output: True
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)
    subRoot = TreeNode(4)
    subRoot.left = TreeNode(1)
    subRoot.right = TreeNode(2)

    start_time = time.time()
    print(SolutionPreorderSubtreeTreeMatchRecur().isSubtree(root, subRoot))
    print(f"PreorderSubtreeTreeMatchRecur: {time.time() - start_time}")

    start_time = time.time()
    print(SolutionTreeSerializationBruteForceSubstringSearch().isSubtree(root, subRoot))
    print(f"TreeSerializationBruteForceSubstringSearch: {time.time() - start_time}")

    start_time = time.time()
    print(SolutionTreeSerializationKMPSubstringSearch().isSubtree(root, subRoot))
    print(f"TreeSerializationKMPSubstringSearch: {time.time() - start_time}")

    # Given tree s:
    #      3
    #     / \
    #    4   5
    #   / \
    #  1   2
    #     /
    #    0
    # Given tree t:
    #    4
    #   / \
    #  1   2
    # Output: False
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(0)
    subRoot = TreeNode(4)
    subRoot.left = TreeNode(1)
    subRoot.right = TreeNode(2)

    start_time = time.time()
    print(SolutionPreorderSubtreeTreeMatchRecur().isSubtree(root, subRoot))
    print(f"PreorderSubtreeTreeMatchRecur: {time.time() - start_time}")

    start_time = time.time()
    print(SolutionTreeSerializationBruteForceSubstringSearch().isSubtree(root, subRoot))
    print(f"TreeSerializationBruteForceSubstringSearch: {time.time() - start_time}")

    start_time = time.time()
    print(SolutionTreeSerializationKMPSubstringSearch().isSubtree(root, subRoot))
    print(f"TreeSerializationKMPSubstringSearch: {time.time() - start_time}")


if __name__ == '__main__':
    main()
