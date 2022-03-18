"""Leetcode 299. Bulls and Cows
Medium

URL: https://leetcode.com/problems/bulls-and-cows/

You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is. 
When your friend makes a guess, you provide a hint with the following info:

The number of "bulls", which are digits in the guess that are in the correct position.
The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. 
Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. 
Note that both secret and guess may contain duplicate digits.

Example 1:
Input: secret = "1807", guess = "7810"
Output: "1A3B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1807"
  |
"7810"

Example 2:
Input: secret = "1123", guess = "0111"
Output: "1A1B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1123"        "1123"
  |      or     |
"0111"        "0111"
Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to allow one 1 to be a bull.
 
Constraints:
- 1 <= secret.length, guess.length <= 1000
- secret.length == guess.length
- secret and guess consist of digits only.
"""

from collections import defaultdict


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        """
        Time complexity: O(n).
        Space complexity: O(n).
        """
        # Iterate through secret & guess to check char matches.
        # If match, incremet bulls counter.
        # If not, insert both chars to char_freq dict.
        n_bulls = 0
        secret_char_freq_d = defaultdict(int)
        guess_char_freq_d = defaultdict(int)

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                n_bulls += 1
            else:
                secret_char_freq_d[secret[i]] += 1
                guess_char_freq_d[guess[i]] += 1
    
        # Iterate through secret's char_freq dict to accumulate cows counter.
        n_cows = 0
        for char, freq in secret_char_freq_d.items():
            if char in guess_char_freq_d:
                n_cows += min(freq, guess_char_freq_d[char])
        
        return "".join([str(n_bulls), "A", str(n_cows), "B"])


def main():
    # Output: "1A3B"
    secret = "1807"
    guess = "7810"
    print(Solution().getHint(secret, guess))

    # Output: "1A1B"
    secret = "1123"
    guess = "0111"
    print(Solution().getHint(secret, guess))


if __name__ == "__main__":
    main()

