class MinimumEditDistance(object):
	"""Minimum Edit Distance (Levenshtein) with Backtrace.

	Given two strings, find the minimum number of operations required to 
	convert string1 to string2.

	You have the following 3 operations permitted on a word:
	- Insert a character (to string1)
	- Delete a character (of string1)
	- Substitude a character (of string1 & string2)

	Operation costs:
	- Standard: If each operation has cost of 1.
	- Levenshtein: If substitude operation has cost of 2.

	Align each character of the two string1 to each other by keeping a "backtrace".

	Example:
	Input: string1 = "intention", string2 = "execution"
	Output: 5
	inte*ntion
	*execution
	----------
	dss is
	"""
	pass


def main():
	pass


if __name__ == '__main__':
	main()
