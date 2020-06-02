class MinimumEditDistance(object):
	"""Minimum Edit Distance (Levenshtein) with Backtrace.

	Given two strings, find the minimum number of operations required to 
	convert string1 to string2.

	We have the following 3 operations permitted on a word:
	- Insert a character (to string1)
	- Delete a character (of string1)
	- Substitude a character (of string1 & string2)

	Operation costs:
	- Standard: If each operation has cost of 1.
	- Levenshtein: If substitude operation has cost of 2.

	Align each character of the two string1 to each other by keeping a "backtrace".

	Example:
	Input: str1 = "intention", str2 = "execution"
	Output:
	- Standard distance: 5
	- Levenshtein distance: 8
	i n t e * n t i o n
	| | | | | | | | | |
	* e x e c u t i o n
	--------------------
	d s s   i s
	"""
	def __init__(self, distance_type="Levenshtein"):
		if distance_type not in ["Levenshtein", "Standard"]:
			raise ValueError(
				"Input arg `distance_type` should be 'Levenshtein'/'Standard'")
		self._distance_type = distance_type

		# Insert/delete with cost from left/up.
		self.ins_cost, self.del_cost = 1, 1

		# Substitute with cost depending on distance type.
		if self._distance_type == "Standard":
			self.sub_cost = 1
		elif self._distance_type == "Levenshtein":
			self.sub_cost = 2

	def get_distance(self, str1, str2):
		n1, n2 = len(str1), len(str2)

		# Use table T to memorize edit distance for str1[:i1] and str2[:i2].
		T = [[0] * (n2 + 1) for _ in range(n1 + 1)]

		# Fill T for str1 = "" or str2 = "".
		for c in range(n2 + 1):
			T[0][c] = c
		for r in range(n1 + 1):
			T[r][0] = r

		# Update T's other cells by inserting, deleting & substituting.
		for r in range(1, n1 + 1):
			for c in range(1, n2 + 1):
				if str1[r - 1] == str2[c - 1]:
					T[r][c] = T[r - 1][c - 1]
				else:
					# Update T cells by min of cost + previous result.
					T[r][c] = min(self.ins_cost + T[r][c - 1], 
					              self.del_cost + T[r - 1][c],
					              self.sub_cost + T[r - 1][c - 1])

		return T[-1][-1]


def main():
	str1 = "intention"
	str2 = "execution"

	# Output: 5.
	std_min_edit_distance = MinimumEditDistance(distance_type="Standard")
	print std_min_edit_distance.get_distance(str1, str2)

	# Output: 8.
	levenshtein_min_edit_distance = MinimumEditDistance(distance_type="Levenshtein")
	print levenshtein_min_edit_distance.get_distance(str1, str2)


if __name__ == '__main__':
	main()
