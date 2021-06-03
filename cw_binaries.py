"""Codewars: Binaries
6 kyu

URL: https://www.codewars.com/kata/5d98b6b38b0f6c001a461198/

Let us take a string composed of decimal digits: "10111213". We want to code
this string as a string of 0 and 1 and after that be able to decode it.

We decompose the given string in its decimal digits 1 0 1 1 1 2 1 3 and we
will code each.

Coding process to code a number n expressed in base 10:
a) Let k be the number of bits of n
b) Put k-1 times the digit 0 followed by the digit 1
c) Put number n in binary
d) Concat the result of b) and c)

So we code 0 as 10, 1 as 11 ... etc...

Repeating this process with the initial string

"10111213" becomes : "11101111110110110111" resulting of concatenation of
11 10 11 11 11 0110 11 0111 .

Task:
- Given strng a string of digits representing a decimal number the function
  code(strng) should return the coding of strng as explained above.
- Given a string strng resulting from the previous coding, decode it to get
  the corresponding decimal string.

Examples:
code("77338855") --> "001111001111011101110001100000011000001101001101"
code("77338")  --> "0011110011110111011100011000"
code("0011121314") --> "1010111111011011011111001100"

decode("001111001111011101110001100000011000001101001101") -> "77338855"
decode("001111 001111 0111011100011000") ->  "77338"
decode("1010111111011011011111001100") -> "0011121314"
"""


def _encode(c):
    binary = bin(int(c))[2:]
    k = len(binary)
    code01 = '0' * (k - 1) + '1'
    return code01 + binary


def code(strng):
    """Code decimal digits to special binary codes.

    Time complexity: O(n), where n is the number of decimal digits.
    Space complexity: O(n).
    """
    # Edge case.
    if not strng:
        return ''

    # Iterate through char in strng, encode it and append to encode_ls.
    encode_ls = []
    for c in strng:
        code = _encode(c)
        encode_ls.append(code)
    return ''.join(encode_ls)

    
def decode(strng):
    """Decode special binary codes back to decimal digits.

    Time complexity: O(n), where n is the number of decimal digits.
    Space complexity: O(n).
    """
    n = len(strng)
    
    # Create a dict:digit->code01.
    digit_code_d = {d: _encode(str(d)) for d in range(10)}

    # Apply max match with digits in descending order, 
    # with one pointer as the start of the next code.
    decode_ls = []
    i = 0
    while i < n - 1:
        for d in reversed(range(10)):
            code = digit_code_d[d]
            if strng[i:i+len(code)] == code:
                decode_ls.append(str(d))
                i += len(code)
                break
    return ''.join(decode_ls)


def main():
    assert code("62") == "0011100110"
    assert code("55337700") == "001101001101011101110011110011111010"
    assert code("1119441933000055") == "1111110001100100110000110011000110010111011110101010001101001101"
    assert code("69") == "00111000011001"
    assert code("86") == "00011000001110"

    assert decode("10001111") == "07"
    assert decode("001100001100001100001110001110001110011101110111001110001110001110001111001111001111001100001100001100") == "444666333666777444"
    assert decode("01110111110001100100011000000110000011110011110111011100110000110001100110") == "33198877334422"
    assert decode("0011010011010011011010101111110011000011000011000011100011100011100011100011100011100001100100011001000110011100011001001111001111001111001111001111001111") == "55500011144466666699919777777"
    assert decode("01110111011111000110010011110011110011110011110011110011110111011101110110011001100110011001101111111010101100011001000110000001100000011000") == "3331977777733322222211100019888"


if __name__ == '__main__':
    main()
