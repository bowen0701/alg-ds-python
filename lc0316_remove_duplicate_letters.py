"""Leetcode 316. Remove Duplicate Letters
Medium

URL: https://leetcode.com/problems/remove-duplicate-letters/

Given a string s, remove duplicate letters so that every letter appears once and only once. 
You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:
Input: s = "bcabc"
Output: "abc"

Example 2:
Input: s = "cbacdcbc"
Output: "acdb"
 
Constraints:
- 1 <= s.length <= 104
- s consists of lowercase English letters.

Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
"""

from collections import defaultdict


class LetterCounterDictLetterVisitedDictSolution:
    def removeDuplicateLetters(self, s: str) -> str:
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
    print(LetterCounterDictLetterVisitedDictSolution().removeDuplicateLetters(s))

    # Output: "acdb"
    s = "cbacdcbc"
    print(LetterCounterDictLetterVisitedDictSolution().removeDuplicateLetters(s))


if __name__ == "__main__":
    main()
