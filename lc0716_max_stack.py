"""Leetcode 716.Max Stack (Premium)
Easy

URL: https://leetcode.com/problems/max-stack

Design a max stack that supports push, pop, top, peekMax and popMax.
1. push(x) -- Push element x onto stack.
2. pop() -- Remove the element on top of the stack and return it.
3. top() -- Get the element on the top.
4. peekMax() -- Retrieve the maximum element in the stack.
5. popMax() -- Retrieve the maximum element in the stack, and remove it.

If you find more than one maximum elements, only remove the top-most one.

Example 1:
MaxStack stack = new MaxStack();
stack.push(5); 
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5

Note:
- -1e7 <= x <= 1e7
- Number of operations won't exceed 10000.
- The last four operations won't be called when stack is empty.
"""

class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None

        Time complexity: O(1).
        Space complexity: O(n).
        """
        if not self._stack:
            self._stack.append((x, x))
        else:
            maximum = max(self._stack[-1][1], x)
            self._stack.append((x, maximum))

    def pop(self):
        """
        :rtype: None

        Time complexity: O(1).
        Space complexity: O(n).
        """
        return self._stack.pop()[0]

    def top(self):
        """
        :rtype: int

        Time complexity: O(1).
        Space complexity: O(n).
        """
        if not self._stack:
            return None

        return self._stack[-1][0]


    def peekMax(self):
        """
        :rtype: int

        Time complexity: O(1).
        Space complexity: O(n).
        """
        if not self._stack:
            return None
        
        return self._stack[-1][1]

    def popMax(self):
        """
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(n).
        """
        if not self._stack:
            return None

        # Pop until found current max, then push back the others.
        maximum = self._stack[-1][1]

        stack = []
        while self._stack[-1][0] != maximum:
            stack.append(self._stack.pop()[0])

        self._stack.pop()

        while stack:
            self.push(stack.pop())

        return maximum


def main():
    min_stack = MinStack()
    min_stack.push(5)
    min_stack.push(1)
    min_stack.push(5)

    # Output: 5
    print min_stack.top()
    # Output: 5
    print min_stack.popMax()
    # Output: 1
    print min_stack.top()
    # Output: 5
    print min_stack.peekMax()
    # Output: 1
    print min_stack.pop()
    # Output: 5
    print min_stack.top()


if __name__ == '__main__':
    main()
