"""Leetcode 785. Is Graph Bipartite?
Medium

URL: https://leetcode.com/problems/is-graph-bipartite/

Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split it's set of nodes into two
independent subsets A and B such that every edge in the graph has one node in A
and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for
which the edge between nodes i and j exists.  Each node is an integer between 0
and graph.length - 1.  There are no self edges or parallel edges: graph[i] does
not contain i, and it doesn't contain any element twice.

Example 1:
Input: [[1,3], [0,2], [1,3], [0,2]]
Output: true
Explanation: 
The graph looks like this:
0----1
|    |
|    |
3----2
We can divide the vertices into two groups: {0, 2} and {1, 3}.

Example 2:
Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
Output: false
Explanation: 
The graph looks like this:
0----1
| \  |
|  \ |
3----2
We cannot find a way to divide the set of nodes into two independent subsets.
 
Note:
- graph will have length in range [1, 100].
- graph[i] will contain integers in range [0, graph.length - 1].
- graph[i] will not contain i or duplicate values.
- The graph is undirected: if any element j is in graph[i], then i will be in 
  graph[j].
"""

class SolutionNodeSetidDictDFSRecur(object):
    def _dfs(self, i, graph, node_setid):
        for j in graph[i]:
            if j in node_setid:
                # If connected nodes have the same set id.
                if node_setid[j] == node_setid[i]:
                    return False
            else:
                # If not, add j to the set with diff set id. 
                node_setid[j] = 1 - node_setid[i]

                # Continue DFS from node j.
                is_bipartite = self._dfs(j, graph, node_setid)
                if not is_bipartite:
                    return False

        return True

    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]; a adjacency matrix.
        :rtype: bool

        Apply recursive DFS through connected nodes to add to different sets.

        Time complexity: O(|V|+|E|), where
          - |V| is the number of nodes.
          - |E| is the number of edges.
        Space complexity: O(|V|).
        """
        # Edge cases: if only one or two nodes.
        if len(graph) <= 2:
            return True

        # Use dict: node->setid={0,1} to denote visits and binary setid.
        node_setid = dict()

        for i in range(len(graph)):
            if i not in node_setid:
                # For disconnected node, set setid = 0 (anyoness).
                node_setid[i] = 0

                # Start DFS from node i.
                is_bipartite = self._dfs(i, graph, node_setid)

                if not is_bipartite:
                    # If one node cannot be added, return False.
                    return False

        return True


def main():
    # Input: [[1,3], [0,2], [1,3], [0,2]]
    # Output: true
    graph = [[1,3], [0,2], [1,3], [0,2]]
    print SolutionNodeSetidDictDFSRecur().isBipartite(graph)

    # Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
    # Output: true
    graph = [[1,2,3], [0,2], [0,1,3], [0,2]]
    print SolutionNodeSetidDictDFSRecur().isBipartite(graph)


if __name__ == '__main__':
    main()
