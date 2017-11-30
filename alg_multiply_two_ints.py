def multiply_two_ints(x, y):
	"""Multiply 2 n-digits integers by divide-and-conquer algorithm"""
    x_str = str(x)
    y_str = str(y)
    if len(x_str) != len(y_str):
    	raise ValueError('The 2 numbers are of not equal lenght')
    else:
    	n = len(x_str)
    left_x_str, right_x_str = x_str[:n], x_str[n:]
    left_y_str, right_y_str = y_str[:n], y_str[n:]
    left_prod_str = 



def main():
    pass

if __name__ == '__main__':
    main()
