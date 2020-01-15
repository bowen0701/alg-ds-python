"""Leetcode 133. Clone Graph
Medium

URL: https://leetcode.com/problems/clone-graph/

Given a reference of a node in a connected undirected graph, return a deep copy
(clone) of the graph. Each node in the graph contains a val (int) and a list
(List[Node]) of its neighbors.
 
Example:
  1 -- 2
  |    |
  4 -- 3
Input:
{"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},
{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},
{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}
Explanation:
Node 1's value is 1, and it has two neighbors: Node 2 and 4.
Node 2's value is 2, and it has two neighbors: Node 1 and 3.
Node 3's value is 3, and it has two neighbors: Node 2 and 4.
Node 4's value is 4, and it has two neighbors: Node 1 and 3.
 
Note:
- The number of nodes will be between 1 and 100.
- The undirected graph is a simple graph, which means no repeated edges and no
  self-loops in the graph. 
- Since the graph is undirected, if node p has node q as neighbor, then node q
  must have node p as neighbor too.
- You must return the copy of the given node as a reference to the cloned graph.
"""

# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class SolutionNodeCopyDictBFS(object):
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

        if not node:
            return None

        copy = Node(node.val, [])

        # Create dict to map node->copied node, to avoid copying duplicated node.
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


class SolutionNodeCopyDictDFSRecur(object):
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

        if not node:
            return None

        copy = Node(node.val, [])
        node_copy_d = defaultdict()
        node_copy_d[node] = copy

        # Apply recursive DFS.
        self._dfs(node, node_copy_d)

        return copy


class SolutionNodeCopyDictDFSIter(object):
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
        from collections import deque

        if not node:
            return None

        copy = Node(node.val, [])
        node_copy_d = defaultdict()
        node_copy_d[node] = copy

        stack = deque([node])

        while stack:
            current = stack.pop()

            for neighbor in current.neighbors:
                if neighbor not in node_copy_d:
                    neighbor_copy = Node(neighbor.val, [])
                    node_copy_d[neighbor] = neighbor_copy

                    # Append neighbor to stack and break for DFS.
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

    print 'Apply BFS with queue:'
    node1_copy = SolutionNodeCopyDictBFS().cloneGraph(node1)
    print node1_copy.neighbors[0].val  # Should be 2.
    print node1_copy.neighbors[1].val  # Should be 4.
    print node1_copy.neighbors[0].neighbors[0].val  # Should be 1.
    print node1_copy.neighbors[0].neighbors[1].val  # Should be 3.
    print node1_copy.neighbors[1].neighbors[0].val  # Should be 1.
    print node1_copy.neighbors[1].neighbors[1].val  # Should be 3.
    print node1_copy.neighbors[0].neighbors[1].neighbors[0].val  # Should be 2.
    print node1_copy.neighbors[0].neighbors[1].neighbors[1].val  # Should be 4.

    print 'Apply recursive DFS:'
    node1_copy = SolutionNodeCopyDictDFSRecur().cloneGraph(node1)
    print node1_copy.neighbors[0].val  # Should be 2.
    print node1_copy.neighbors[1].val  # Should be 4.
    print node1_copy.neighbors[0].neighbors[0].val  # Should be 1.
    print node1_copy.neighbors[0].neighbors[1].val  # Should be 3.
    print node1_copy.neighbors[1].neighbors[0].val  # Should be 1.
    print node1_copy.neighbors[1].neighbors[1].val  # Should be 3.
    print node1_copy.neighbors[0].neighbors[1].neighbors[0].val  # Should be 2.
    print node1_copy.neighbors[0].neighbors[1].neighbors[1].val  # Should be 4.

    print 'Apply iterative DFS:'
    node1_copy = SolutionNodeCopyDictDFSIter().cloneGraph(node1)
    print node1_copy.neighbors[0].val  # Should be 2.
    print node1_copy.neighbors[1].val  # Should be 4.
    print node1_copy.neighbors[0].neighbors[0].val  # Should be 1.
    print node1_copy.neighbors[0].neighbors[1].val  # Should be 3.
    print node1_copy.neighbors[1].neighbors[0].val  # Should be 1.
    print node1_copy.neighbors[1].neighbors[1].val  # Should be 3.
    print node1_copy.neighbors[0].neighbors[1].neighbors[0].val  # Should be 2.
    print node1_copy.neighbors[0].neighbors[1].neighbors[1].val  # Should be 4.


if __name__ == '__main__':
    main()
