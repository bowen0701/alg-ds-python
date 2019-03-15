from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

class Person(object):
    def __init__(name, score):
        self.name = name
        self.score = score


def compare(a, b):
    """Sort an array of persons with comparator.

    Comparator:
      - If scores are equal, compare names.
      - If a.score is higher than b.score, a should appear first.
      - Vice versa.
    """
    if a.score == b.score:
        return a.name < b.name
    return b.score - a.score < 0


def quicksort_comparator(a_list):
    n = len(a_list)
    pivot = a_list[n // 2]
    left_list = [x for x in a_list if compare(x, pivot)]
    middle_list = [pivot]
    right_list = [x for x in a_list if compare(pivot, x)]
    return (
        quicksort_comparator(left_list) 
        + middle_list 
        + quicksort_comparator(right_list))


def print_person(a_list):
    print([x.name for x in a_list])


def main():
    gayle = Person('Gayle', 1903)
    john = Person('John', 1791)
    andy = Person('Andy', 1400)
    davis = Person('Davis', 1400)

    a_list = [davis, gayle, john, andy]

    sorted_list = quicksort_comparator(a_list)
    print_person(sorted_list)


if __name__ == '__main__':
    main()
