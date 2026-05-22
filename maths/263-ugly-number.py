'''
Problem Description:
An ugly number is a positive integer whose prime factors
only include:

    2, 3, and 5

Return True if n is an ugly number,
otherwise return False.

Approach:
- Handle edge cases:
    - 0 is not ugly
    - 1 is considered ugly

- Repeatedly divide n by:
    - 2
    - 3
    - 5

whenever divisible.

- If after removing all factors of 2, 3, and 5,
  the number becomes 1:
      → only these prime factors existed
      → return True

- Otherwise:
      → some other prime factor exists
      → return False

Time Complexity:
O(log n)

Since n keeps shrinking by division.

Space Complexity:
O(1)
'''
class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n == 1:
            return True

        if n == 0:
            return False

        while n != 1:

            if n % 2 == 0:
                n //= 2

            elif n % 3 == 0:
                n //= 3

            elif n % 5 == 0:
                n //= 5

            else:
                return False

        return True
