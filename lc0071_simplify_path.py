"""Leetcode 71. Simplify Path
Medium

URL: https://leetcode.com/problems/simplify-path/

Given an absolute path for a file (Unix-style), simplify it. Or in other words,
convert it to the canonical path.

In a UNIX-style file system, a period . refers to the current directory.
Furthermore, a double period .. moves the directory up a level.
For more information, see: Absolute path vs relative path in Linux/Unix

Note that the returned canonical path must always begin with a slash /,
and there must be only a single slash / between two directory names.
The last directory name (if it exists) must not end with a trailing /.
Also, the canonical path must be the shortest string representing the absolute path.

Example 1:
Input: "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.

Example 2:
Input: "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, 
as the root level is the highest level you can go.

Example 3:
Input: "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by
a single one.

Example 4:
Input: "/a/./b/../../c/"
Output: "/c"

Example 5:
Input: "/a/../../b/../c//.//"
Output: "/c"

Example 6:
Input: "/a//b////c/d//././/.."
Output: "/a/b/c"
"""

class SolutionCurrentStack(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str

        Time complexity: O(n), where n is the length of path.
        Space complexity: O(n).
        """
        # Split path by '/', and remove empty strings.
        split_path = path.split('/')

        # Create stack to mimic dir hierarchy.
        stack = []

        # Iterate through split path to change dir.
        for i in range(len(split_path)):
            if split_path[i] == '' or split_path[i] == '.':
                continue
            elif split_path[i] == '..':
                if not stack:
                    current = ''
                else:
                    current = stack.pop()
            else:
                stack.append(split_path[i])

        return '/' + '/'.join(stack)


def main():
    # Output: "/home/foo"
    path = "/home//foo/"
    print SolutionCurrentStack().simplifyPath(path)

    # Output: "/c"
    path = "/a/./b/../../c/"
    print SolutionCurrentStack().simplifyPath(path)

    # Output: "/c"
    path = "/a/../../b/../c//.//"
    print SolutionCurrentStack().simplifyPath(path)

    # Output: "/a/b/c"
    path = "/a//b////c/d//././/.."
    print SolutionCurrentStack().simplifyPath(path)


if __name__ == '__main__':
    main()
