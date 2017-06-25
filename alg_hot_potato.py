from __future__ import print_function
from ds_queue import Queue

def pass_hot_potato(name_ls, num):
	name_queue = Queue()

	for name in name_ls:
		name_queue.enqueue(name)

	while name_queue.size() > 1:
		for i in xrange(num):
			name_queue.enqueue(name_queue.dequeue())

		name_queue.dequeue()

	return name_queue.dequeue()


def main():
	name_ls = ['Bowen', 'Bowen1', 'Bowen2']
	num = 5
	print(name_ls)
	print('num: {}'.format(num))
	print(pass_hot_potato(name_ls, num))


if __name__ == '__main__':
	main()
