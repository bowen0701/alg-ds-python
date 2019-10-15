"""Leetcode 225. Implement Stack using Queues
Easy

URL: https://leetcode.com/problems/implement-stack-using-queues/

Implement the following operations of a stack using queues.
- push(x) -- Push element x onto stack.
- pop() -- Removes the element on top of the stack.
- top() -- Get the top element.
- empty() -- Return whether the stack is empty.

Example:
MyStack stack = new MyStack();
stack.push(1);
stack.push(2);  
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false

Notes:
- You must use only standard operations of a queue -- which means only 
  push to back, peek/pop from front, size, and is empty operations are valid.
- Depending on your language, queue may not be supported natively. You may simulate
  a queue by using a list or deque (double-ended queue), as long as you use only
  standard operations of a queue.
- You may assume that all operations are valid (for example, no pop or top
  operations will be called on an empty stack).
"""

class MyStackByTwoQueues(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Create two queues with old/new halves.
        from collections import deque

        self.queue_new = deque([])
        self.queue_old = deque([])

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        # Always push to queue_new's back.
        self.queue_new.appendleft(x)

    def _shift_new_to_old_queues(self):
        # If #queue_new > 1, shift from queue_new to queue_old until #queue_new = 1.
        while len(self.queue_new) > 1:
            self.queue_old.appendleft(self.queue_new.pop())

    def _shift_old_to_new_queues(self):
        # Shift the whole queue_old to queue_new.
        while self.queue_old:
            self.queue_new.appendleft(self.queue_old.pop())

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        self._shift_new_to_old_queues()
        popped_element = self.queue_new.pop()
        self._shift_old_to_new_queues()
        return popped_element

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        self._shift_new_to_old_queues()
        top_element = self.queue_new[-1]
        return top_element

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self.queue_new and not self.queue_old


def main():
    stack = MyStackByTwoQueues()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print 'top:', stack.top()   # returns 3
    print 'pop:', stack.pop()   # returns 3
    stack.push(4)
    print 'pop:', stack.pop()   # return 4
    print stack.empty()         # returns False


if __name__ == '__main__':
    main()
