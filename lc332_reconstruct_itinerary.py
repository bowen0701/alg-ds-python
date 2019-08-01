"""Leetcode 332. Reconstruct post_visits.
Medium

URL: https://leetcode.com/problems/reconstruct-post_visits/

Given a list of airline tickets represented by pairs of 
departure and arrival airports [from, to], reconstruct the post_visits in order. 
All of the tickets belong to a man who departs from JFK. 
Thus, the post_visits must begin with JFK.

Note:
If there are multiple valid itineraries, you should return the post_visits that 
has the smallest lexical order when read as a single string. 
For example, the post_visits ["JFK", "LGA"] has a smaller lexical order than 
["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid post_visits.

Example 1:
Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]

Example 2:
Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.
"""

class SolutionRecur(object):
    def _makeGraph(self, tickets):
        graph = {}
        
        for (start, end) in sorted(tickets)[::-1]:
            # Append airport in lexical order.
            if start not in graph:
                graph[start] = [end]
            else:
                graph[start] += [end]

        return graph

    def _dfs_recur(self, start, graph, post_visits):
        # Keep DFS after popping out next airport.
        while graph.get(start):
            self._dfs_recur(graph[start].pop(), graph, post_visits)

        post_visits.append(start)

    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]

        Time complexity: O(|E|log|E|), where 
          |E| is the number of tickets, due to sorting.
        Space complexity: O(|E|).
        """
        # Make a graph for post_visits's adjacency lists in lexical order.
        graph = self._makeGraph(tickets)

        # Vist airports by DFS on graph and track post_visits.
        post_visits = []
        start = 'JFK'
        self._dfs_recur(start, graph, post_visits)

        # Get itinerary by reverting the post_visits.
        itinerary = post_visits[::-1]
        return itinerary


class SolutionIter(object):
    def _makeGraph(self, tickets):
        graph = {}
        
        for (start, end) in sorted(tickets)[::-1]:
            # Append airport in lexical order.
            if start not in graph:
                graph[start] = [end]
            else:
                graph[start] += [end]

        return graph

    def _dfs_iter(self, start, graph, post_visits):
        stack = [start]

        # Keep DFS after popping out next airport.
        while stack:
            while graph.get(stack[-1]):
                stack.append(graph[stack[-1]].pop())

            post_visits.append(stack.pop())

    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        
        Time complexity: O(|E|log|E|), where 
          |E| is the number of tickets, due to sorting.
        Space complexity: O(|E|).
        """
        # Make a graph for post_visits's adjacency lists in lexical order.
        graph = self._makeGraph(tickets)

        # Vist airports by DFS on graph and track post_visits.
        post_visits = []
        start = 'JFK'
        self._dfs_iter(start, graph, post_visits)

        # Get itinerary by reverting the post_visits.
        itinerary = post_visits[::-1]
        return itinerary


def main():
    import time

    # Answer: ["JFK", "MUC", "LHR", "SFO", "SJC"]
    tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]

    start_time = time.time()
    print 'By recur: {}'.format(SolutionRecur().findItinerary(tickets))
    print 'Time: {}'.format(time.time() - start_time)
    
    start_time = time.time()
    print 'By iter: {}'.format(SolutionIter().findItinerary(tickets))
    print 'Time: {}'.format(time.time() - start_time)

    # Answer: ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
    tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]

    start_time = time.time()
    print 'By recur: {}'.format(SolutionRecur().findItinerary(tickets))
    print 'Time: {}'.format(time.time() - start_time)
    
    start_time = time.time()
    print 'By iter: {}'.format(SolutionIter().findItinerary(tickets))
    print 'Time: {}'.format(time.time() - start_time)

    # Answer: ["JFK","NRT","JFK","KUL"]
    tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]

    start_time = time.time()
    print 'By recur: {}'.format(SolutionRecur().findItinerary(tickets))
    print 'Time: {}'.format(time.time() - start_time)
    
    start_time = time.time()
    print 'By iter: {}'.format(SolutionIter().findItinerary(tickets))
    print 'Time: {}'.format(time.time() - start_time)


if __name__ == '__main__':
    main()
