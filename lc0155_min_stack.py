"""Leetcode 155. Min Stack
Easy

URL: https://leetcode.com/problems/min-stack/

Design a stack that supports push, pop, top, and retrieving the minimum element 
in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(x)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
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
        Space complexity: O(n), where n is the number of elements.
        """
        if not self._stack:
            # If stack is empty, insert (x, min) into the stack, where min = x.
            self._stack = [(x, x)]
        else:
            # If stack is not empty, insert (x, min) where min is updated if needed.
            minimum = min(x, self._stack[-1][1])
            self._stack.append([x, minimum])

        return None
            
    def pop(self):
        """
        :rtype: None

        Time complexity: O(1).
        Space complexity: O(n), where n is the number of elements.
        """
        if self._stack:
            return self._stack.pop()[1]
        else:
            return None

    def top(self):
        """
        :rtype: int

        Time complexity: O(1).
        Space complexity: O(n), where n is the number of elements.
        """
        if self._stack:
            return self._stack[-1][0]
        else:
            return None

    def getMin(self):
        """
        :rtype: int

        Time complexity: O(1).
        Space complexity: O(n), where n is the number of elements.
        """
        if self._stack:
            return self._stack[-1][1]
        else:
            return None


def main():
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    # Returns -3.
    print minStack.getMin()
    minStack.pop()
    # Returns 0.
    print minStack.top()
    # Returns -2.
    print minStack.getMin()


if __name__ == '__main__':
    min_stack = main()
