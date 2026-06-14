"""
Problem Description:
Given a positive integer n:

digitSum  = sum of its digits
squareSum = sum of the squares of its digits

An integer is considered good if:

    squareSum - digitSum >= 50

Return True if n is good, otherwise return False.

Approach:
- Extract each digit using modulo 10.
- Add the digit to digitSum.
- Add the square of the digit to squareSum.
- Remove the last digit using integer division by 10.
- After processing all digits, check whether:

      squareSum - digitSum >= 50

Time Complexity:
O(d)

where d is the number of digits in n.

Space Complexity:
O(1)
"""

class Solution(object):

    def checkGoodInteger(self, n):
        """
        :type n: int
        :rtype: bool
        """

        digitSum = 0
        squareSum = 0

        while n > 0:

            digit = n % 10

            digitSum += digit
            squareSum += digit * digit

            n //= 10

        return squareSum - digitSum >= 50
