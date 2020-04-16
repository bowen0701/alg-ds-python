"""Leetcode: Perform String Shifts

URL: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3299/

You are given a string s containing lowercase English letters, and a matrix
shift, where shift[i] = [direction, amount]:
- direction can be 0 (for left shift) or 1 (for right shift). 
- amount is the amount by which string s is to be shifted.
- A left shift by 1 means remove the first character of s and append it to
  the end.
- Similarly, a right shift by 1 means remove the last character of s and
  add it to the beginning.
Return the final string after all operations.

Example 1:
Input: s = "abc", shift = [[0,1],[1,2]]
Output: "cab"
Explanation: 
[0,1] means shift to left by 1. "abc" -> "bca"
[1,2] means shift to right by 2. "bca" -> "cab"

Example 2:
Input: s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
Output: "efgabcd"
Explanation:  
[1,1] means shift to right by 1. "abcdefg" -> "gabcdef"
[1,1] means shift to right by 1. "gabcdef" -> "fgabcde"
[0,2] means shift to left by 2. "fgabcde" -> "abcdefg"
[1,3] means shift to right by 3. "abcdefg" -> "efgabcd"
 
Constraints:
- 1 <= s.length <= 100
- s only contains lower case English letters.
- 1 <= shift.length <= 100
- shift[i].length == 2
- 0 <= shift[i][0] <= 1
- 0 <= shift[i][1] <= 100
"""

class SolutionAccumShiftsModeLength(object):
    def stringShift(self, s, shift):
        """
        :type s: str
        :type shift: List[List[int]]
        :rtype: str

        Time complexity: O(n).
        Space complexity: O(n).
        """
        # Edge case with one char.
        n = len(s)
        if n == 1:
            return s

        # Accumulate total shifts: left:-1, right:+1.
        n_shifts = 0
        for direct, amount in shift:
            n_shifts += (2 * direct - 1) * amount

        # Take n_shift mod s length to remove redundant shifts.
        n_shifts %= n

        # Shift string by total shifts.
        s_shifted = [None] * n
        for i in range(n):
            i_shifted = (i + n_shifts) % n
            s_shifted[i_shifted] = s[i]
        return ''.join(s_shifted)


def main():
    import time

    start_time = time.time()
    # Output: "cab"
    s = "abc"
    shift = [[0,1],[1,2]]
    print SolutionAccumShiftsModeLength().stringShift(s, shift)

    # Output: "efgabcd"
    s = "abcdefg"
    shift = [[1,1],[1,1],[0,2],[1,3]]
    print SolutionAccumShiftsModeLength().stringShift(s, shift)
    print 'Time: {}'.format(time.time() - start_time)


if __name__ == '__main__':
    main()
