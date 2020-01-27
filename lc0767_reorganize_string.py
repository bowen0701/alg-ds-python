"""Leetcode 767. Reorganize String
Medium

URL: https://leetcode.com/problems/reorganize-string/

Given a string S, check if the letters can be rearranged so that two characters
that are adjacent to each other are not the same.

If possible, output any possible result. If not possible, return the empty string.

Example 1:
Input: S = "aab"
Output: "aba"

Example 2:
Input: S = "aaab"
Output: ""

Note:
S will consist of lowercase letters and have length in range [1, 500].
"""

class SolutionCharCountMaxHeap(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str

        Time complexity: O(n*log26) = O(n).
        Space complexity: O(1).
        """
        from collections import defaultdict
        import heapq

        # Create char counts in S.
        char_count_d = defaultdict(int)
        for char in S:
            char_count_d[char] += 1

        # To get the most frequent char, push (count, char) into max heap.
        # Specifically, push (-count, char) into min heap.
        max_hq = []
        for char, count in char_count_d.items()
            heapq.heappush(max_hq, (-count, char))

        # Create previous char and its negative count.
        prev_neg_count = 0
        prev_char = ''
        result = ''

        while max_hq:
            neg_count, char = heapq.heappop(max_hq)
            result += char

            # If there remains previous char, push back to max heap.
            if prev_neg_count < 0:
                heapq.heappush(max_hq, (prev_neg_count, prev_char))

            # Update previous char and its negative count by neg_count + 1.
            prev_neg_count = neg_count + 1
            prev_char = char

        if len(result) != len(S):
            return ''
        else:
            return result


def main():
    # # Output: "aba"
    # S = "aab"
    # print SolutionCharCountMaxHeap().reorganizeString(S)

    # Output: ""
    S = "aaab"
    print SolutionCharCountMaxHeap().reorganizeString(S)


if __name__ == '__main__':
    main()
