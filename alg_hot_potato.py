from __future__ import print_function
from ds_queue import Queue

def pass_hot_potato(names, num):
	"""Pass hot potato.

	A hot potato is sequentially passed to ones in a queue line.
	After a number of passes, the one who got the hot potato is out.
	Then the passing hot potato game is launched againg,
	until the last person is remaining one.
	"""
	name_queue = Queue()

	for name in names:
		name_queue.enqueue(name)

	while name_queue.size() > 1:
		for i in xrange(num):
			name_queue.enqueue(name_queue.dequeue())

		name_queue.dequeue()

	return name_queue.dequeue()


def main():
	names = ['Bowen', 'Bowen1', 'Bowen2']
	num = 5
	print(names)
	print('num: {}'.format(num))
	print(pass_hot_potato(names, num))


if __name__ == '__main__':
	main()
