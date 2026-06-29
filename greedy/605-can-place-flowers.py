"""
Problem Description:
Given a flowerbed represented by:

    0 -> empty
    1 -> occupied

Determine whether n new flowers can be planted such that
no two flowers are adjacent.

Approach:
- Handle small edge cases.
- Greedily plant a flower whenever:
    - the current plot is empty,
    - the left neighbor (if any) is empty,
    - the right neighbor (if any) is empty.
- Decrease n after each successful placement.
- If n becomes 0, return True.
- Otherwise, return whether all required flowers were planted.

Time Complexity:
O(n)

Space Complexity:
O(1)
"""

class Solution(object):

    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        if n == 0:
            return True

        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return (n - 1) == 0

        if n >= len(flowerbed):
            return False

        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1

            if n == 0:
                return True

        for i in range(1, len(flowerbed) - 1):

            if (
                flowerbed[i] == 0
                and flowerbed[i - 1] == 0
                and flowerbed[i + 1] == 0
            ):

                flowerbed[i] = 1
                n -= 1

                if n == 0:
                    return True

        if n > 0 and flowerbed[-1] == 0 and flowerbed[-2] == 0:
            flowerbed[-1] = 1
            n -= 1

        return n == 0
