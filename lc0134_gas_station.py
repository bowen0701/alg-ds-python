"""Leetcode 134. Gas Station
Medium

URL: https://leetcode.com/problems/gas-station/

There are N gas stations along a circular route,
where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and
it costs cost[i] of gas to travel from station i to its next station (i+1).
You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index
if you can travel around the circuit once in the clockwise direction,
otherwise return -1.

Note:
- If there exists a solution, it is guaranteed to be unique.
- Both input arrays are non-empty and have the same length.
- Each element in the input arrays is a non-negative integer.

Example 1:
Input: 
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.

Example 2:
Input: 
gas  = [2,3,4]
cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
"""

class SolutionNaiveIter(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int

        Time complexity: O(n^2).
        Space complexity: O(1).
        """
        n = len(gas)

        for i in range(n):
            is_travel = True
            visits = list(range(i, n)) + list(range(i)) + [i]

            # Memoize tank with initialized value = 0.
            tank = 0
            for j in range(len(visits)):
                if j == 0:
                    # First station with adding gas only.
                    tank += gas[visits[0]]
                else:
                    # For travel to station j, check tank with station j - 1.
                    if tank >= cost[visits[j - 1]]:
                        tank = tank - cost[visits[j - 1]] + gas[visits[j]]
                    else:
                        is_travel = False
                        break

            if is_travel and visits[j] == i:
                # If still travel and visit i again.
                return i
            else:
                # If not, start from next i.
                continue
        
        return -1


class SolutionIter(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(1).
        """
        if sum(gas) < sum(cost):
            # If we don't have more fuel than costed in total.
            return -1

        position = 0
        current_bank = 0

        for i in range(len(gas)):
            # For each station, check current bank.
            current_bank += gas[i] - cost[i]

            if current_bank < 0:
                # If we don't have more gas, the current station is not a start.
                current_bank = 0
                position = i + 1
            else:
                # If we have more gas, then the current station is a start.
                # No need for re-run the loop again.
                continue

        return position


def main():
    # Ans: 3
    gas  = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    print SolutionNaiveIter().canCompleteCircuit(gas, cost)
    print SolutionIter().canCompleteCircuit(gas, cost)

    # Ans: -1
    gas  = [2,3,4]
    cost = [3,4,3]
    print SolutionNaiveIter().canCompleteCircuit(gas, cost)
    print SolutionIter().canCompleteCircuit(gas, cost)


if __name__ == '__main__':
    main()
