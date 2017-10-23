"""The tower of Hanoi."""
from __future__ import print_function


def move_towers(height, from_pole, to_pole, with_pole):
    if height == 1:
        print('Moving disk from {0} to {1}'.format(from_pole, to_pole))
    else:
        move_towers(height - 1, from_pole, with_pole, to_pole)
        move_towers(1, from_pole, to_pole, with_pole)
        move_towers(height - 1, with_pole, to_pole, from_pole)  


def main():
    from_pole = 'f' 
    to_pole = 't'
    with_pole = 'w'

    height = 1
    print('height: {}'.format(height))
    move_towers(height, from_pole, to_pole, with_pole)

    height = 2
    print('height: {}'.format(height))
    move_towers(height, from_pole, to_pole, with_pole)

    height = 5 
    print('height: {}'.format(height))
    move_towers(height, from_pole, to_pole, with_pole)

if __name__ == '__main__':
    main()
