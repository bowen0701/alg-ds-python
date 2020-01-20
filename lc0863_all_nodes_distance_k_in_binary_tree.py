"""Leetcode 863. All Nodes Distance K in Binary Tree
Medium

URL: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

We are given a binary tree (with root node root), a target node, and an integer
value K.

Return a list of the values of all nodes that have a distance K from the target
node.  The answer can be returned in any order.

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
Output: [7,4,1]
Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.
Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.

Note:
- The given tree is non-empty.
- Each node in the tree has unique values 0 <= node.val <= 500.
- The target node is a node in the tree.
- 0 <= K <= 1000.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class SolutionUndirectedParentChildrenGraphBFS(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]

        Time complexity: O(n + |V|+|E|) = O(n+n+n) = O(n).
        Space complexity: O(n + |V|) = O(n).
        """
        from collections import defaultdict
        from collections import deque

        # Apply preorder traversal to build undirected graph: parent<->childrens.
        parent_children_d = defaultdict(list)
        stack = [(None, root)]
        while stack:
            parent, current = stack.pop()
            if parent and current:
                parent_children_d[parent.val].append(current.val)
                parent_children_d[current.val].append(parent.val)

            if current.right:
                stack.append((current, current.right))
            if current.left:
                stack.append((current, current.left))

        # Start from target, iterate BFS K times to collect node with distance K.
        queue = deque([target.val])
        visited = set([target.val])
        for i in range(K):
            for j in range(len(queue)):
                current = queue.pop()
                for neighbor in parent_children_d[current]:
                    if neighbor not in visited:
                        queue.appendleft(neighbor)
                        visited.add(neighbor)

        return list(queue)


def main():
    # Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
    # Output: [7,4,1]
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    target = root.left
    K = 2
    print SolutionUndirectedParentChildrenGraphBFS().distanceK(root, target, K)


if __name__ == '__main__':
    main()
