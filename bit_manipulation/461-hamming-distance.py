"""
Problem Description:
The Hamming distance between two integers is the number
of bit positions at which they differ.

Given two integers x and y, return their Hamming
distance.

Approach:
- XOR the two numbers.
- In the XOR result:
    - A bit is 1 if the corresponding bits of x and y
      are different.
    - A bit is 0 if they are the same.
- Count the number of set bits (1s) in the XOR result.
- Return the count.

Time Complexity:
O(b)

Space Complexity:
O(1)

where b is the number of bits in the XOR result.
"""

class Solution(object):

    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        num = x ^ y

        count = 0

        while num:

            digit = num % 2

            if digit == 1:
                count += 1

            num //= 2

        return count
