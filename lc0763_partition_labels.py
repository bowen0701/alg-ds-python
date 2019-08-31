"""Leetcode 763. Partition Labels
Medium

URL: https://leetcode.com/problems/partition-labels/submissions/

A string S of lowercase letters is given. We want to partition this string into
as many parts as possible so that each letter appears in at most one part,
and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect,
because it splits S into less parts.

Note:
- S will have length in range [1, 500].
- S will consist of lowercase letters ('a' to 'z') only.
"""

class SolutionDict(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]

        Time complexity: O(n).
        Space complexity: O(n).
        """
        from collections import defaultdict

        partition_lens = []

        # Use dict to record last index.
        last_idx = defaultdict(int)

        for i, c in enumerate(S):
            last_idx[c] = i

        # Iterate from index 0 to check end indeces and partion.
        i = 0
        while i < len(S):
            end_idx = last_idx[S[i]]

            # Start from index i to update their end indeces.
            j = i
            while j < end_idx:
                end_idx = max(end_idx, last_idx[S[j]])
                j += 1

            partition_lens.append(j - i + 1)
            i = j + 1

        return partition_lens


def main():
    S = "ababcbacadefegdehijhklij"
    print SolutionDict().partitionLabels(S)


if __name__ == '__main__':
    main()
