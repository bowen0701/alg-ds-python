"""Leetcode 733. Flood Fill
Easy

URL: https://leetcode.com/problems/flood-fill/

An image is represented by a 2-D array of integers, each integer representing
the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of
the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected
4-directionally to the starting pixel of the same color as the starting pixel,
plus any pixels connected 4-directionally to those pixels
(also with the same color as the starting pixel), and so on.
Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.

Note:
- The length of image and image[0] will be in the range [1, 50].
- The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
- The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
"""

class SolutionDFS(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        # Check starting color and new color.
        if image[sr][sc] == newColor:
            return image

        n_rows, n_cols = len(image), len(image[0])

        # Apply DFS with stack to modify image.
        old_color = image[sr][sc]

        stack = [(sr, sc)]

        while stack:
            r, c = stack.pop()
            image[r][c] = newColor

            # Make 4 directions: up, down, left, right.
            dirs = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]

            for r_neighbor, c_neighbor in dirs:
                # If visit is out of boundary or does not match old color.
                if (r_neighbor < 0 or r_neighbor >= n_rows or
                    c_neighbor < 0 or c_neighbor >= n_cols or
                    image[r_neighbor][c_neighbor] != old_color):
                    continue

                image[r_neighbor][c_neighbor] = newColor
                stack.append((r_neighbor, c_neighbor))

        return image


def main():
    # Output: [[2,2,2],[2,2,0],[2,0,1]]
    image = [[1,1,1],
             [1,1,0],
             [1,0,1]]
    sr, sc = 1, 1
    newColor = 2
    print SolutionDFS().floodFill(image, sr, sc, newColor)

    # Output: [[0,0,0],[0,1,1]]
    image = [[0,0,0],
             [0,1,1]]
    sr, sc = 1, 1
    newColor = 1
    print SolutionDFS().floodFill(image, sr, sc, newColor)


if __name__ == '__main__':
    main()
