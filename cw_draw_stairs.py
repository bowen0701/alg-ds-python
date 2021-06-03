"""Codewars: Draw stairs
8 kyu

URL: https://www.codewars.com/kata/draw-stairs/

Given a number n, draw stairs using the letter "I", n tall and n wide,
with the tallest in the top left.

For example n = 3 result in "I\n I\n I", or printed:
I
 I
  I

Another example, a 7-step stairs should be drawn like this:
I
 I
  I
   I
    I
     I
      I
"""

def draw_stairs(n):
    """
    Time complexity: O(n^2).
    Space complexity: O(n).
    """
    stairs = []
    
    for i in range(n):
        # Append (i - 1) spaces.
        stairs.append(' ' * i)
        
        # Append stair I.
        stairs.append('I')
        
        # Append change line if not the last line.
        if i != n - 1:
            stairs.append('\n')
    
    return ''.join(stairs)


def main():
    # Output: "I\n I\n I" 
    n = 3
    print draw_stairs(n)

    # Output: "I\n I\n I\n   I\n    I\n     I\n      I\n       I" 
    n = 7
    print draw_stairs(n)


if __name__ == '__main__':
    main()
