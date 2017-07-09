"""The tower of Hanoi."""
from __future__ import print_function

def move_towers(height, from_pole, to_pole, with_pole):
    move_towers(height - 1, from_pole, with_pole, to_pole)
    move_disk(from_pole, to_pole)
    move_towers(height - 1, with_pole, to_pole, from_pole)


def move_disk(from_pole, to_pole):
    print('Moving disk from {0} to {1}'
          .format(from_pole, to_pole))
