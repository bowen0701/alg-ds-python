from __future__ import print_function
import numpy as np
from ds_queue import Queue


class Printer(object):
	def __init__(self, pages_per_minute):
		pass

	def tick(self):
		pass

	def busy(self):
		pass

	def start_next(self, new_task):
		pass


class Task(object):
	def __init__(self, time):
		pass

	def get_stamp(self):
		pass

	def get_pages(self):
		pass

	def wait_time(self, current_time):
		pass


def simulate_print_tasks(num_seconds, pages_per_minute):
	pass


def create_print_task():
	pass


def main():
	pass


if __name__ == '__main__':
	main()
