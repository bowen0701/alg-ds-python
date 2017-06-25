from __future__ import print_function
from __future__ import division
import numpy as np
from ds_queue import Queue


class Printer(object):
    """A printer class."""
    def __init__(self, pages_per_minute):
        self.page_rate = pages_per_minute
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task is not None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining == 0:
                self.current_task = None

    def busy(self):
        if self.current_task is not None:
            return True
        else:
            return False

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = (
            new_task.get_pages() / (self.page_rate / 60))


class Task(object):
    """Task class."""
    def __init__(self, time):
        self.timestamp = time
        self.pages = np.random.random_integers(1, 20) 

    def get_stamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.timestamp


def create_print_task():
    """Create printing task.

    A printing task is generated per 180 seconds.
    """
    num = np.random.random_integers(1, 180)
    if num == 180:
        return True
    else:
        return False


def simulate_print_tasks(num_seconds, pages_per_minute):
    """Simulate printing tasks."""
    printer = Printer(pages_per_minute)
    print_queue = Queue()

    waiting_times = []

    for current_second in xrange(num_seconds):
        if create_print_task():
            task = Task(current_second)
            print_queue.enqueue(task)

        if (not printer.busy()) and (not print_queue.is_empty()):
            next_task = print_queue.dequeue()
            waiting_times.append(
                next_task.wait_time(current_second))
            printer.start_next(next_task)

        printer.tick()

    avg_wait_seconds = sum(waiting_times) / len(waiting_times)
    print('Average wait {0:.2f} secs, {1} tasks remaining.'
          .format(avg_wait_seconds, print_queue.size()))


def main():
    num_seconds = 3600
    pages_per_minute = 5
    print('num_seconds: {0}, pages_per_minute: {1}'
          .format(num_seconds, pages_per_minute))
    for i in xrange(10):
        simulate_print_tasks(num_seconds, pages_per_minute)

    print('===')

    num_seconds = 3600
    pages_per_minute = 10
    print('num_seconds: {0}, pages_per_minute: {1}'
          .format(num_seconds, pages_per_minute))
    for i in xrange(10):
        simulate_print_tasks(num_seconds, pages_per_minute)


if __name__ == '__main__':
    main()
