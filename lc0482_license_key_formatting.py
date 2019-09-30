"""Leecode 482. License Key Formatting
Easy

URL: https://leetcode.com/problems/license-key-formatting/

You are given a license key represented as a string S which consists only
alphanumeric character and dashes. The string is separated into N+1 groups
by N dashes.

Given a number K, we would want to reformat the strings such that each group
contains exactly K characters, except for the first group which could be
shorter than K, but still must contain at least one character. Furthermore,
there must be a dash inserted between two groups and all lowercase letters
should be converted to uppercase.

Given a non-empty string S and a number K, format the string according to the
rules described above.

Example 1:
Input: S = "5F3Z-2e-9-w", K = 4
Output: "5F3Z-2E9W"
Explanation: The string S has been split into two parts, each part has 4
characters.
Note that the two extra dashes are not needed and can be removed.

Example 2:
Input: S = "2-5g-3-J", K = 2
Output: "2-5G-3J"
Explanation: The string S has been split into three parts, each part has 2
characters except the first part as it could be shorter as mentioned above.

Note:
- The length of string S will not exceed 12,000, and K is a positive integer.
- String S consists only of alphanumerical characters (a-z and/or A-Z and/or 0-9)
  and dashes(-).
- String S is non-empty.
"""

class SolutionReverseIter(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str

        Time complexity: O(n).
        Space complexity: O(|S|/K).
        """
        # Upper case and drop dash.
        S_nodashes = S.upper().replace('-','')
        size_nodashes = len(S_nodashes)

        # Reversely iterate through no-dashed list, concat to string until K chars.
        res_ls = [''] * (size_nodashes // K + (size_nodashes % K > 0))

        cur_idx = len(res_ls) - 1
        cur_counter = 0

        for i in range(size_nodashes - 1, -1, -1):
            if cur_counter < K:
                res_ls[cur_idx] = S_nodashes[i] + res_ls[cur_idx]
                cur_counter += 1
            else:
                cur_idx -= 1
                res_ls[cur_idx] = S_nodashes[i] + res_ls[cur_idx]
                cur_counter = 1

        return '-'.join(res_ls)


class SolutionForwardIterK(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str

        Time complexity: O(n).
        Space complexity: O(|S|/K).
        """
        # Upper case and drop dash.
        S_nodashes = S.upper().replace('-', '')
        size_nodashes = len(S_nodashes)

        # Get the end index for the 1st part.
        remainder = size_nodashes % K
        if remainder:
            end_idx = remainder
        else:
            end_idx = K

        # Get the 1st part.
        res_ls = [S_nodashes[:end_idx]]

        # Iteratively append K chars at a time.
        while end_idx < size_nodashes:
            res_ls.append(S_nodashes[end_idx:end_idx+K])
            end_idx += K

        return '-'.join(res_ls)


def main():
    # Output: "5F3Z-2E9W"
    S = "5F3Z-2e-9-w"
    K = 4
    print SolutionReverseIter().licenseKeyFormatting(S, K)
    print SolutionForwardIterK().licenseKeyFormatting(S, K)

    # Output: "5F3Z-2E9W"
    S = "2-5g-3-J"
    K = 2
    print SolutionReverseIter().licenseKeyFormatting(S, K)
    print SolutionForwardIterK().licenseKeyFormatting(S, K)


if __name__ == '__main__':
    main()
