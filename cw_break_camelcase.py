"""Codewars: Break camelCase
6kyu

URL: https://www.codewars.com/kata/5208f99aee097e6552000148/

Complete the solution so that the function will break up camel casing,
using a space between words.

Example
solution("camelCasing")  ==  "camel Casing"
"""


def break_camel(s):
    """
    Time complexity: O(n).
    Space complexity: O(n).
    """
    ls = []
    for c in s:
        if c.isupper():
            ls.append(' ')
        ls.append(c)
    return ''.join(ls)


def main():
    assert break_camel("helloWorld") == "hello World"
    assert break_camel("camelCase") == "camel Case"
    assert break_camel("breakCamelCase") == "break Camel Case"


