"""Leetcode 187. Repeated DNA Sequences
Medium

URL: https://leetcode.com/problems/repeated-dna-sequences/

All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T,
for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify
repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more
than once in a DNA molecule.

Example:
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC", "CCCCCAAAAA"]
"""

class SolutionDict(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # Apply dict to accumulate 10-letter sequence occurrence.

        from collections import defaultdict

        repeated_seq = []

        # Start from index 0 to accumuluate sequence occurrence count.
        seen_seq_count = defaultdict(int)

        i = 0
        while i + 10 <= len(s):
            # Take substring and accumulate occurrence count.
            seq = s[i:(i + 10)]
            seen_seq_count[seq] += 1

            if seen_seq_count[seq] == 2:
                # Check double occurrence only to prevend duplicates.
                repeated_seq.append(seq)

            # Increment i.
            i += 1

        return repeated_seq


def main():
    # Output: ["AAAAACCCCC", "CCCCCAAAAA"]
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    print SolutionDict().findRepeatedDnaSequences(s)


if __name__ == '__main__':
    main()
