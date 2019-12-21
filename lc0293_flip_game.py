"""Leetcode 293. Flip Game (Premium)
Easy

URL: https://leetcode.com/problems/flip-game

You are playing the following Flip Game with your friend: Given a string that
contains only these two characters: + and -, you and your friend take turns to
flip two consecutive "++" into "--". The game ends when a person can no longer
make a move and therefore the other person will be the winner.

Write a function to compute all possible states of the string after one valid
move.

Example:
Input: s = "++++"
Output: 
[
  "--++",
  "+--+",
  "++--"
]
Note: If there is no valid move, return an empty list [].
"""

class SolutionIter(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # Edge cases.
        if len(s) <= 1:
            return []

        n_minus_1 = len(s) - 1
        possible_states = []

        # Iterate through string to check if char and its next are '++'.
        i = 0
        while i < n_minus_1:
            if s[i] == '+':
                while i < n_minus_1 and s[i + 1] == '+':
                    possible_states.append(s[:i] + '--' + s[i+2:])
                    i += 1

            i += 1

        return possible_states


def main():
    # Input: s = "++++"
    # Output: 
    # [
    #   "--++",
    #   "+--+",
    #   "++--"
    # ]
    s = '++++'
    print SolutionIter().generatePossibleNextMoves(s)


if __name__ == '__main__':
    main()
