"""Leetcode 547. Friend Circles
Medium

URL: https://leetcode.com/problems/friend-circles/

There are N students in a class. Some of them are friends, while some are not.
Their friendship is transitive in nature. For example, if A is a direct friend
of B, and B is a direct friend of C, then A is an indirect friend of C.
And we defined a friend circle is a group of students who are direct or indirect
friends.

Given a N*N matrix M representing the friend relationship between students in
the class. If M[i][j] = 1, then the ith and jth students are direct friends
with each other, otherwise not. And you have to output the total number of
friend circles among all the students.

Example 1:
Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend
circle. 
The 2nd student himself is in a friend circle. So return 2.

Example 2:
Input: 
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students
are direct friends, 
so the 0th and 2nd students are indirect friends. All of them are in the same
friend circle, so return 1.

Note:
- N is in range [1,200].
- M[i][i] = 1 for all students.
- If M[i][j] = 1, then M[j][i] = 1.
"""

class SolutionDFS(object):
    def _dfs(self, i, M, visited):
        for neighbor, edge in enumerate(M[i]):
            if edge == 1 and neighbor not in visited:
                visited.add(neighbor)
                self._dfs(neighbor, M, visited)

    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int

        Time complexity: O(m*n), where
          - m: number of rows in M
          - n: number of columns in N
        Space complexity: O(m*n).
        """
        n = len(M)
        if n == 1:
            return 1

        circles = 0
        visited = set()

        for i in range(n):
            if i not in visited:
                circles += 1
                self._dfs(i, M, visited)

        return circles


def main():
    # Output: 2.
    M = [[1,1,0],
         [1,1,0],
         [0,0,1]]
    print SolutionDFS().findCircleNum(M)

    # Output: 1.
    M = [[1,1,0],
         [1,1,1],
         [0,1,1]]
    print SolutionDFS().findCircleNum(M)


if __name__ == '__main__':
    main()
