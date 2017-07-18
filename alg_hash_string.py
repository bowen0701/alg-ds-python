from __future__ import print_function


def hash_str(a_str, table_size):
	"""Hash a string by the folding method.
 
    - Get ordinal number for each char.
    - Sum all of the ordinal numbers.
    - Return the remainder of the sum with table_size. 
	"""
	sum = 0
	for c in a_str:
		sum += ord(c)
	return sum % table_size


def weighted_hash_str(a_str, table_size):
	"""Weighted-Hash a string by the folding method.

    - Get ordinal number for each char.
    - Weighted-sum all of the ordinal numbers.
    - Return the remainder of the sum with table_size. 
	"""
	sum = 0
	for i, c in enumerate(a_str):
		sum += (i + 1) * ord(c)
	return sum % table_size


def main():
	a_str = 'cat'
	print('For hash_str(): {}'.format(hash_str(a_str, 11)))
	print('For weighted_hash_str(): {}'
		  .format(weighted_hash_str(a_str, 11)))


if __name__ == '__main__':
	main()
