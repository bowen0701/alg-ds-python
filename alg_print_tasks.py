from __future__ import print_function
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
			new_task.get_pages() / (pages_per_minute / 60))


class Task(object):
	def __init__(self, time):
		self.timestamp = time
		self.pages = np.random.random_integers(1, 20) 

	def get_stamp(self):
		return self.timestamp

	def get_pages(self):
		return self.pages

	def wait_time(self, current_time):
		return current_time - self.timestamp


def simulate_print_tasks(num_seconds, pages_per_minute):
	printer = Printer(pages_per_minute)
	print_queueu = Queue()

	waiting_times = []

	for current_second in xrange(num_seconds):
		pass


def create_print_task():
	pass


def main():
	pass


if __name__ == '__main__':
	main()
