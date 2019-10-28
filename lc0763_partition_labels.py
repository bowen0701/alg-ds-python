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
        Space complexity: O(1).
        """
        from collections import defaultdict

        partition_lens = []

        # Use dict to record last pos for each letter.
        last_poses = defaultdict(int)
        for i, c in enumerate(S):
            last_poses[c] = i

        i = 0
        while i < len(S):
            # For each letter, get its last position as the last pos for i.
            partition_last = last_poses[S[i]]

            j = i
            while j < partition_last:
                # Interate through each letter following S[i], update last position.
                # If j is out of last position, we get one partition.
                partition_last = max(partition_last, last_poses[S[j]])
                j += 1

            partition_lens.append(j - i + 1)

            # Start from the next of the previous partition end.
            i = j + 1

        return partition_lens


def main():
    S = "ababcbacadefegdehijhklij"
    print SolutionDict().partitionLabels(S)


if __name__ == '__main__':
    main()
