"""Leetcode 771. Jewels and Stones
Easy

URL: https://leetcode.com/problems/jewels-and-stones/

You're given strings J representing the types of stones that are jewels,
and S representing the stones you have.
Each character in S is a type of stone you have.
You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters.
Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:
Input: J = "aA", S = "aAAbbbb"
Output: 3

Example 2:
Input: J = "z", S = "ZZ"
Output: 0

Note:
- S and J will consist of letters and have length at most 50.
- The characters in J are distinct.
"""

class SolutionSet(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int

        Time complexity: O(max(|J|, |S|)), where
          - |J|: lenght of J,
          - |S|: lenght of S.
        Space complexity: o(|J|).
        """
        # Use set to collect jewels for fast lookup.
        jewels = set(J)

        # Iterate over S to check if it's jewel.
        count = 0
        for s in S:
            if s in jewels:
                count += 1
        return count


def main():
    # Output: 3
    J = "aA"
    S = "aAAbbbb"
    print SolutionSet().numJewelsInStones(J, S)

    # Output: 0
    J = "z"
    S = "ZZ"
    print SolutionSet().numJewelsInStones(J, S)


if __name__ == '__main__':
    main()
