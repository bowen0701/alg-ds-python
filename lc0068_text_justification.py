"""Leetcode 68. Text Justification
Hard

URL: https://leetcode.com/problems/text-justification/

Given an array of words and a width maxWidth, format the text such that each line has
exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you
can in each line. Pad extra spaces ' ' when necessary so that each line has exactly
maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number
of spaces on a line do not divide evenly between words, the empty slots on the left
will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted
between words.

Note:
- A word is defined as a character sequence consisting of non-space characters only.
- Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
- The input array words contains at least one word.

Example 1:
Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:
Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only
             one word.

Example 3:
Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
"""

class Solution(object):
    def _insertSpaceWord(self, w):
        # Append 1 space and next word to the line words.
        self.line_words.append(' ')
        self.line_words.append(w)

        self.n_words += 1
        self.n_chars += len(w)
        self.width += 1 + len(w)

    def _packSpaceWords(self):
        from math import ceil

        if self.width < self.maxWidth:
            # Get total number of spaces one line should have.
            n_spaces = self.maxWidth - self.n_chars

            if self.n_words == 1:
                # If only one word, line is left-justified.
                self.line_words.append(' ' * n_spaces)
            else:
                for j in range(len(self.line_words)):
                    if self.line_words[j] == ' ':
                        # Distribute space between remaining words as evenly as possible.
                        n_new_spaces = int(ceil(float(n_spaces) / (self.n_words - 1)))
                        
                        self.line_words[j] = ' ' * n_new_spaces

                        n_spaces -= n_new_spaces
                        self.n_words -= 1
                        self.width += n_new_spaces - 1
                        if self.width == self.maxWidth:
                            # If line is packed completely, skip remaining spaces.
                            break

    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]

        Procedure:
        - Iterate through words to append them to line.
        - If the width of line + 1 space + current word > maxWidth, 
          pack words in the line
        - Append current word to a new line.

        Time complexity: O(n).
        Space complexity: O(n).
        """
        self.maxWidth = maxWidth
        self.line_words = [words[0]]
        self.n_words, self.n_chars, self.width = 1, len(words[0]), len(words[0])
        
        result = []

        for i in range(1, len(words)):
            w = words[i]

            if self.width + 1 + len(w) <= self.maxWidth:
                # Insert 1 space and word into line.
                self._insertSpaceWord(w)
            else:
                # Pack words in line.
                self._packSpaceWords()

                line = ''.join(self.line_words)
                result.append(line)

                # Append word to a new line.
                self.line_words = [w]
                self.n_words, self.n_chars, self.width = 1, len(w), len(w)

        # For last line, line is left-justified. 
        if self.line_words:
            n_spaces = self.maxWidth - self.width
            self.line_words.append(' ' * n_spaces)
            line = ''.join(self.line_words)
            result.append(line)

        return result


def main():
    # Output:
    # [
    #    "This    is    an",
    #    "example  of text",
    #    "justification.  "
    # ]
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    print Solution().fullJustify(words, maxWidth)

    # Output:
    # [
    #   "What   must   be",
    #   "acknowledgment  ",
    #   "shall be        "
    # ]
    words = ["What","must","be","acknowledgment","shall","be"]
    maxWidth = 16
    print Solution().fullJustify(words, maxWidth)

    # Output:
    # [
    #   "Science  is  what we",
    #   "understand      well",
    #   "enough to explain to",
    #   "a  computer.  Art is",
    #   "everything  else  we",
    #   "do                  "
    # ]
    words = ["Science","is","what","we","understand","well","enough","to","explain",
             "to","a","computer.","Art","is","everything","else","we","do"]
    maxWidth = 20
    print Solution().fullJustify(words, maxWidth)

    # Output: 
    # [
    #   "The     important",
    #   "thing  is  not to",
    #   "stop questioning.",
    #   "Curiosity has its",
    #   "own   reason  for",
    #   "existing.        "
    # ]
    words = ["The","important","thing","is","not","to","stop","questioning.","Curiosity","has","its","own","reason","for","existing."]
    maxWidth = 17
    print Solution().fullJustify(words, maxWidth)

    # Output:
    # [
    #   "Give  me  my  Romeo; and,",
    #   "when  he  shall die, Take",
    #   "him  and  cut  him out in",
    #   "little stars, And he will",
    #   "make  the  face of heaven",
    #   "so   fine  That  all  the",
    #   "world  will  be  in  love",
    #   "with  night  And  pay  no",
    #   "worship   to  the  garish",
    #   "sun.                     "
    #  ]
    words = ["Give","me","my","Romeo;","and,","when","he","shall","die,","Take","him","and","cut","him","out","in","little","stars,","And","he","will","make","the","face","of","heaven","so","fine","That","all","the","world","will","be","in","love","with","night","And","pay","no","worship","to","the","garish","sun."]
    maxWidth = 25
    print Solution().fullJustify(words, maxWidth)


if __name__ == '__main__':
    main()
