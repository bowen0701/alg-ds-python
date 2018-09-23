from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def fizzbuzz(n):
	ls = []
	for i in range(1, n + 1):
		if i % 15 == 0:
			ls.append('fizzbuzz')
		elif i % 3 == 0:
			ls.append('fizz')
		elif i % 5 == 0:
			ls.append('buzz')
		else:
			ls.append(i)
	return ls


def main():
	n = 100
	fizzbuzz_ls = fizzbuzz(n)
	print(fizzbuzz_ls)


if __name__ == '__main__':
	main()
