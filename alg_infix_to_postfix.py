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
    postfix_ls = []

    token_ls = infix_str.split()

    for token in token_ls:
        if token in string.ascii_uppercase:
            postfix_ls.append(token)
        elif token == '(':
            op_stack.push(token)
        elif token == ')':
            top_token = op_stack.pop()
            while top_token != '(':
                postfix_ls.append(top_token)
                top_token = op_stack.pop()
        elif token in '*/+-':
            while ((not op_stack.is_empty()) and 
                   (order[op_stack.peek()] <= order[token])):
                postfix_ls.append(op_stack.pop())
            op_stack.push(token)
        else:
            raise ValueError('Incorrect string.')

    while not op_stack.is_empty():
        postfix_ls.append(op_stack.pop())

    return ' '.join(postfix_ls)


if __name__ == '__main__':
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
