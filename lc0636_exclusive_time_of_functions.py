"""Leetcode 636. Exclusive Time of Functions
Medium

URL: https://leetcode.com/problems/exclusive-time-of-functions/

On a single threaded CPU, we execute some functions. Each function has a unique id
between 0 and N-1.

We store logs in timestamp order that describe when a function is entered or exited.

Each log is a string with this format: "{function_id}:{"start" | "end"}:{timestamp}".
For example, "0:start:3" means the function with id 0 started at the beginning of
timestamp 3.  "1:end:2" means the function with id 1 ended at the end of timestamp 2.

A function's exclusive time is the number of units of time spent in this function.
Note that this does not include any recursive calls to child functions.

The CPU is single threaded which means that only one function is being executed at
a given time unit.

Return the exclusive time of each function, sorted by their function id.

Example 1:
Input:
n = 2
logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
Output: [3, 4]
Explanation:
Function 0 starts at the beginning of time 0, then it executes 2 units of time and
reaches the end of time 1.
Now function 1 starts at the beginning of time 2, executes 4 units of time and ends
at time 5.
Function 0 is running again at the beginning of time 6, and also ends at the end of
time 6, thus executing for 1 unit of time. 
So function 0 spends 2 + 1 = 3 units of total time executing, and function 1 spends
4 units of total time executing.

Note:
- 1 <= n <= 100
- Two functions won't start or end at the same time.
- Functions will always log when they exit.
"""


class SolutionStartStackIter(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]

        Time complexity: O(n).
        Space complexity: O(n).
        """
        # Use times to store fid's exec times.
        times = [0] * n

        # Use start_stack to store starting fid's logs.
        start_stack = []

        # logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
        for log in logs:
            fid, op, time = log.split(':')
            fid, time = int(fid), int(time)

            if op == 'start':
                # A new fid starts, add its log to stack.
                start_stack.append((fid, op, time))
            else:
                # A fid ends, since single thread, this fid must be equal to last fid.
                # Obtain its exec time.
                fid, op, start_time = start_stack.pop()
                times[fid] += time - start_time + 1

                # If there still exist running fid's, update its exec time by 
                # substracting last fid's exec time.
                if start_stack:
                    times[start_stack[-1][0]] -= time - start_time + 1

        return times


def main():
    # Output: [3, 4]
    n = 2
    logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
    print SolutionStartStackIter().exclusiveTime(n, logs)


if __name__ == '__main__':
    main()
