"""The tower of Hanoi."""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def tower_of_hanoi(height, from_pole, to_pole, with_pole, counter):
    """Tower of Hanoi.

    Time complexity: T(1) = 1, T(n) = 2T(n - 1) + 1 => O(2^n).
    Space complexity: O(1).
    """
    if height == 1:
        counter[0] += 1
        print('{0} -> {1}'.format(from_pole, to_pole))
    else:
        tower_of_hanoi(height - 1, from_pole, with_pole, to_pole, counter)
        tower_of_hanoi(1, from_pole, to_pole, with_pole, counter)
        tower_of_hanoi(height - 1, with_pole, to_pole, from_pole, counter)  


def main():
    from_pole = 'A' 
    to_pole = 'B'
    with_pole = 'C'

    height = 1
    counter = [0]
    print('height: {}'.format(height))
    tower_of_hanoi(height, from_pole, to_pole, with_pole, counter)
    print('counter: {}'.format(counter[0]))

    height = 2
    counter = [0]
    print('height: {}'.format(height))
    tower_of_hanoi(height, from_pole, to_pole, with_pole, counter)
    print('counter: {}'.format(counter[0]))

    height = 5
    counter = [0]
    print('height: {}'.format(height))
    tower_of_hanoi(height, from_pole, to_pole, with_pole, counter)
    print('counter: {}'.format(counter[0]))


if __name__ == '__main__':
    main()
