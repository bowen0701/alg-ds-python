"""Leetcode 732. My Calendar III
Hard

URL: https://leetcode.com/problems/my-calendar-iii/

Implement a MyCalendarThree class to store your events. A new event can always be added.

Your class will have one method, book(int start, int end). Formally, this represents a
booking on the half open interval [start, end), the range of real numbers x such that
start <= x < end.

A K-booking happens when K events have some non-empty intersection (ie., there is some
time that is common to all K events.)

For each call to the method MyCalendar.book, return an integer K representing the
largest integer such that there exists a K-booking in the calendar.

Your class will be called like this: 
MyCalendarThree cal = new MyCalendarThree();
MyCalendarThree.book(start, end)

Example 1:
MyCalendarThree();
MyCalendarThree.book(10, 20); // returns 1
MyCalendarThree.book(50, 60); // returns 1
MyCalendarThree.book(10, 40); // returns 2
MyCalendarThree.book(5, 15); // returns 3
MyCalendarThree.book(5, 10); // returns 3
MyCalendarThree.book(25, 55); // returns 3
Explanation: 
The first two events can be booked and are disjoint, so the maximum K-booking is a 1-booking.
The third event [10, 40) intersects the first event, and the maximum K-booking is a 2-booking.
The remaining events cause the maximum K-booking to be only a 3-booking.
Note that the last event locally causes a 2-booking, but the answer is still 3 because
eg. [10, 20), [10, 40), and [5, 15) are still triple booked.

Note:
- The number of calls to MyCalendarThree.book per test case will be at most 400.
- In calls to MyCalendarThree.book(start, end), start and end are integers in the range [0, 10^9].
"""

class MyCalendarThreeTimeCounterDictSort(object):
    def __init__(self):
        from collections import defaultdict
        self.time_counter_d = defaultdict(int)

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int

        Time complexity: O(n*logn).
        Space complexity: O(n).
        """
        # Create time counter: new event starts at start, ends at end.
        self.time_counter_d[start] += 1
        self.time_counter_d[end] -= 1

        # Update max k-events by iterating through sorted events by times.
        sorted_time_counters = sorted(self.time_counter_d.items())

        max_k_events = 0
        cur_k_events = 0

        for time, counter in sorted_time_counters:
            cur_k_events += counter
            max_k_events = max(max_k_events, cur_k_events)

        return max_k_events


class MyCalendarThreeTimeCountersListBisectInsort(object):
    def __init__(self):
        self.time_counters = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(n).
        """
        from bisect import insort

        # Create sorted events with diffs by times.
        insort(self.time_counters, (start, 1))
        insort(self.time_counters, (end, -1))

        # Update max k-events by iterating through sorted events.
        max_k_events = 0
        cur_k_events = 0

        for time, counter in self.time_counters:
            cur_k_events += counter
            max_k_events = max(max_k_events, cur_k_events)

        return max_k_events


def main():
    # MyCalendarThree.book(10, 20); // returns 1
    # MyCalendarThree.book(50, 60); // returns 1
    # MyCalendarThree.book(10, 40); // returns 2
    # MyCalendarThree.book(5, 15); // returns 3
    # MyCalendarThree.book(5, 10); // returns 3
    # MyCalendarThree.book(25, 55); // returns 3
    calendar = MyCalendarThreeTimeCounterDictSort()
    print calendar.book(10, 20)
    print calendar.book(50, 60)
    print calendar.book(10, 40)
    print calendar.book(5, 15)
    print calendar.book(5, 10)
    print calendar.book(25, 55)

    calendar = MyCalendarThreeTimeCountersListBisectInsort()
    print calendar.book(10, 20)
    print calendar.book(50, 60)
    print calendar.book(10, 40)
    print calendar.book(5, 15)
    print calendar.book(5, 10)
    print calendar.book(25, 55)


if __name__ == '__main__':
    main()
