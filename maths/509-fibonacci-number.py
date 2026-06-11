"""
Problem Description:
The Fibonacci sequence is defined as:

    F(0) = 0
    F(1) = 1

For n >= 2:

    F(n) = F(n - 1) + F(n - 2)

Given n, return F(n).

Approach:
- Use two variables:
    a = F(n-2)
    b = F(n-1)
- Iteratively compute the next Fibonacci number.
- Update the variables after each computation.
- This avoids recursion and uses constant extra space.

Time Complexity:
O(n)

Space Complexity:
O(1)
"""

class Solution(object):

    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """

        a = 0
        b = 1

        if n == 0 or n == 1:
            return n

        total = 0

        for _ in range(2, n + 1):

            total = a + b
            a = b
            b = total

        return total
