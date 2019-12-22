"""Leetcode 443. String Compression
Easy

URL: https://leetcode.com/problems/string-compression/

Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the
original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length
of the array.

Follow up:
Could you solve it using only O(1) extra space?
 
Example 1:
Input:
["a","a","b","b","c","c","c"]
Output:
Return 6, and the first 6 characters of the input array should be:
["a","2","b","2","c","3"]
Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".

Example 2:
Input:
["a"]
Output:
Return 1, and the first 1 characters of the input array should be: ["a"]
Explanation:
Nothing is replaced.

Example 3:
Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output:
Return 4, and the first 4 characters of the input array should be: 
["a","b","1","2"].
Explanation:
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb"
is replaced by "b12".
Notice each digit has it's own entry in the array.

Note:
- All characters have an ASCII value in [35, 126].
- 1 <= len(chars) <= 1000.
"""

class SolutionTwoPointersRepeat(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(1).
        """
        n = len(chars)
        if n <= 1:
            return n

        # Apply two pointere method: i: old index, j: new index.
        i, j = 0, 0

        while i < n:
            chars[j] = chars[i]
            repeat = 1

            # Iterate RHS of char i to check if same char.
            while i + 1 < n and chars[i + 1] == chars[i]:
                i += 1
                repeat += 1

            # If repeat > 1, replace chars by repeat.
            if repeat > 1:
                for c in str(repeat):
                    j += 1
                    chars[j] = c

            # Increment i, j to continue visiting chars.
            i += 1
            j += 1

        return j


def main():
    # Input: ["a","a","b","b","c","c","c"]
    # Output: Return 6, and the first 6 characters of the input array should be:
    # ["a","2","b","2","c","3"]
    chars = ["a","a","b","b","c","c","c"]
    length = SolutionTwoPointersRepeat().compress(chars)
    print length, chars[:length]

    # Input: ["a"]
    # Output: Return 1, and the first 1 characters of the input array should be:
    # ["a"]
    chars = ["a"]
    length = SolutionTwoPointersRepeat().compress(chars)
    print length, chars[:length]

    # Input: ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    # Output: Return 4, and the first 4 characters of the input array should be: 
    # ["a","b","1","2"].
    chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    length = SolutionTwoPointersRepeat().compress(chars)
    print length, chars[:length]


if __name__ == '__main__':
    main()
