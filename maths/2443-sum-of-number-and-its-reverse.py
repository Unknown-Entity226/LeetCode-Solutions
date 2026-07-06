"""
Problem Description:
Given a non-negative integer num, determine whether there
exists a non-negative integer x such that:

    x + reverse(x) = num

Return True if such an integer exists, otherwise False.

Approach:
- Handle the special case:
      num = 0
- Define a helper function to reverse an integer.
- Try every possible value from 0 to num - 1.
- If any value satisfies:

      x + reverse(x) == num

  return True.
- Otherwise, return False.

Time Complexity:
O(n × d)

where:
- n = num
- d = number of digits in num

Since reversing an integer takes O(d),

Overall:
O(num × log(num))

Space Complexity:
O(1)
"""

class Solution(object):

    def sumOfNumberAndReverse(self, num):
        """
        :type num: int
        :rtype: bool
        """

        if num == 0:
            return True

        def rev(n):

            temp = 0

            while n != 0:
                temp = temp * 10 + n % 10
                n //= 10

            return temp

        for i in range(num):

            if num == (i + rev(i)):
                return True

        return False
