from __future__ import print_function
from __future__ import division

from ds_stack import Stack
from ds_binary_tree import BinaryTree


def build_parse_tree(fp_exp):
    fp_ls = fp_exp.split()
    par_stack = Stack()
    parse_tree = BinaryTree('')
    par_stack.push(parse_tree)
    current_tree = parse_tree
    for i in fp_ls:
        if i == '(':
            current_tree.insert_left('')
            par_stack.push(current_tree)
            current_tree = current_tree.get_left_tree()
        elif i not in '+-*/)':
            current_tree.set_root_value(eval(i))
            parent = par_stack.pop()
            current_tree = parent
        elif i in '+-*/':
            current_tree.set_root_value(i)
            current_tree.insert_right('')
            par_stack.push(current_tree)
            current_tree = current_tree.get_right_tree()
        elif i == ')':
            current_tree = par_stack.pop()
        else:
            raise ValueError('Unknown operator: {}'.format(i))
    return parse_tree


def eval_tree(parse_tree):
    import operator
    opers = {'+': operator.add,
             '-': operator.sub,
             '*': operator.mul,
             '/': operator.truediv}

    left_tree = parse_tree.get_left_tree()
    right_tree = parse_tree.get_right_tree()
    if left_tree and right_tree:
        ft = opers[parse_tree.get_root_value()]
        return ft(eval_tree(left_tree), eval_tree(right_tree))
    else:
        return parse_tree.get_root_value()


def postorder_eval_tree(parse_tree):
    import operator
    opers = {'+': operator.add,
             '-': operator.sub,
             '*': operator.mul,
             '/': operator.truediv}

    left_tree = None
    right_tree = None  
    if parse_tree:
        left_tree = postorder_eval_tree(parse_tree.get_left_tree())
        right_tree = postorder_eval_tree(parse_tree.get_right_tree())
        if left_tree and right_tree:
            ft = opers[parse_tree.get_root_value()]
            return ft(left_tree, right_tree)
        else:
            return parse_tree.get_root_value()


def main():
    fp_exp = '( 3 + ( 4 * 5 ) )'
    parse_tree = build_parse_tree(fp_exp)
    val_tree = eval_tree(parse_tree)
    print('For eval {0}: {1}'.format(fp_exp, val_tree))
    postorder_val_tree = postorder_eval_tree(parse_tree)
    print('For postorder eval {0}: {1}'.format(
        fp_exp, postorder_val_tree))

    fp_exp = '( ( 5 - 3 ) / ( 4 * 2 ) )'
    parse_tree = build_parse_tree(fp_exp)
    val_tree = eval_tree(parse_tree)
    print('For eval {0}: {1}'.format(fp_exp, val_tree))
    postorder_val_tree = postorder_eval_tree(parse_tree)
    print('For postorder eval {0}: {1}'.format(
        fp_exp, postorder_val_tree))


if __name__ == '__main__':
    main()
