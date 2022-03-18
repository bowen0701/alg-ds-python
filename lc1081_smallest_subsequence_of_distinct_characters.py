"""1081. Smallest Subsequence of Distinct Characters
Medium

URL: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

Given a string s, return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.

Example 1:
Input: s = "bcabc"
Output: "abc"

Example 2:
Input: s = "cbacdcbc"
Output: "acdb"
 
Constraints:
- 1 <= s.length <= 1000
- s consists of lowercase English letters.

Note: This question is the same as 316: https://leetcode.com/problems/remove-duplicate-letters/
"""

from collections import defaultdict


class LetterCounterDictLetterVisitedDictSolution:
    def smallestSubsequence(self, s: str) -> str:
        """
        Time complexity: O(n).
        Space complexity: O(1).
        """
        letter_counter_d = defaultdict(int)
        letter_visited_d = defaultdict(bool)
        
        # Iterate through s to get letter counters.
        for c in s:
            letter_counter_d[c] += 1
        
        # Iterate through s to accumulate the letters in stack.
        # If visiting letter is smaller than stack back, 
        # pop stack if there are more letters later.
        stack = []

        for c in s:
            letter_counter_d[c] -= 1
    
            if letter_visited_d[c]:
                continue
                
            while stack and c < stack[-1] and letter_counter_d[stack[-1]] > 0:
                letter_visited_d[stack[-1]] = False
                stack.pop()
            
            stack.append(c)
            letter_visited_d[c] = True
        
        return "".join(stack)


def main():
    # Output: "abc"
    s = "bcabc"
    print(LetterCounterDictLetterVisitedDictSolution().smallestSubsequence(s))

    # Output: "acdb"
    s = "cbacdcbc"
    print(LetterCounterDictLetterVisitedDictSolution().smallestSubsequence(s))


if __name__ == "__main__":
    main()
