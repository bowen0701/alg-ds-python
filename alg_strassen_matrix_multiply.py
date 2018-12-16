from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def square_matrix_multiply(A, B):
    """Square matrix multiplication by naive algorithm."""
    n = len(A)
    C = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C


def _matrix_index_calculation(A, row_indices, col_indices):
    """Sub-matrix by index calculation."""
    return [[A[i][j] for j in col_indices] for i in row_indices]


def _matrix_sum(A, B):
    """Sum of two matrices."""
    m, n = len(A), len(A[0])
    C = [[0 for j in range(n)] for i in range(m)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C


def _matrix_assign(A, A_row_indices, A_col_indices, B):
    """Assign matrix B to sub-matrix A by index calculation."""
    for i in range(len(A_row_indices)):
        for j in range(len(A_col_indices)):
            A[A_row_indices[i]][A_col_indices[j]] = B[i][j]


def square_matrix_multiply_dc(A, B):
    """Square matrix multiplication by simple divide & conquer algorithm.

    Assume: the square matrix's dimension n is an exact power of 2.
    """
    n = len(A)
    C = [[0 for j in range(n)] for i in range(n)]

    if n == 1:
        C[0][0] = A[0][0] * B[0][0]
    else:
        # C11 = A11 * B11 + A12 * B21
        C11 = _matrix_sum(
            square_matrix_multiply_dc(
                _matrix_index_calculation(A, range(n // 2), range(n // 2)),
                _matrix_index_calculation(B, range(n // 2), range(n // 2))
                ),
            square_matrix_multiply_dc(
                _matrix_index_calculation(A, range(n // 2), range(n // 2, n)),
                _matrix_index_calculation(B, range(n // 2, n), range(n // 2))
                )
            )
        _matrix_assign(C, range(n // 2), range(n // 2), C11)

        # C12 = A11 * B12 + A12 * B22
        C12 = _matrix_sum(
            square_matrix_multiply_dc(
                _matrix_index_calculation(A, range(n // 2), range(n // 2)),
                _matrix_index_calculation(B, range(n // 2), range(n // 2, n))
                ),
            square_matrix_multiply_dc(
                _matrix_index_calculation(A, range(n // 2), range(n // 2, n)),
                _matrix_index_calculation(B, range(n // 2, n), range(n // 2, n))
                )
            )
        _matrix_assign(C, range(n // 2), range(n // 2, n), C12)

        # C21 = A21 * B11 + A22 * B21
        C21 = _matrix_sum(
            square_matrix_multiply_dc(
                _matrix_index_calculation(A, range(n // 2, n), range(n // 2)),
                _matrix_index_calculation(B, range(n // 2), range(n // 2))
                ),
            square_matrix_multiply_dc(
                _matrix_index_calculation(A, range(n // 2, n), range(n // 2, n)),
                _matrix_index_calculation(B, range(n // 2, n), range(n // 2))
                )
            )
        _matrix_assign(C, range(n // 2, n), range(n // 2), C21)

        # C22 = A21 * B12 + A22 * B22
        C22 = _matrix_sum(
            square_matrix_multiply_dc(
                _matrix_index_calculation(A, range(n // 2, n), range(n // 2)),
                _matrix_index_calculation(B, range(n // 2), range(n // 2, n))
                ),
            square_matrix_multiply_dc(
                _matrix_index_calculation(A, range(n // 2, n), range(n // 2, n)),
                _matrix_index_calculation(B, range(n // 2, n), range(n // 2, n))
                )
            )
        _matrix_assign(C, range(n // 2, n), range(n // 2, n), C22)
        
    return C


def strassen_square_matrix_multiply(A, B):
    """square matrix multiplication by Strassen's algorithm.

    Assume: the square matrix's dimension n is an exact power of 2.

    Time complexity: O(n^log7)
    Space complexity: O(1).
    """
    pass


def main():
    import time

    # From CLRS, Ex 4.2-1, p. 83. 
    A = [[1, 3], [7, 5]]
    B = [[6, 8], [4, 2]]
    # A = [[1, 3, 4, 6], [7, 5, 9, 5], [2, 6, 5, 7], [3, 7, 5, 4]]
    # B = [[6, 8, 5, 9], [4, 2, 8, 2], [3, 1, 9, 5], [5, 2, 1, 8]]

    start_time = time.time()
    print('By naive algorithm:\n{}'.format(square_matrix_multiply(A, B)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By simple divide & conquer algorithm:\n{}'
          .format(square_matrix_multiply_dc(A, B)))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
