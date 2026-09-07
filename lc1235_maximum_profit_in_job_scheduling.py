"""Leetcode 1235. Maximum Profit in Job Scheduling
Hard

URL: https://leetcode.com/problems/maximum-profit-in-job-scheduling/

We have n jobs, where every job is scheduled to be done from
startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the
maximum profit you can take such that there are no two jobs in the
subset with overlapping time range.

If you choose a job that ends at time X you will be able to start
another job that starts at time X.

Example 1:
Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job.
Time range [1-3]+[3-6], we get profit of 50 + 70 = 120.

Example 2:
Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150
Explanation: The subset chosen is the first, fourth and fifth job.
Total profit is 20 + 70 + 60 = 150.

Example 3:
Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
Output: 6

Constraints:
- 1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
- 1 <= startTime[i] < endTime[i] <= 10^9
- 1 <= profit[i] <= 10^4
"""

from typing import List
import bisect


# Suffix subproblem: T[i] = max profit from jobs[i:].
# Top-down (recur/memo): starts at i=0 (data head), recurses toward i=n (base case).
# Bottom-up (DP): starts at i=n-1 (data tail), iterates toward i=0 (answer).


class SolutionRecur:
    def _recur(self, i: int, jobs: List[tuple]) -> int:
        if i >= len(jobs):
            return 0

        # Option 1: skip job i.
        skip_profit = self._recur(i + 1, jobs)

        # Option 2: take job i, find next non-overlapping job by linear scan.
        end_time = jobs[i][1]
        next_job = i + 1
        while next_job < len(jobs) and jobs[next_job][0] < end_time:
            next_job += 1

        take_profit = jobs[i][2] + self._recur(next_job, jobs)

        return max(skip_profit, take_profit)

    def jobScheduling(
        self,
        startTime: List[int],
        endTime: List[int],
        profit: List[int],
    ) -> int:
        """
        Time complexity: O(n * 2^n), where n is the number of jobs.
          - Each job has 2 choices (skip or take), no memoization.
          - Linear scan O(n) per call to find next non-overlapping job.
        Space complexity: O(n), for recursion stack.
        """
        jobs = sorted(zip(startTime, endTime, profit))
        return self._recur(0, jobs)


class SolutionMemo:
    def _recur(self, i: int, jobs: List[tuple], memo: dict) -> int:
        if i >= len(jobs):
            return 0

        if i in memo:
            return memo[i]

        # Option 1: skip job i.
        skip_profit = self._recur(i + 1, jobs, memo)

        # Option 2: take job i, find next non-overlapping job by linear scan.
        end_time = jobs[i][1]
        next_job = i + 1
        while next_job < len(jobs) and jobs[next_job][0] < end_time:
            next_job += 1

        take_profit = jobs[i][2] + self._recur(next_job, jobs, memo)

        memo[i] = max(skip_profit, take_profit)
        return memo[i]

    def jobScheduling(
        self,
        startTime: List[int],
        endTime: List[int],
        profit: List[int],
    ) -> int:
        """
        Time complexity: O(n^2).
          - n subproblems, each does O(n) linear scan.
        Space complexity: O(n).
        """
        jobs = sorted(zip(startTime, endTime, profit))
        memo = {}
        return self._recur(0, jobs, memo)


class SolutionMemo2:
    def _recur(self, i: int, jobs: List[tuple], memo: dict) -> int:
        if i >= len(jobs):
            return 0

        if i in memo:
            return memo[i]

        # Option 1: skip job i.
        skip_profit = self._recur(i + 1, jobs, memo)

        # Option 2: take job i, find next non-overlapping job.
        end_time = jobs[i][1]
        # Manual binary search for first job starting at or after end_time.
        lo, hi = i + 1, len(jobs)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if jobs[mid][0] < end_time:
                lo = mid + 1
            else:
                hi = mid

        take_profit = jobs[i][2] + self._recur(lo, jobs, memo)

        memo[i] = max(skip_profit, take_profit)
        return memo[i]

    def jobScheduling(
        self,
        startTime: List[int],
        endTime: List[int],
        profit: List[int],
    ) -> int:
        """
        Time complexity: O(n * log(n)).
          - Sorting O(n*logn); n subproblems, each O(logn) binary search.
        Space complexity: O(n).
        """
        jobs = sorted(zip(startTime, endTime, profit))
        memo = {}
        return self._recur(0, jobs, memo)


