"""Leetcode 621. Task Scheduler
Medium

URL: https://leetcode.com/problems/task-scheduler/

Given a char array representing tasks CPU need to do. It contains capital letters
A to Z where different letters represent different tasks. Tasks could be done
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

class SolutionTaskCountDictMaxHeap(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int

        Time complexity: O(m), where m is the length of tasks.
        Space complexity: O(m).
        """
        from collections import defaultdict
        import heapq

        # Create dict: task->count.
        task_count_d = defaultdict(int)
        for t in tasks:
            task_count_d[t] += 1

        # Push tasks/counts into max heap (min heap with negative keys).
        negcount_minheap = [-c for c in task_count_d.values()]
        heapq.heapify(negcount_minheap)

        n_cycles = 0

        while negcount_minheap:
            # Collect cycle tasks, denoted by their negative counts.
            cycle_tasks = []

            # Run n + 1 tasks, 1 for 1st task and n for cooling.
            for i in range(n + 1):
                if negcount_minheap:
                    cycle_tasks.append(-heapq.heappop(negcount_minheap))

            # If specific task exists after processed one, add back to maxheap.
            for j in cycle_tasks:
                if j > 1:
                    heapq.heappush(negcount_minheap, -(j - 1))

            # Add full cycles or add cycles for the last batch of tasks.  
            if negcount_minheap:
                n_cycles += n + 1
            else:
                n_cycles += len(cycle_tasks)

        return n_cycles


def main():
    # Output: 8.
    tasks = ["A","A","A","B","B","B"]
    n = 2
    print SolutionTaskCountDictMaxHeap().leastInterval(tasks, n)

    # Output: 16.
    tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
    n = 2
    print SolutionTaskCountDictMaxHeap().leastInterval(tasks, n)


if __name__ == '__main__':
    main()
