"""Leetcode 621. Task Scheduler
Medium

URL: https://leetcode.com/problems/task-scheduler/

Given a char array representing tasks CPU need to do. It contains capital letters
A to Z where different letters represent differenttasks. Tasks could be done
without original order. Each task could be done in one interval. For each
interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same
tasks, there must be at least n intervals that CPU are doing different tasks or
just be idle.

You need to return the least number of intervals the CPU will take to finish all
the given tasks.

Example:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.

Note:
- The number of tasks is in the range [1, 10000].
- The integer n is in the range [0, 100].
"""

class SolutionDictMaxHeap(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        from collections import defaultdict
        import heapq

        # Accumulate tasks's counts in dict.
        task_count_d = defaultdict(int)
        for t in tasks:
            task_count_d[t] += 1

        # Push tasks/counts into max heap (min heap with negative keys).
        neg_count_hq = [-c for c in task_count_d.values()]
        heapq.heapify(neg_count_hq)

        cycles = 0

        while neg_count_hq:
            # Use cycle_tasks to collect tasks, denoted by their negative counts.
            cycle_tasks = []
            for i in range(n + 1):
                if neg_count_hq:
                    cycle_tasks.append(-heapq.heappop(neg_count_hq))

            # If specific task remains after processed one, add back to maxheap.
            for j in cycle_tasks:
                if j - 1 > 0:
                    heapq.heappush(neg_count_hq, -(j - 1))

            # Add cycles for the last batch of tasks, or continue.  
            if not neg_count_hq:
                cycles += len(cycle_tasks)
            else:
                cycles += n + 1

        return cycles


def main():
    # Output: 8.
    tasks = ["A","A","A","B","B","B"]
    n = 2
    print SolutionDictMaxHeap().leastInterval(tasks, n)

    # Output: 16.
    tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
    n = 2
    print SolutionDictMaxHeap().leastInterval(tasks, n)


if __name__ == '__main__':
    main()
