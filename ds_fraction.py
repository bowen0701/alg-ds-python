from __future__ import print_function
from alg_gcd import compute_gcd

class Fraction(object):
    """Fraction class with print, show, add, subtract,
    multiplication, division and equality.

    W extend some of the above methods.
    """
    def __init__(self, num, den):
        gcd = compute_gcd(num, den)
        self.num = num / gcd
        self.den = den / gcd
        
    def __str__(self):
        return str(self.num) + '/' + str(self.den)
    
    def show(self):
        print(self.num, '/', self.den)

    def __add__(self, other_frac):
        new_num = self.num * other_frac.den + \
            self.den * other_frac.num
        new_den = self.den * other_frac.den
        gcd = compute_gcd(new_num, new_den)
        new_num = new_num // gcd
        new_den = new_den // gcd
        if new_num == new_den:
            fracs_add = 1
        else:
            fracs_add = Fraction(new_num, new_den)
        return fracs_add
    
    def __sub__(self, other_frac):
        new_num = self.num * other_frac.den - \
            self.den * other_frac.num
        new_den = self.den * other_frac.den
        gcd = compute_gcd(new_num, new_den)
        new_num = new_num // gcd
        new_den = new_den // gcd
        if new_num == new_den:
            fracs_sub = 1
        else:
            fracs_sub = Fraction(new_num, new_den)
        return fracs_sub

    def __mul__(self, other_frac):
        new_num = self.num * other_frac.num
        new_den = self.den * other_frac.den
        gcd = compute_gcd(new_num, new_den)
        new_num = new_num // gcd
        new_den = new_den // gcd
        if new_num == new_den:
            fracs_div = 1
        else:
            fracs_div = Fraction(new_num, new_den)
        return fracs_div

    def __div__(self, other_frac):
        new_num = self.num * other_frac.den
        new_den = self.den * other_frac.num
        gcd = compute_gcd(new_num, new_den)
        new_num = new_num // gcd
        new_den = new_den // gcd
        if new_num == new_den:
            fracs_div = 1
        else:
            fracs_div = Fraction(new_num, new_den)
        return fracs_div

    def __eq__(self, other_frac):
        first_num = self.num * other_frac.den
        second_num = other_frac.num * self.den
        return first_num == second_num
