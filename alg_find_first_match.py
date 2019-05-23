from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def find_first_match(search, source):
    """Find first match.

    Find the position in source string with the search string. 
    
    Time complexity: O(nk), 
      where n and k is the length of source and search, respectively.
    Space complexity: O(k).
    """
    for i in range(len(source) - len(search)):
        if source[i:(i + len(search))] == search:
            return i
    return -1


def main():
    source = 'abcdyesefgh'
    search = 'yes'
    # Output: 5
    print(find_first_match(search, source))

    source =  'abcdyefg'
    search = 'yes'
    # Output = -1
    print(find_first_match(search, source))


if __name__ == '__main__':
    main()
