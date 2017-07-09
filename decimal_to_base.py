from ds_stack import Stack


def convert_decimal_to_base2(dec_num):
	"""Convert decimal number to binary number."""
	rem_stack = Stack()
	
	while dec_num > 0:
		rem = dec_num % 2
		rem_stack.push(rem)
		# TODO: Update dec_num.
		# dec_num = 


def convert_decimal_to_base(dec_num, base):
	"""Convert decimal number to any base."""
	pass
