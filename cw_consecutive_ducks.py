"""Codewars: Consecutive Ducks
7 kyu

URL: https://www.codewars.com/kata/5dae2599a8f7d90025d2f15f/

Positive integers have so many gorgeous features. Some of them could be
expressed as a sum of two or more consecutive positive numbers.

Consider an Example :
10 , could be expressed as a sum of 1 + 2 + 3 + 4.
Task
Given Positive integer, N , Return true if it could be expressed as a sum
of two or more consecutive positive numbers , OtherWise return false .

Notes
Guaranteed constraint : 2 <= N <= (2^32) -1 .
Input >> Output Examples:
* consecutiveDucks(9) ==> return (true)  //  9 , could be expressed as
  a sum of ( 2 + 3 + 4 ) or ( 4 + 5 ) .
* consecutiveDucks(64) ==> return (false)
* consecutiveDucks(42) ==> return (true) //  42 , could be expressed
"""


def consecutive_ducks1(n):
    """
    Time complexity: O(n)
    Space complexity: O(n).
    """
    # Edge case.
    if n == 2:
        return False

    # Create dict cusum_idx_d:cusum->idx.
    # Check if cusum - n exists in cusum_idx_d.
    cusums = [0]
    cusum_idx_d = dict()
    cusum_idx_d[0] = 0
    for i in range(1, n + 1):
        cusums.append(cusums[i - 1] + i)
        cusum_idx_d[cusums[i]] = i

        diff = cusums[i] - n
        if diff in cusum_idx_d and i - cusum_idx_d[diff] >= 2:
            return True

    return False


def consecutive_ducks2(n):
    """
    Time complexity: O(1).
    Space complexity: O(1).
    """
    # Edge case.
    if n == 2:
        return False

    # Check if n is odd, then it can be expressed.
    if n % 2 == 1:
        return True

    # Check if n is power of two, then it cannot be expressed.
    if n & (n - 1) == 0:
        return False

    return True


def main():    
    consecutive_ducks = consecutive_ducks2

    assert consecutive_ducks(3984309891) == True
    assert consecutive_ducks(10) == True
    assert consecutive_ducks(9) == True
    assert consecutive_ducks(64) == False
    assert consecutive_ducks(42) == True

    assert consecutive_ducks(69) == True
    assert consecutive_ducks(8) == False
    assert consecutive_ducks(57) == True
    assert consecutive_ducks(6) == True
    assert consecutive_ducks(13) == True
    assert consecutive_ducks(16) == False
    assert consecutive_ducks(91) == True
    assert consecutive_ducks(75) == True
    assert consecutive_ducks(38) == True
    assert consecutive_ducks(25) == True
    assert consecutive_ducks(32) == False
    assert consecutive_ducks(65) == True
    assert consecutive_ducks(13) == True
    assert consecutive_ducks(16) == False
    assert consecutive_ducks(99) == True
    
    # Check Medium Values
    assert consecutive_ducks(522) == True
    assert consecutive_ducks(974) == True
    assert consecutive_ducks(755) == True
    assert consecutive_ducks(512) == False
    assert consecutive_ducks(739) == True
    assert consecutive_ducks(1006) == True
    assert consecutive_ducks(838) == True
    assert consecutive_ducks(1092) == True
    assert consecutive_ducks(727) == True
    assert consecutive_ducks(648) == True
    assert consecutive_ducks(1024) == False
    assert consecutive_ducks(851) == True
    assert consecutive_ducks(541) == True
    assert consecutive_ducks(1011) == True
    assert consecutive_ducks(822) == True
    
    # Check Large Values.
    assert consecutive_ducks(382131) == True
    assert consecutive_ducks(118070) == True
    assert consecutive_ducks(17209) == True
    assert consecutive_ducks(32768) == False
    assert consecutive_ducks(161997) == True
    assert consecutive_ducks(400779) == True
    assert consecutive_ducks(198331) == True
    assert consecutive_ducks(325482) == True
    assert consecutive_ducks(88441) == True
    assert consecutive_ducks(648) == True
    assert consecutive_ducks(65536) == False
    assert consecutive_ducks(323744) == True
    assert consecutive_ducks(183540) == True
    assert consecutive_ducks(65271) == True
    assert consecutive_ducks(5263987) == True


if __name__ == '__main__':
    main()
