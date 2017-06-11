from ds_stack import Stack

def balance_parentheses(symbol_str):
    """Balance parentheses in a string.

    I extend balance parentheses '()' to an "arbitrary" string.
    """
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
    		else:
    			s.pop()
    	else:
    		pass
    	index += 1

    if balanced and s.is_empty():
    	return True
    else:
    	return False


def _match_symbols(open, close):
    opens = '([{'
    closers = ')]}'
    match_flag = opens.index(open) == closers.index(close)
    return match_flag

def balance_symbols(symbol_str):
    """Balance symbols in a string.

    I extend balance symbols to an "arbitrary" string.
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
            else:
                top = s.pop()
                if not _match_symbols(top, symbol):
                    balanced = False
        else:
            pass
        index += 1

    if balanced and s.is_empty():
        return True
    else:
        return False
