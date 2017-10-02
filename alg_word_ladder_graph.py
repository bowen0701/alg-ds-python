from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

WORDS_FILE = 'four_letter_words.txt'


def read_words():
	"""Read words file with producing a generator."""
	with open(WORDS_FILE) as f:
		for line in f:
			yield line[:-1]


def build_word_ladder_graph(words):
	vertex_dict = {}
	graph_dict = {}

	# Create buckets of words that are different by one letter.
	for word in words:
		for i in xrange(len(word)):
			bucket = '{0}_{1}'.format(word[:i], word[i+1:])
			if bucket in vertex_dict:
				vertex_dict[bucket].append(word)
			else:
				vertex_dict[bucket] = list(word)

	pass


def main():
	words = read_words()


if __name__ == '__main__':
	main()
