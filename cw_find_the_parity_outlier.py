"""Codewars: Find The Parity Outlier
6 kyu

URL: https://www.codewars.com/kata/5526fc09a1bbd946250002dc

You are given an array (which will have a length of at least 3,
but could be very large) containing integers.
The array is either entirely comprised of odd integers or 
entirely comprised of even integers except for a single integer N.
Write a method that takes the array as an argument and returns this "outlier" N.

Examples
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
"""

def find_outlier_naive(integers):
    # Iterate through integers to get number of evens.
    n_even = 0
    for i in range(len(integers)):
        if integers[i] % 2 == 0:
            n_even += 1

    # Obtain outlier is odd or even.
    if n_even > 1:
        outlier = 1
    else:
        outlier = 0
    
    for i in range(len(integers)):
        if outlier == integers[i] % 2:
            return integers[i]


def find_outlier(integers):
    """
    Collect evens and odds in one pass.

    Time complexity: O(n).
    Space complexity: O(n).
    """
    evens = []
    odds = []
    for i in integers:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)

    # If the number of events is one or not, then we get outlier.
    if len(evens) == 1:
        return evens[0]
    else:
        return odds[0]


def main():
    # Output: 11.
    integers = [2, 4, 0, 100, 4, 11, 2602, 36]
    print find_outlier(integers)

    # Output: 160
    integers = [160, 3, 1719, 19, 11, 13, -21]
    print find_outlier(integers)

    # Output: 2175970
    integers = [-7647303, -2670293, 9861423, -8134069, 9044429, -6477399, -7649341, 7689623, 6303953, 1239087, 5674661, 6572153, 2175970, -2144529, 7551097, -7069623, -4450133, 7611367, 632637, -1456711, 7081059, 7833561, -7208763, 8089047, 6067831, -231225]
    print find_outlier(integers)


if __name__ == '__main__':
    main()
