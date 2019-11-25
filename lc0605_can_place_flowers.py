"""Leetcode 605. Can Place Flowers
Easy

URL: https://leetcode.com/problems/can-place-flowers/

Suppose you have a long flowerbed in which some of the plots are planted and some are not.
However, flowers cannot be planted in adjacent plots - 
they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1,
where 0 means empty and 1 means not empty), and a number n, 
return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False

Note:
- The input array won't violate no-adjacent-flowers rule.
- The input array size is in the range of [1, 20000].
- n is a non-negative integer which won't exceed the input array size.
"""

class SolutionIter(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if not n:
            return True

        # Edge case: flowerbed = [0].
        if flowerbed == [0]:
            if n == 1:
                return True
            else:
                return False

        # Iterate to plant n flowers starting from position i = 0.
        i = 0
        while n > 0 and i < len(flowerbed):
            if not flowerbed[i]:
                if i == 0:
                    if not flowerbed[i + 1]:
                        flowerbed[i] = 1
                        n -= 1
                elif i == len(flowerbed) - 1:
                    if not flowerbed[i - 1]:
                        flowerbed[i] = 1
                        n -= 1
                else:
                    if not flowerbed[i - 1] and not flowerbed[i + 1]:
                        flowerbed[i] = 1
                        n -= 1

            i += 1

        # Check if there remain flowers to plant.
        if n > 0:
            return False
        else:
            return True


def main():
    # Output: True
    flowerbed = [1,0,0,0,1]
    n = 1
    print SolutionIter().canPlaceFlowers(flowerbed, n)

    # Output: False
    flowerbed = [1,0,0,0,1]
    n = 2
    print SolutionIter().canPlaceFlowers(flowerbed, n)

    # Output: True
    flowerbed = [0,0,1]
    n = 1
    print SolutionIter().canPlaceFlowers(flowerbed, n)


if __name__ == '__main__':
    main()
