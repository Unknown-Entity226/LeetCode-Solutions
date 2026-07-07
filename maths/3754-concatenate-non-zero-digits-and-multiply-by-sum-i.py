"""
Problem Description:
Given an integer n:

- Form a new integer x by concatenating all non-zero
  digits of n while preserving their original order.
- If n contains no non-zero digits, then x = 0.
- Let sum be the sum of the digits of x.

Return:

    x × sum

Approach:
- Traverse the digits of n from right to left.
- Ignore every digit equal to 0.
- Build x using place values so that the original order
  of the non-zero digits is preserved.
- Simultaneously compute the sum of the retained digits.
- Return the product of x and the digit sum.

Time Complexity:
O(d)

Space Complexity:
O(1)

where d is the number of digits in n.
"""

class Solution(object):

    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """

        s = 0
        m = 0
        ten = 1

        while n != 0:

            if n % 10 != 0:
                m = m + (n % 10) * ten
                ten *= 10
                s += n % 10

            n //= 10

        return m * s
