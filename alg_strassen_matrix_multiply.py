from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def matrix_multiply_naive(A, B):
    """Square matrix multiplication by naive algorithm.

    Time complexity: O(n^3)
    Space complexity: O(n^3)
    """
    n = len(A)
    C = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C


def _submatrix(A, row_idx, col_idx):
    """Sub-matrix by index calculation."""
    return [[A[i][j] for j in col_idx] for i in row_idx]


def _matrix_sum(A, B):
    """Sum of two matrices."""
    n = len(A)
    C = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C


def _matrix_assign(A, A_row_idx, A_col_idx, B):
    """Assign matrix B to sub-matrix A by index calculation."""
    for i in range(len(A_row_idx)):
        for j in range(len(A_col_idx)):
            A[A_row_idx[i]][A_col_idx[j]] = B[i][j]


def matrix_multiply_dc(A, B):
    """Square matrix multiplication by simple divide & conquer algorithm.

    Assume: the square matrix's dimension n is an exact power of 2.

    Time complexity: O(n^3)
    Space complexity: O(n^3)
    """
    n = len(A)
    C = [[0 for j in range(n)] for i in range(n)]

    if n == 1:
        C[0][0] = A[0][0] * B[0][0]
    else:
        # C11 = A11 * B11 + A12 * B21
        _matrix_assign(C, range(n // 2), range(n // 2),
            _matrix_sum(
                matrix_multiply_dc(
                    _submatrix(A, range(n // 2), range(n // 2)),
                    _submatrix(B, range(n // 2), range(n // 2))
                    ),
                matrix_multiply_dc(
                    _submatrix(A, range(n // 2), range(n // 2, n)),
                    _submatrix(B, range(n // 2, n), range(n // 2))
                    )
                )
            )

        # C12 = A11 * B12 + A12 * B22
        _matrix_assign(C, range(n // 2), range(n // 2, n),
            _matrix_sum(
                matrix_multiply_dc(
                    _submatrix(A, range(n // 2), range(n // 2)),
                    _submatrix(B, range(n // 2), range(n // 2, n))
                    ),
                matrix_multiply_dc(
                    _submatrix(A, range(n // 2), range(n // 2, n)),
                    _submatrix(B, range(n // 2, n), range(n // 2, n))
                    )
                )
            )

        # C21 = A21 * B11 + A22 * B21
        _matrix_assign(C, range(n // 2, n), range(n // 2),
            _matrix_sum(
                matrix_multiply_dc(
                    _submatrix(A, range(n // 2, n), range(n // 2)),
                    _submatrix(B, range(n // 2), range(n // 2))
                    ),
                matrix_multiply_dc(
                    _submatrix(A, range(n // 2, n), range(n // 2, n)),
                    _submatrix(B, range(n // 2, n), range(n // 2))
                    )
                )
            )

        # C22 = A21 * B12 + A22 * B22
        _matrix_assign(C, range(n // 2, n), range(n // 2, n),
            _matrix_sum(
                matrix_multiply_dc(
                    _submatrix(A, range(n // 2, n), range(n // 2)),
                    _submatrix(B, range(n // 2), range(n // 2, n))
                    ),
                matrix_multiply_dc(
                    _submatrix(A, range(n // 2, n), range(n // 2, n)),
                    _submatrix(B, range(n // 2, n), range(n // 2, n))
                    )
                )
            )
        
    return C


def strassen_matrix_multiply(A, B):
    """square matrix multiplication by Strassen's algorithm.

    Assume: the square matrix's dimension n is an exact power of 2.

    Time complexity: O(n^log7)
    Space complexity: O(n^3)
    """
    pass


def main():
    import time

    A = [[1, 3], [7, 5]]
    B = [[6, 8], [4, 2]]
    # [[18, 14], [62, 66]]

    start_time = time.time()
    print('By naive algorithm:\n{}'
          .format(matrix_multiply_naive(A, B)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By simple divide & conquer algorithm:\n{}'
          .format(matrix_multiply_dc(A, B)))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
