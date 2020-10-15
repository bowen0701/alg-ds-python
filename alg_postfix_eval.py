from __future__ import print_function
from __future__ import division
from ds_stack import Stack

def eval_postfix(postfix_str):
    """Evaluate postfix: A B * = A * B.

    Args:
      postfix_str: A string. Multiple postfix string.

    Returns:
      A float. Evaluated postfix result.
    """
    operand_stack = Stack()
    
    tokens = postfix_str.split()

    for token in tokens:
        if token in '0123456789':
            operand_stack.push(int(token))
        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = do_math(token, operand1, operand2)
            operand_stack.push(result)
    
    return operand_stack.pop()


def do_math(op, operand1, operand2):
    if op == '*':
        return operand1 * operand2
    elif op == '/':
        return operand1 / operand2
    elif op == '+':
        return operand1 + operand2
    elif op == '-':
        return operand1 - operand2
    else:
        raise ValueError('Incorrect operation.')


def main():
    print('4 2 *')
    print(eval_postfix('4 2 *'))

    print('4 2 /')
    print(eval_postfix('4 2 /'))

    print('4 2 +')
    print(eval_postfix('4 2 +'))
  
    print('4 2 -')
    print(eval_postfix('4 2 -'))


if __name__ == '__main__':
    main()
