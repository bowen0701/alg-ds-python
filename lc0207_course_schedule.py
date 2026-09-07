"""Leetcode 207. Course Schedule
Medium

URL: https://leetcode.com/problems/course-schedule/

There are a total of numCourses courses you have to take, labeled from
0 to numCourses - 1. You are given an array prerequisites where
prerequisites[i] = [ai, bi] indicates that you must take course bi first
if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to
first take course 1.

Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0
you should also have finished course 1. So it is impossible.

Constraints:
- 1 <= numCourses <= 2000
- 0 <= prerequisites.length <= 5000
- prerequisites[i].length == 2
- 0 <= ai, bi < numCourses
- All the pairs prerequisites[i] are unique.
"""

from typing import Dict, List


class SolutionPrereqCoursesDFS:
    def _has_cycle_dfs(self, course: int, states: List[int], prereq_courses_d: Dict[int, List[int]]) -> bool:
        # If the course completed visiting
        if states[course] == 1:
            return False

        # If the course is being process: detected cycle.
        if states[course] == -1:
            return True

        # The course is not visited at all, start processing by recursive DFS.
        states[course] = -1

        for next_course in prereq_courses_d[course]:
            if self._has_cycle_dfs(next_course, states, prereq_courses_d):
                return True

        # If no cycle was detected, completed visiting.
        states[course] = 1
        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Time complexity: O(|V|+|E|), where
          - |V|: number of vertices, i.e. courses.
          - |E|: number of edges.
        Space complexity: O(|V|).
        """
        from collections import defaultdict

        # Build graph by dict: prereq->list(courses).
        prereq_courses_d = defaultdict(list)

        for course, prereq in prerequisites:
            prereq_courses_d[prereq].append(course)

        # Traverse graph to detect cycle using course state:
        # - state: 0, not visited at all, default state
        # - state: -1, being processed 
        # - state: 1, completed visiting
        states = [0] * numCourses

        for course in range(numCourses):
            if self._has_cycle_dfs(course, states, prereq_courses_d):
                return False

        return True


class SolutionPrereqCoursesBFSTopologicalSort:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Time complexity: O(|V|+|E|), where
          - |V|: number of vertices, i.e. courses.
          - |E|: number of edges.
        Space complexity: O(|V|).
        """
        # Apply BFS Topological Sort to take courses.
        from collections import defaultdict
        from collections import deque

        # Build graph by dict: prereq->list(courses) & courses's indegrees.
        prereq_courses_d = defaultdict(list)
        n_prereqs = [0] * numCourses

        for course, prereq in prerequisites:
            prereq_courses_d[prereq].append(course)
            n_prereqs[course] += 1

        # Create a queue for courses w/o prereq so they can be taken immediately.
        queue = deque()
        for course in range(numCourses):
            if n_prereqs[course] == 0:
                queue.appendleft(course)

        while queue:
            # Take course w/o prerequisites.
            course = queue.pop()
            numCourses -= 1

            # Take prereq's next courses after taking prereq.
            for nxt_course in prereq_courses_d[course]:
                # Decrement number of prerequisites of next course as prereq was taken.
                n_prereqs[nxt_course] -= 1

                # If no more prereq, add next course to queue to start taking it.
                if n_prereqs[nxt_course] == 0:
                    queue.appendleft(nxt_course)

        return numCourses == 0


def main():
    # Output: true
    numCourses = 2
    prerequisites = [[1,0]]
    print(SolutionPrereqCoursesBFSTopologicalSort().canFinish(numCourses, prerequisites))
    print(SolutionPrereqCoursesDFS().canFinish(numCourses, prerequisites))

    # Output: false
    numCourses = 2
    prerequisites = [[1,0],[0,1]]
    print(SolutionPrereqCoursesBFSTopologicalSort().canFinish(numCourses, prerequisites))
    print(SolutionPrereqCoursesDFS().canFinish(numCourses, prerequisites))

    # Output: false
    numCourses = 3
    prerequisites = [[1,0],[2,1],[0,2]]
    print(SolutionPrereqCoursesBFSTopologicalSort().canFinish(numCourses, prerequisites))
    print(SolutionPrereqCoursesDFS().canFinish(numCourses, prerequisites))


if __name__ == '__main__':
    main()
