def gcd(m, n):
    """Greatest Common Divisor (GCD) by Euclid's Algorithm.

    Time complexity: O(m%n).
    """
    while n != 0:
        m, n = n, m % n
    return m


def main():
    print(gcd(4, 2))
    print(gcd(2, 4))

    print(gcd(10, 4))
    print(gcd(4, 10))

    print(gcd(10, 1))
    print(gcd(1, 10))


if __name__ == '__main__':
    main()
