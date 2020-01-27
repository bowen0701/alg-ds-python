"""Leetcode 158. Read N Characters Given Read4 II - Call multiple times (Premium)
Hard

URL: https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/

Given a file and assume that you can only read the file using a given method read4,
implement a method read to read n characters. Your method read may be called
multiple times.

Method read4:

The API read4 reads 4 consecutive characters from the file, then writes those
characters into the buffer array buf.

The return value is the number of actual characters read.

Note that read4() has its own file pointer, much like FILE *fp in C.

Definition of read4:

    Parameter:  char[] buf
    Returns:    int

Note: buf[] is destination not source, the results from read4 will be copied to
buf[].
Below is a high level example of how read4 works:

File file("abcdefghijk"); // File is "abcdefghijk", initially file pointer (fp) points to 'a'
char[] buf = new char[4]; // Create buffer with enough space to store characters
read4(buf); // read4 returns 4. Now buf = "abcd", fp points to 'e'
read4(buf); // read4 returns 4. Now buf = "efgh", fp points to 'i'
read4(buf); // read4 returns 3. Now buf = "ijk", fp points to end of file

Method read:

By using the read4 method, implement the method read that reads n characters from
the file and store it in the buffer array buf. Consider that you cannot manipulate
the file directly.

The return value is the number of actual characters read.

Definition of read:

    Parameters: char[] buf, int n
    Returns:    int

Note: buf[] is destination not source, you will need to write the results to buf[].

Example 1:
File file("abc");
Solution sol;
// Assume buf is allocated and guaranteed to have enough space for storing all
characters from the file.
sol.read(buf, 1); // After calling your read method, buf should contain "a". We
read a total of 1 character from the file, so return 1.
sol.read(buf, 2); // Now buf should contain "bc". We read a total of 2 characters
from the file, so return 2.
sol.read(buf, 1); // We have reached the end of file, no more characters can be
read. So return 0.

Example 2:
File file("abc");
Solution sol;
sol.read(buf, 4); // After calling your read method, buf should contain "abc". We
read a total of 3 characters from the file, so return 3.
sol.read(buf, 1); // We have reached the end of file, no more characters can be
read. So return 0.

Note:
- Consider that you cannot manipulate the file directly, the file is only accesible
  for read4 but not for read.
- The read function may be called multiple times.
- Please remember to RESET your class variables declared in Solution, as static/
  class variables are persisted across multiple test cases. Please see here for
  more details.
- You may assume the destination buffer array, buf, is guaranteed to have enough
  space for storing n characters.
- It is guaranteed that in a given test case the same buffer buf is called by read.
"""

class SolutionPreviousSizeIdxBuffer(object):
    def __init__(self):
        self.prev_size = 0
        self.prev_idx = 0
        self.prev_buf = [''] * 4

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)

        Time complexity: O(n).
        Space complexity: O(1).
        """
        # Use read counter to increment reading n chars from previous buffer.
        read_counter = 0

        while read_counter < n:
            # If previous buffer index is still in previous buffer, 
            # read char from previous buffer, increment read counter & buffer index.
            if self.prev_idx < self.prev_size:
                buf[read_counter] = self.prev_buf[self.prev_idx]

                self.prev_idx += 1
                read_counter += 1
            else:
                # If previous buffer index is out of boundary of previous buffer,
                # read new chars by read4, store in previous buffer & reset previous index.
                self.prev_size = read4(self.prev_buf)
                self.prev_idx = 0

                # If read4's reading receives no more chars, break.
                if self.prev_size == 0:
                    break

        return read_counter


def main():
    pass


if __name__ == '__main__':
    main()
