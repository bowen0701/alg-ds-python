"""Leetcode 232. Implement Queue using Stacks
Easy

URL: https://leetcode.com/problems/implement-queue-using-stacks/

Implement the following operations of a queue using stacks.
- push(x) -- Push element x to the back of queue.
- pop() -- Removes the element from in front of queue.
- peek() -- Get the front element.
- empty() -- Return whether the queue is empty.

Example:
MyQueue queue = new MyQueue();
queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false

Notes:
- You must use only standard operations of a stack -- which means only push to top,
  peek/pop from top, size, and is empty operations are valid.
- Depending on your language, stack may not be supported natively. You may simulate
  a stack by using a list or deque (double-ended queue), as long as you use only
  standard operations of a stack.
- You may assume that all operations are valid (for example, no pop or peek
  operations will be called on an empty queue).
"""

class MyQueueByTwoStacks(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Create two stacks with the newest/oldest on top.
        from collections import deque

        self.stack_newest_on_top = deque([])
        self.stack_oldest_on_top = deque([])

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        # Always push to stack_newest_on_top.
        self.stack_newest_on_top.append(x)
        return None

    def _shift_stacks(self):
        """
        Shift elements from stack_newest_on_top to stack_oldest_on_top,
        if stack_oldest_on_top is empty.
        """
        if not self.stack_oldest_on_top:
            while self.stack_newest_on_top:
                self.stack_oldest_on_top.append(self.stack_newest_on_top.pop())
        return None

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self._shift_stacks()
        return self.stack_oldest_on_top.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        self._shift_stacks()
        return self.stack_oldest_on_top[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.stack_newest_on_top and not self.stack_oldest_on_top


def main():
    queue = MyQueueByTwoStacks()
    queue.push(1)
    queue.push(2)
    print queue.peek()   # returns 1
    print queue.pop()    # returns 1
    print queue.empty()  # returns False


if __name__ == '__main__':
    main()
