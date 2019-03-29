from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def longest_common_subsequence_recur(s1, s2, n1, n2):
	if n1 < 0 or n2 < 0:  # Base case.
		return 0
	elif s1[n1] == s2[n2]:
		return 1 + longest_common_subsequence_recur(
			s1, s2, n1 - 1, n2 - 1)
	elif s1[n1] != s2[n2]:  # Just for clarity.
		lcs1 = longest_common_subsequence_recur(s1, s2, n1 - 1, n2)
		lcs2 = longest_common_subsequence_recur(s1, s2, n1, n2 - 1)
		return max(lcs1, lcs2)


def longest_common_subsequence_memo(s1, s2, n1, n2):
	pass


def longest_common_subsequence_dp(s1, s2, n1, n2):
	pass


def main():
	s1 = 'BATD'
	s2 = 'ABACD'
	n1 = len(s1) - 1
	n2 = len(s2) - 1
	print('Length of LCD: {}'.format(
		longest_common_subsequence_recur(s1, s2, n1, n2)))


if __name__ == '__main__':
	main()
