"""Leetcode 210. Course Schedule II
Medium

URL: https://leetcode.com/problems/course-schedule-ii/

There are a total of numCourses courses you have to take, labeled from
0 to numCourses - 1. You are given an array prerequisites where
prerequisites[i] = [ai, bi] indicates that you must take course bi first
if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have
to first take course 1.

Return the ordering of courses you should take to finish all courses.
If there are many valid answers, return any of them. If it is impossible
to finish all courses, return an empty array.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1
you should have finished course 0. So the correct course order is [0,1].

Example 2:
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3
you should have finished both courses 1 and 2. Both courses 1 and 2
should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is
[0,2,1,3].

Example 3:
Input: numCourses = 1, prerequisites = []
Output: [0]

Constraints:
- 1 <= numCourses <= 2000
- 0 <= prerequisites.length <= numCourses * (numCourses - 1)
- prerequisites[i].length == 2
- 0 <= ai, bi < numCourses
- ai != bi
- All the pairs [ai, bi] are distinct.
"""

from typing import Dict, List
from collections import defaultdict, deque


class SolutionCoursePrereqsDFS:
    def _has_cycle_dfs(
        self,
        course: int,
        states: List[int],
        course_prereqs_d: Dict[int, List[int]],
        order: List[int],
    ) -> bool:
        # If the course completed visiting.
        if states[course] == 1:
            return False

        # If the course is being processed: detected cycle.
        if states[course] == -1:
            return True

        # The course is not visited at all, start processing by recursive DFS.
        states[course] = -1

        for prereq in course_prereqs_d[course]:
            if self._has_cycle_dfs(prereq, states, course_prereqs_d, order):
                return True

        # If no cycle was detected, completed visiting.
        # Add to order: prereqs are appended before this course (postorder).
        states[course] = 1
        order.append(course)
        return False

    def findOrder(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
    ) -> List[int]:
        """
        Time complexity: O(|V|+|E|), where
          - |V|: number of vertices, i.e. courses.
          - |E|: number of edges.
        Space complexity: O(|V|+|E|), for adjacency list built in function.
        """
        # Build graph by dict: course->list(prereqs) (not prereqs_course_d as LC207).
        # By this course_prereqs_d DFS recurses into prereqs first, so prereqs are appended before dependents.
        course_prereqs_d = defaultdict(list)
        for course, prereq in prerequisites:
            course_prereqs_d[course].append(prereq)

        # Traverse graph to detect cycle using course state:
        # - state: 0, not visited at all, default state
        # - state: -1, being processed
        # - state: 1, completed visiting
        states = [0] * numCourses
        order = []

        for course in range(numCourses):
            if self._has_cycle_dfs(course, states, course_prereqs_d, order):
                return []

        # If using prereq->courses (prereq_courses_d), need order[::-1].
        return order


class SolutionPrereqCoursesBFSTopologicalSort:
    def findOrder(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
    ) -> List[int]:
        """
        Time complexity: O(|V|+|E|), where
          - |V|: number of vertices, i.e. courses.
          - |E|: number of edges.
        Space complexity: O(|V|+|E|), for adjacency list built in function.
        """
        # Build graph by dict: prereq->list(courses) & course indegrees.
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

        order = []

        while queue:
            # Take course w/o prerequisites.
            course = queue.pop()
            order.append(course)

            # Unlock follow-up courses that depend on this course.
            for next_course in prereq_courses_d[course]:
                n_prereqs[next_course] -= 1

                # If no more prereq, add next course to queue to start taking it.
                if n_prereqs[next_course] == 0:
                    queue.appendleft(next_course)

        if len(order) == numCourses:
            return order
        else:
            return []


def main():
    # Output: [0, 1]
    numCourses = 2
    prerequisites = [[1, 0]]
    print(SolutionCoursePrereqsDFS().findOrder(numCourses, prerequisites))
    print(SolutionPrereqCoursesBFSTopologicalSort().findOrder(numCourses, prerequisites))

    # Output: [0, 2, 1, 3] or [0, 1, 2, 3]
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    print(SolutionCoursePrereqsDFS().findOrder(numCourses, prerequisites))
    print(SolutionPrereqCoursesBFSTopologicalSort().findOrder(numCourses, prerequisites))

    # Output: [0]
    numCourses = 1
    prerequisites = []
    print(SolutionCoursePrereqsDFS().findOrder(numCourses, prerequisites))
    print(SolutionPrereqCoursesBFSTopologicalSort().findOrder(numCourses, prerequisites))

    # Output: [] (cycle)
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
    print(SolutionCoursePrereqsDFS().findOrder(numCourses, prerequisites))
    print(SolutionPrereqCoursesBFSTopologicalSort().findOrder(numCourses, prerequisites))


if __name__ == '__main__':
    main()