class SolutionMemo3:
    def _recur(
        self,
        i: int,
        jobs: List[tuple],
        start_times: List[int],
        memo: dict,
    ) -> int:
        if i >= len(jobs):
            return 0

        if i in memo:
            return memo[i]

        # Option 1: skip job i.
        skip_profit = self._recur(i + 1, jobs, start_times, memo)

        # Option 2: take job i, find next non-overlapping job via bisect.
        next_job = bisect.bisect_left(start_times, jobs[i][1])
        take_profit = jobs[i][2] + self._recur(next_job, jobs, start_times, memo)

        memo[i] = max(skip_profit, take_profit)
        return memo[i]

    def jobScheduling(
        self,
        startTime: List[int],
        endTime: List[int],
        profit: List[int],
    ) -> int:
        """
        Time complexity: O(n * log(n)).
          - Sorting O(n*logn); n subproblems, each O(logn) bisect search.
        Space complexity: O(n).
        """
        jobs = sorted(zip(startTime, endTime, profit))
        start_times = [j[0] for j in jobs]
        memo = {}
        return self._recur(0, jobs, start_times, memo)


class SolutionDP:
    def jobScheduling(
        self,
        startTime: List[int],
        endTime: List[int],
        profit: List[int],
    ) -> int:
        """
        Time complexity: O(n^2).
          - n iterations, each does O(n) linear scan.
        Space complexity: O(n).
        """
        n = len(startTime)
        jobs = sorted(zip(startTime, endTime, profit))

        # T[i] = max profit considering jobs[i:]; T[n] = 0 as base case.
        T = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            # Find next non-overlapping job by linear scan.
            end_time = jobs[i][1]
            next_job = i + 1
            while next_job < n and jobs[next_job][0] < end_time:
                next_job += 1

            # Take or skip.
            T[i] = max(jobs[i][2] + T[next_job], T[i + 1])

        return T[0]


class SolutionDP2:
    def jobScheduling(
        self,
        startTime: List[int],
        endTime: List[int],
        profit: List[int],
    ) -> int:
        """
        Time complexity: O(n * log(n)).
          - Sorting O(n*logn); n iterations, each O(logn) bisect search.
        Space complexity: O(n).
        """
        n = len(startTime)
        jobs = sorted(zip(startTime, endTime, profit))
        start_times = [j[0] for j in jobs]

        # T[i] = max profit considering jobs[i:]; T[n] = 0 as base case.
        T = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            # Find next non-overlapping job via bisect.
            next_job = bisect.bisect_left(start_times, jobs[i][1])

            # Take or skip.
            T[i] = max(jobs[i][2] + T[next_job], T[i + 1])

        return T[0]


def main():
    # Output: 120.
    startTime = [1, 2, 3, 3]
    endTime = [3, 4, 5, 6]
    profit = [50, 10, 40, 70]
    print(SolutionRecur().jobScheduling(startTime, endTime, profit))
    print(SolutionMemo().jobScheduling(startTime, endTime, profit))
    print(SolutionMemo2().jobScheduling(startTime, endTime, profit))
    print(SolutionMemo3().jobScheduling(startTime, endTime, profit))
    print(SolutionDP().jobScheduling(startTime, endTime, profit))
    print(SolutionDP2().jobScheduling(startTime, endTime, profit))

    # Output: 150.
    startTime = [1, 2, 3, 4, 6]
    endTime = [3, 5, 10, 6, 9]
    profit = [20, 20, 100, 70, 60]
    print(SolutionRecur().jobScheduling(startTime, endTime, profit))
    print(SolutionMemo().jobScheduling(startTime, endTime, profit))
    print(SolutionMemo2().jobScheduling(startTime, endTime, profit))
    print(SolutionMemo3().jobScheduling(startTime, endTime, profit))
    print(SolutionDP().jobScheduling(startTime, endTime, profit))
    print(SolutionDP2().jobScheduling(startTime, endTime, profit))

    # Output: 6.
    startTime = [1, 1, 1]
    endTime = [2, 3, 4]
    profit = [5, 6, 4]
    print(SolutionRecur().jobScheduling(startTime, endTime, profit))
    print(SolutionMemo().jobScheduling(startTime, endTime, profit))
    print(SolutionMemo2().jobScheduling(startTime, endTime, profit))
    print(SolutionMemo3().jobScheduling(startTime, endTime, profit))
    print(SolutionDP().jobScheduling(startTime, endTime, profit))
    print(SolutionDP2().jobScheduling(startTime, endTime, profit))


if __name__ == '__main__':
    main()
