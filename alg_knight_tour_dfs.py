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

def _add_edge(adjacency_dict, vertex, move_vertex):
    adjacency_dict[vertex].add(move_vertex)
    adjacency_dict[move_vertex].add(vertex)

def build_knight_tour_graph(board_size):
    adjacency_dict = defaultdict(set)
    for row, col in product(xrange(board_size), xrange(board_size)):
        for move_row, move_col in _legal_moves_from(row, col, board_size):
            _add_edge(adjacency_dict, (row, col), (move_row, move_col))
    return adjacency_dict


def get_first_next_vertex(next_vertices):
    for vertex in next_vertices:
        if vertex:
            return vertex
    return None

def traverse_dfs(path_ls, current_vertex, 
                 adjacency_dict, total_squares, sorted_func=None):
    """Depth First Search traverse."""
    # Including the current square, if we have visited all squares,
    # just return the whole path as the solution.
    if len(path_ls) + 1 == total_squares:
        return path_ls + [current_vertex]

    legal_vertices = adjacency_dict[current_vertex] - set(path_ls)
    if not legal_vertices:
        # No legal neighbor vertices, so dead end.
        return False

    # Then try all valid paths.
    next_vertices = sorted(legal_vertices, sorted_func)
    return get_first_next_vertex(
        traverse_dfs(
            path_ls + [current_vertex], vertex,
            adjacency_dict, total_squares, sorted_func=sorted_func)
        for vertex in next_vertices)

def knight_tour_dfs(board_size, sorted_func=None):
    adjacency_dict = build_knight_tour_graph(board_size)
    total_squares = board_size * board_size
    
    path_ls = get_first_next_vertex(
        traverse_dfs(
            [], start_vertex, 
            adjacency_dict, total_squares, sorted_func=sorted_func)
        for start_vertex in adjacency_dict)
    return path_ls


def main():
    board_size = 5
    adjacency_dict = build_knight_tour_graph(board_size)
    print(adjacency_dict)

    path_ls = knight_tour_dfs(board_size, sorted_func=None)
    print('path_ls: {}'.format(path_ls))

if __name__ == '__main__':
    main()
