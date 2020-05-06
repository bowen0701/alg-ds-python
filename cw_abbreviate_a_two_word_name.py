"""Codewars: Abbreviate a Two Word Name
8 kyu

URL: https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3/

Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:
Sam Harris => S.H
Patrick Feeney => P.F
"""


def abbrevName(name):
    """
    Time complexity: O(n), where n is the number of words.
    Space complexity: O(n).
    """
    return '.'.join([w[0].upper() for w in name.split()])


def main():
    assert abbrevName("Sam Harris") == "S.H"
    assert abbrevName("Patrick Feenan") == "P.F"
    assert abbrevName("Evan Cole") == "E.C"
    assert abbrevName("P Favuzzi") == "P.F"
    assert abbrevName("David Mendieta") == "D.M"


if __name__ == '__main__':
    main()
