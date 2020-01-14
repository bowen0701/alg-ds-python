"""Leetcode 729. My Calendar I
Medium

URL: https://leetcode.com/problems/my-calendar-i/

Implement a MyCalendar class to store your events. A new event can be added if adding
the event will not cause a double booking.

Your class will have the method, book(int start, int end). Formally, this represents a
booking on the half open interval [start, end), the range of real numbers x such that
start <= x < end.

A double booking happens when two events have some non-empty intersection (ie., there
is some time that is common to both events.)

For each call to the method MyCalendar.book, return true if the event can be added to
the calendar successfully without causing a double booking. Otherwise, return false
and do not add the event to the calendar.

Your class will be called like this: MyCalendar cal = new MyCalendar(); 
MyCalendar.book(start, end)

Example 1:
MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(15, 25); // returns false
MyCalendar.book(20, 30); // returns true
Explanation: 
The first event can be booked.  The second can't because time 15 is already booked by
another event.
The third event can be booked, as the first event takes every time less than 20,
but not including 20.
 
Note:
- The number of calls to MyCalendar.book per test case will be at most 1000.
- In calls to MyCalendar.book(start, end), start and end are integers in the range [0, 10^9].

Your MyCalendar object will be instantiated and called as such:
obj = MyCalendar()
param_1 = obj.book(start,end)
"""

class MyCalendarArray(object):
    def __init__(self):
        self.events = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool

        Time complexity: O(n).
        Space complexity: O(n).
        """
        # Iteratively check all events overlapping with [start, end].
        for event in self.events:
            if start < event[1] and end > event[0]:
                return False

        # If no overlaps, add to events.
        self.events.append([start, end])
        return True


class Node(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None


class MyCalendarBST(object):
    def __init__(self):
        self.root = None

    def _binary_search(self, start, end, node):
        if start >= node.end:
            # If new event is in RHS of node, insert new as right or search in RHS.
            if not node.right:
                node.right = Node(start, end)
                return True
            else:
                return self._binary_search(start, end, node.right)
        elif end <= node.start:
            # If new event is in LHS of node, insert new as left or search in LHS.
            if not node.left:
                node.left = Node(start, end)
                return True
            else:
                return self._binary_search(start, end, node.left)
        else:
            return False

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool

        Time complexity: O(logn).
        Space complexity: O(n).
        """
        if not self.root:
            self.root = Node(start, end)
            return True

        return self._binary_search(start, end, self.root)


def main():
    # MyCalendar.book(10, 20); // returns true
    # MyCalendar.book(15, 25); // returns false
    # MyCalendar.book(20, 30); // returns true
    calendar = MyCalendarArray()
    print calendar.book(10, 20)
    print calendar.book(15, 25)
    print calendar.book(20, 30)

    calendar = MyCalendarBST()
    print calendar.book(10, 20)
    print calendar.book(15, 25)
    print calendar.book(20, 30)



if __name__ == '__main__':
    main()
