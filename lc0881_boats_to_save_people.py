"""Leetcode 881. Boats to Save People
Medium

URL: https://leetcode.com/problems/boats-to-save-people/

The i-th person has weight people[i], and each boat can carry a maximum weight
of limit.

Each boat carries at most 2 people at the same time, provided the sum of the
weight of those people is at most limit.

Return the minimum number of boats to carry every given person.
(It is guaranteed each person can be carried by a boat.)

Example 1:
Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)

Example 2:
Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)

Example 3:
Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)

Note:
- 1 <= people.length <= 50000
- 1 <= people[i] <= limit <= 30000
"""

class SolutionTwoPointers(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int

        Time complexity: O(n*logn), where n is the number of people.
        Space complexity: O(1).
        """
        # Sort people first.
        people.sort()

        # Apply two pointers method: the lightest & heaviest people.
        i, j = 0, len(people) - 1

        n_boats = 0

        while i <= j:
            if people[i] + people[j] <= limit:
                # Both people can be in the boat.
                i += 1
                j -= 1
            else:
                # Put heaviest person in the boat, lightest goes to another.
                j -= 1

            n_boats += 1

        return n_boats


def main():
    # Output: 1
    people = [1,2]
    limit = 3
    print SolutionTwoPointers().numRescueBoats(people, limit)

    # Output: 3
    people = [3,2,2,1]
    limit = 3
    print SolutionTwoPointers().numRescueBoats(people, limit)

    # Output: 4
    people = [3,5,3,4]
    limit = 5
    print SolutionTwoPointers().numRescueBoats(people, limit)


if __name__ == '__main__':
    main()
