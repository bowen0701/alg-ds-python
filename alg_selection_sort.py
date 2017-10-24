def selection_sort(a_list):
    """Selection Sort algortihm.

    Concept: 
      - Find out the max item's original slot first,
      - then swap it and the item at the max slot. 
      - Iterate the procedure for the next max, etc. 
    """
    for max_slot in reversed(range(len(a_list))):
        select_slot = 0
        for slot in range(1, max_slot + 1):
            if a_list[slot] > a_list[select_slot]:
                select_slot = slot

        temp = a_list[max_slot]
        a_list[max_slot] = a_list[select_slot]
        a_list[select_slot] = temp


def main():
    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print('a_list: {}'.format(a_list))
    print('By selection sort: ')
    selection_sort(a_list)
    print(a_list)


if __name__ == '__main__':
    main()
