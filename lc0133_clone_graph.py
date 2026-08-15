"""Leetcode 133. Clone Graph
Medium

URL: https://leetcode.com/problems/clone-graph/

Given a reference of a node in a connected undirected graph, return a deep copy
(clone) of the graph. Each node in the graph contains a val (int) and a list
(List[Node]) of its neighbors.

Test case format:
For simplicity, each node's value is the same as the node's index (1-indexed).
For example, the first node with val == 1, the second node with val == 2, and
so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite
graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the
copy of the given node as a reference to the cloned graph.

Example 1:
  1 -- 2
  |    |
  4 -- 3
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

Example 2:
Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of
only one node with val = 1 and it does not have any neighbors.

Example 3:
Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.

Constraints:
- The number of nodes in the graph is in the range [0, 100].
- 1 <= Node.val <= 100
- Node.val is unique for each node.
- There are no repeated edges and no self-loops in the graph.
- The Graph is connected and all nodes can be visited starting from the given
  node.
"""

# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class SolutionNodeCopyDictBFS:
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node

        Apply BFS travdersal with a queue on the graph.

        Time complexity: O(|V|+|E|), where
          - |V|: number of nodes.
          - |E|: number of edges.
        Space complexity: O(|V|).
        """
        from collections import defaultdict
        from collections import deque

        # Edge case.
        if not node:
            return None

        copy = Node(node.val, [])

        # Create dict: node->copied node, to avoid copying duplicated node.
        node_copy_d = defaultdict()
        node_copy_d[node] = copy

        # Apply BFS with queue.
        queue = deque([node])

        while queue:
            current = queue.pop()

            for neighbor in current.neighbors:
                if neighbor not in node_copy_d:
                    # If current's neighbor is not visited, create a current copy.
                    neighbor_copy = Node(neighbor.val, [])
                    node_copy_d[neighbor] = neighbor_copy

                    queue.appendleft(neighbor)

                # Add neighbor's copy to current copy's neighbor.
                node_copy_d[current].neighbors.append(node_copy_d[neighbor])

        return copy


class SolutionNodeCopyDictDFSRecur:
    def _dfs(self, node, node_copy_d):
        for neighbor in node.neighbors:
            if neighbor not in node_copy_d:
                # If neighbor is not visited, create neighbor's copy.
                neighbor_copy = Node(neighbor.val, [])
                node_copy_d[neighbor] = neighbor_copy

                # Apply DFS.
                self._dfs(neighbor, node_copy_d)

            # Add neighbor's copy to node copy's neighbor.
            node_copy_d[node].neighbors.append(node_copy_d[neighbor])

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node

        Apply recursive DFS travdersal on the graph.

        Time complexity: O(|V|+|E|), where
          - |V|: number of nodes.
          - |E|: number of edges.
        Space complexity: O(|V|).
        """
        from collections import defaultdict

        # Edge case.
        if not node:
            return None

        copy = Node(node.val, [])

        # Create dict: node->copied node, to avoid copying duplicated node.
        node_copy_d = defaultdict()
        node_copy_d[node] = copy

        # Apply recursive DFS.
        self._dfs(node, node_copy_d)

        return copy


class SolutionNodeCopyDictDFSIter:
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node

        Apply iterative DFS travdersal on the graph.

        Time complexity: O(|V|+|E|), where
          - |V|: number of nodes.
          - |E|: number of edges.
        Space complexity: O(|V|).
        """
        from collections import defaultdict

        # Edge case.
        if not node:
            return None

        copy = Node(node.val, [])

        # Create dict: node->copied node, to avoid copying duplicated node.
        node_copy_d = defaultdict()
        node_copy_d[node] = copy

        stack = [node]

        while stack:
            current = stack.pop()

            for neighbor in current.neighbors:
                if neighbor not in node_copy_d:
                    neighbor_copy = Node(neighbor.val, [])
                    node_copy_d[neighbor] = neighbor_copy

                    # Append neighbor to stack.
                    stack.append(neighbor)

                node_copy_d[current].neighbors.append(node_copy_d[neighbor])

        return copy


def main():
    # Given a graph:
    # 1 -- 2
    # |    |
    # 4 -- 3
    node1 = Node(1, [])
    node2 = Node(2, [])
    node3 = Node(3, [])
    node4 = Node(4, [])
    node1.neighbors.append(node2)
    node1.neighbors.append(node4)
    node2.neighbors.append(node1)
    node2.neighbors.append(node3)
    node3.neighbors.append(node2)
    node3.neighbors.append(node4)
    node4.neighbors.append(node1)
    node4.neighbors.append(node3)

    print('Apply BFS with queue:')
    node1_copy = SolutionNodeCopyDictBFS().cloneGraph(node1)
    print(node1_copy.neighbors[0].val)  # Should be 2.
    print(node1_copy.neighbors[1].val)  # Should be 4.
    print(node1_copy.neighbors[0].neighbors[0].val)  # Should be 1.
    print(node1_copy.neighbors[0].neighbors[1].val)  # Should be 3.
    print(node1_copy.neighbors[1].neighbors[0].val)  # Should be 1.
    print(node1_copy.neighbors[1].neighbors[1].val)  # Should be 3.
    print(node1_copy.neighbors[0].neighbors[1].neighbors[0].val)  # Should be 2.
    print(node1_copy.neighbors[0].neighbors[1].neighbors[1].val)  # Should be 4.

    print('Apply recursive DFS:')
    node1_copy = SolutionNodeCopyDictDFSRecur().cloneGraph(node1)
    print(node1_copy.neighbors[0].val)  # Should be 2.
    print(node1_copy.neighbors[1].val)  # Should be 4.
    print(node1_copy.neighbors[0].neighbors[0].val)  # Should be 1.
    print(node1_copy.neighbors[0].neighbors[1].val)  # Should be 3.
    print(node1_copy.neighbors[1].neighbors[0].val)  # Should be 1.
    print(node1_copy.neighbors[1].neighbors[1].val)  # Should be 3.
    print(node1_copy.neighbors[0].neighbors[1].neighbors[0].val)  # Should be 2.
    print(node1_copy.neighbors[0].neighbors[1].neighbors[1].val)  # Should be 4.

    print('Apply iterative DFS:')
    node1_copy = SolutionNodeCopyDictDFSIter().cloneGraph(node1)
    print(node1_copy.neighbors[0].val)  # Should be 2.
    print(node1_copy.neighbors[1].val)  # Should be 4.
    print(node1_copy.neighbors[0].neighbors[0].val)  # Should be 1.
    print(node1_copy.neighbors[0].neighbors[1].val)  # Should be 3.
    print(node1_copy.neighbors[1].neighbors[0].val)  # Should be 1.
    print(node1_copy.neighbors[1].neighbors[1].val)  # Should be 3.
    print(node1_copy.neighbors[0].neighbors[1].neighbors[0].val)  # Should be 2.
    print(node1_copy.neighbors[0].neighbors[1].neighbors[1].val)  # Should be 4.


if __name__ == '__main__':
    main()
