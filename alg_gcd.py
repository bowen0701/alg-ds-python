def compute_gcd(m, n):
    """Compute the greatest common divisor by Euclid's Algorithm."""
    while m % n != 0:
        old_m = m
        old_n = n
        m = old_n
        n = old_m % old_n
    return n
