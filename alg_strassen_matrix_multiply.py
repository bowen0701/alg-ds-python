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


def _matrix_sum(A, B):
    m, n = len(A), len(A[0])
    C = [[0 for j in range(n)] for i in range(m)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C


def square_matrix_multiply_dc(A, B):
    """Square matrix multiplication by simple divide & conquer algorithm"""
    n = len(A)
    print('n: {}'.format(n))
    C = [[0 for j in range(n)] for i in range(n)]

    if n == 1:
        C[0][0] = A[0][0] * B[0][0]
    else:
        # TODO: Come up with how to do index calculation.
        # C11 = A11 * B11 + A12 * B21
        C[:(n // 2)][:(n // 2)] = _square_matrix_sum(
            square_matrix_multiply_dc(
                A[:(n // 2)][:(n // 2)], B[:(n // 2)][:(n // 2)]),
            square_matrix_multiply_dc(
                A[:(n // 2)][(n // 2):], B[(n // 2):][:(n // 2)]))

        # C12 = A11 * B12 + A12 * B22
        C[:(n // 2)][(n // 2):] = _square_matrix_sum(
            square_matrix_multiply_dc(
                A[:(n // 2)][:(n // 2)], B[:(n // 2)][(n // 2):]),
            square_matrix_multiply_dc(
                A[:(n // 2)][(n // 2):], B[:(n // 2)][:(n // 2)]))

        # C21 = A21 * B11 + A22 * B21
        C[(n // 2):][:(n // 2)] = _square_matrix_sum(
            square_matrix_multiply_dc(
                A[(n // 2):][:(n // 2)], B[:(n // 2)][:(n // 2)]),
            square_matrix_multiply_dc(
                A[(n // 2):][(n // 2):], B[(n // 2):][:(n // 2)]))

        # C22 = A21 * B12 + A22 * B22
        C[(n // 2):][(n // 2):] = _square_matrix_sum(
            square_matrix_multiply_dc(
                A[(n // 2):][:(n // 2)], B[:(n // 2)][(n // 2):]),
            square_matrix_multiply_dc(
                A[(n // 2):][(n // 2):], B[(n // 2):][(n // 2):]))
        
    return C


def strassen_square_matrix_multiply(A, B):
    """square matrix multiplication by Strassen's algorithm.

    Note: Here assume the square matrix's dimension n is an exact power of 2.

    Time complexity: O(n^log7)
    Space complexity: O(1).
    """
    pass


def main():
    import time

    # From CLRS, Ex 4.2-1, p. 83. 
    A = [[1, 3], [7, 5]]
    B = [[6, 8], [4, 2]]

    start_time = time.time()
    print('By naive algorithm:\n{}'.format(square_matrix_multiply(A, B)))
    print('Time: {}'.format(time.time() - start_time))

    # start_time = time.time()
    # print('By simple divide & conquer algorithm:\n{}'
    #       .format(square_matrix_multiply_dc(A, B)))
    # print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
