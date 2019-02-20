from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from ds_stack import Stack


def balance_parentheses(symbol_str):
    """Balance parentheses in a string."""
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbol_str) and balanced:
        symbol = symbol_str[index]
        if symbol == '(':
            s.push(symbol)
        elif symbol == ')':
            if s.is_empty():
                balanced = False
                break
            else:
                s.pop()
        else:
            pass
        index += 1

    if balanced and s.is_empty():
        return True
    else:
        return False


def _match_symbols(opener, closer):
    openers = '([{'
    closers = ')]}'
    match_bool = openers.index(opener) == closers.index(closer)
    return match_bool


def balance_symbols(symbol_str):
    """Balance "arbitrary" symbols in a string.
    The symbols here are '()', '[]' and '{}'. 
    """
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbol_str) and balanced:
        symbol = symbol_str[index]
        if symbol in '([{':
            s.push(symbol)
        elif symbol in ')]}':
            if s.is_empty():
                balanced = False
                break
            else:
                open_symbol = s.pop()
                if not _match_symbols(open_symbol, symbol):
                    balanced = False
                    break
        else:
            pass
        index += 1

    if balanced and s.is_empty():
        return True
    else:
        return False


def main():
    import time

    text_match = '(abcd)'

    start_time = time.time()
    print('By balance_parentheses(): {}'
          .format(balance_parentheses(text_match)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By balance_symbols(): {}'
          .format(balance_symbols(text_match)))
    print('Time: {}'.format(time.time() - start_time))

    text_match2 = '([abcd]efg)'

    start_time = time.time()
    print('By balance_symbols(): {}'
          .format(balance_symbols(text_match2)))
    print('Time: {}'.format(time.time() - start_time))

    text_unmatch = '(abcd]'

    start_time = time.time()
    print('By balance_parentheses(): {}'
          .format(balance_parentheses(text_unmatch)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By balance_symbols(): {}'
          .format(balance_symbols(text_unmatch)))
    print('Time: {}'.format(time.time() - start_time))



if __name__ == '__main__':
    main()
