"""The tower of Hanoi."""

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def tower_of_hanoi(height, from_pole, to_pole, with_pole, counter):
    """Tower of Hanoi.

    height = 1: 0 + 1 + 0 = 1 step,
    height = 2: 1 + 1 + 1 = 3 steps,
    height = 3: 3 + 1 + 3 = 7 steps,
    height = 4: 7 + 1 + 7 = 15 steps,
    and so on.

    tower_of_hanoi(n) = 2^n - 1.

    Time complexity: T(1) = 1, T(n) = 2T(n - 1) + 1 => O(2^n).
    Space complexity: O(1).
    """
    if height == 1:
        counter[0] += 1
        print('{0} -> {1}'.format(from_pole, to_pole))
        return

    # Move (n - 1) disks to with_pole, the (largest) nth to to_pole,
    # finally (n - 1) disks to to_pole.
    tower_of_hanoi(height - 1, from_pole, with_pole, to_pole, counter)
    tower_of_hanoi(1, from_pole, to_pole, with_pole, counter)
    tower_of_hanoi(height - 1, with_pole, to_pole, from_pole, counter)  


def main():
    from_pole = 'A' 
    to_pole = 'B'
    with_pole = 'C'

    # Output: 1.
    height = 1
    counter = [0]
    print('height: {}'.format(height))
    tower_of_hanoi(height, from_pole, to_pole, with_pole, counter)
    print('counter: {}'.format(counter[0]))

    # Output: 3.
    height = 2
    counter = [0]
    print('height: {}'.format(height))
    tower_of_hanoi(height, from_pole, to_pole, with_pole, counter)
    print('counter: {}'.format(counter[0]))

    # Output: 31.
    height = 5
    counter = [0]
    print('height: {}'.format(height))
    tower_of_hanoi(height, from_pole, to_pole, with_pole, counter)
    print('counter: {}'.format(counter[0]))


if __name__ == '__main__':
    main()
