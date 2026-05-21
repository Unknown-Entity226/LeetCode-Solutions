'''
Problem Description:
Given an integer n, return True if it is a power of four.

An integer n is a power of four if there exists
an integer x such that:

    n = 4^x

Approach:
- Handle non-positive numbers first.
- Repeatedly divide n by 4 while it is divisible by 4.
- If the final value becomes 1,
  then n was a power of four.

Example:
64 → 16 → 4 → 1  => True

48 → 12 → 3      => False

Time Complexity:
O(log₄ n)

Space Complexity:
O(1)
'''
class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n <= 0:
            return False

        while n % 4 == 0:
            n //= 4

        return n == 1
