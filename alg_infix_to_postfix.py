from __future__ import print_function
from ds_stack import Stack
import string

def convert_infix_to_postfix(infix_str):
    order = {}
    order['*'] = 1
    order['/'] = 1
    order['+'] = 2
    order['-'] = 2
    order['('] = 3

    op_stack = Stack()
    postfixes = []

    tokens = infix_str.split()

    for token in tokens:
        if token in string.ascii_uppercase:
            postfixes.append(token)
        elif token == '(':
            op_stack.push(token)
        elif token == ')':
            top_token = op_stack.pop()
            while top_token != '(':
                postfixes.append(top_token)
                top_token = op_stack.pop()
        elif token in '*/+-':
            while ((not op_stack.is_empty()) and 
                   (order[op_stack.peek()] <= order[token])):
                postfixes.append(op_stack.pop())
            op_stack.push(token)
        else:
            raise ValueError('Incorrect string.')

    while not op_stack.is_empty():
        postfixes.append(op_stack.pop())

    return ' '.join(postfixes)


def main():
    s = '( A + B ) * ( C + D )'
    print('Infix:', s)
    print('Postfix:', convert_infix_to_postfix(s))

    s = '( A + B ) * C'
    print('Infix:', s)
    print('Postfix:', convert_infix_to_postfix(s))

    s = 'A + B * C'    
    print('Infix:', s)
    print('Postfix:', convert_infix_to_postfix(s))

    s = 'A + B * C + D'
    print('Infix:', s)
    print('Postfix:', convert_infix_to_postfix(s))


if __name__ == '__main__':
    main()
