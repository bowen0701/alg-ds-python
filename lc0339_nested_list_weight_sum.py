"""Leetcode 339. Nested List Weight Sum
Easy

URL: https://leetcode.com/problems/nested-list-weight-sum/

Given a nested list of integers, return the sum of all integers in the list
weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be
integers or other lists.

Example 1:
Input: [[1,1],2,[1,1]]
Output: 10 
Explanation: Four 1's at depth 2, one 2 at depth 1.

Example 2:
Input: [1,[4,[6]]]
Output: 27 
Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3;
1 + 4*2 + 6*3 = 27.
"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class SolutionDFSRecur(object):
    def _dfs(self, item, depth):
        if item.isInteger():
            return item.getInteger() * depth

        depth_sum = 0
        for neighbor in item.getList():
            depth_sum += self._dfs(neighbor, depth + 1)
        return depth_sum

    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int

        Time complexity: O(n), where n is the total elements.
        Space complexity: O(d), where d is the depth.
        """
        if not nestedList:
            return 0

        depth_sum = 0
        depth = 1
        for item in nestedList:
            depth_sum += self._dfs(item, depth)
        return depth_sum


class SolutionLevelBFS(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(w), where w is the biggest width.
        """
        from collections import deque

        if not nestedList:
            return 0

        depth_sum = 0
        depth = 0
        queue = deque(nestedList)

        while queue:
            depth += 1
            for i in range(len(queue)):
                item = queue.pop()
                if item.isInteger():
                    depth_sum += item.getInteger() * depth
                else:
                    for neighbor in item.getList():
                        queue.appendleft(neighbor)

        return depth_sum
