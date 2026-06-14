"""
Problem Description:
Given an integer n, return True if its binary representation
contains exactly one pair of consecutive 1s.

Examples:

    6  -> 110   -> True
    14 -> 1110  -> False
    5  -> 101   -> False

Approach:
- Traverse the bits from right to left.
- Check the current bit and the next bit.
- If a pair "11" is found:
    - If it's the first pair, mark it.
    - If a pair was already found, return False.
- After processing all bits:
    - Return whether exactly one pair was found.

Time Complexity:
O(log n)

Space Complexity:
O(1)
"""

class Solution(object):

    def consecutiveSetBits(self, n):
        """
        :type n: int
        :rtype: bool
        """

        pairDone = False

        while n >= 1:

            if n % 2 == 1 and (n // 2) % 2 == 1 and not pairDone:
                pairDone = True

            elif n % 2 == 1 and (n // 2) % 2 == 1 and pairDone:
                return False

            n //= 2

        return pairDone
