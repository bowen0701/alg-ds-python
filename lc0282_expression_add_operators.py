"""Leetcode 282. Expression Add Operators
Hard

URL: https://leetcode.com/problems/expression-add-operators/

Given a string that contains only digits 0-9 and a target value,
return all possibilities to add binary operators (not unary) +, -, or *
between the digits so they evaluate to the target value.

Example 1:
Input: num = "123", target = 6
Output: ["1+2+3", "1*2*3"] 

Example 2:
Input: num = "232", target = 8
Output: ["2*3+2", "2+3*2"]

Example 3:
Input: num = "105", target = 5
Output: ["1*0+5","10-5"]

Example 4:
Input: num = "00", target = 0
Output: ["0+0", "0-0", "0*0"]

Example 5:
Input: num = "3456237490", target = 9191
Output: []
"""


class SolutionBacktrack(object):
    def _backtrack(self, result, temp, pos, val, prev_val):
        if pos == len(self.num):
            if val == self.target:
                result.append(temp)
            return None

        for i in range(pos, len(self.num)):
            if i > pos and self.num[pos] == '0':
                # If current char is 0, use it as single digit. Skip latter iterations.
                break

            # Get current number string adnd current value.
            cur_num = self.num[pos:i+1]
            cur_val = int(cur_num)

            if pos == 0:
                # For starting pos = 0 with no operations before.
                self._backtrack(result, temp + cur_num, i + 1, 
                                cur_val, cur_val)
            else:
                # For latter pos > 1, perform operations with value & previous value.
                # Use operation: '+'.
                self._backtrack(result, temp + '+' + cur_num, i + 1, 
                                val + cur_val, cur_val)
                # Use operation: '-'.
                self._backtrack(result, temp + '-' + cur_num, i + 1,
                                val - cur_val, -cur_val)
                # Use operation: '*', e.g. 1+2*3 = (1+2)-2+2*3.
                self._backtrack(result, temp + '*' + cur_num, i + 1,
                                val - prev_val + prev_val * cur_val, 
                                prev_val * cur_val)

    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]

        Time complexity: O(n*4^n), where n is the length of string.
        Space complexity: O(n).
        """
        self.num = num
        self.target = target

        # Edge case.
        if not self.num:
            return []

        # Apply backtracking.
        result = []
        temp = ''
        pos = 0
        val = 0
        prev_val = 0
        self._backtrack(result, temp, pos, val, prev_val)
        return result


def main():
    # Output: ["1+2+3", "1*2*3"] 
    num = "123"
    target = 6
    print SolutionBacktrack().addOperators(num, target)

    # Output: ["2*3+2", "2+3*2"]
    num = "232"
    target = 8
    print SolutionBacktrack().addOperators(num, target)

    # Output: ["1*0+5","10-5"]
    num = "105"
    target = 5
    print SolutionBacktrack().addOperators(num, target)

    # Output: ["0+0", "0-0", "0*0"]
    num = "00"
    target = 0
    print SolutionBacktrack().addOperators(num, target)

    # Output: []
    num = "3456237490"
    target = 9191
    print SolutionBacktrack().addOperators(num, target)


if __name__ == '__main__':
    main()
