from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

from collections import defaultdict 
from itertools import product


MOVE_OFFSETS = (
              (-1, -2), (1, -2),
    (-2, -1),                    (2, -1),
    (-2,  1),                    (2,  1),
              (-1,  2), (1, 2)             
)

def _legal_moves_from(row, col, board_size):
	for row_offset, col_offset in MOVE_OFFSETS:
		move_row, move_col = row + row_offset, col + col_offset
		if 0 <= move_row < board_size and 0 <= move_col < board_size:
			yield move_row, move_col

def _add_edge(graph_dict, vertex, move_vertex):
	graph_dict[vertex].add(move_vertex)
	graph_dict[move_vertex].add(vertex)

def build_knight_tour_graph(board_size):
    graph_dict = defaultdict(set)
    for row, col in product(xrange(board_size), xrange(board_size)):
    	for move_row, move_col in _legal_moves_from(row, col, board_size):
    		_add_edge(graph_dict, (row, col), (move_row, move_col))
    return graph_dict


def main():
    board_size = 8
    graph_dict = build_knight_tour_graph(board_size)
    print(graph_dict)

if __name__ == '__main__':
    main()
