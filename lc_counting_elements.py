"""Counting Elements

URL: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3289/

Given an integer array arr, count element x such that x + 1 is also in arr.

If there're duplicates in arr, count them seperately.

Example 1:
Input: arr = [1,2,3]
Output: 2
Explanation: 1 and 2 are counted cause 2 and 3 are in arr.

Example 2:
Input: arr = [1,1,3,3,5,5,7,7]
Output: 0
Explanation: No numbers are counted, cause there's no 2, 4, 6, or 8 in arr.

Example 3:
Input: arr = [1,3,2,3,5,0]
Output: 3
Explanation: 0, 1 and 2 are counted cause 1, 2 and 3 are in arr.

Example 4:
Input: arr = [1,1,2,2]
Output: 2
Explanation: Two 1s are counted cause 2 is in arr.

Constraints:
- 1 <= arr.length <= 1000
- 0 <= arr[i] <= 1000
"""

    
class SolutionNumCountDict(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(n).
        """
        from collections import defaultdict
        
        # Edge case.
        if len(arr) == 1:
            return 0
        
        # Create a dict:number->count.
        num_count_d = defaultdict(int)
        for num in arr:
            num_count_d[num] += 1
        
        result = 0
        for num, count in num_count_d.items():
            if num + 1 in num_count_d:
                result += count
        
        return result


def main():
    # Output: 2
    arr = [1,2,3]
    print SolutionNumCountDict().countElements(arr)

    # Output: 0
    arr = [1,1,3,3,5,5,7,7]
    print SolutionNumCountDict().countElements(arr)

    # Output: 3
    arr = [1,3,2,3,5,0]
    print SolutionNumCountDict().countElements(arr)

    # Output: 2
    arr = [1,1,2,2]
    print SolutionNumCountDict().countElements(arr)


if __name__ == '__main__':
    main()
