from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


class DocumentDistance():
	"""Document Distance Algorithm.

	Procedure:
	- Step 1: Split doc into words; 
	  non-alphanumeric characters are treated as blanks, and case is not significant.
    - Step 2: Compute word frequencies.
    - Step 3: Compute cosine similarity: inner_product(d1, d1) / (|d1| * |d2|)
	"""
	def __init__(self, filename1, filename2):
		self._filename1 = filename1
		self._filename2 = filename2

	pass


def main():
	pass


if __name__ == '__main__':
	main()
