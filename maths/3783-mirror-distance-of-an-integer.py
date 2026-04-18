'''
Problem Description:
Given an integer n, define its mirror distance as:
    abs(n - reverse(n))

where reverse(n) is formed by reversing the digits of n.

Return the mirror distance.

Approach:
- Reverse the integer using digit extraction:
    - Extract last digit using n % 10
    - Build reversed number using rev = rev * 10 + digit
    - Remove last digit using integer division
- Compute absolute difference between original and reversed number.

Time Complexity:
O(d), where d is the number of digits in n.

Space Complexity:
O(1)
'''
class Solution(object):
    def mirrorDistance(self, n):
        """
        :type n: int
        :rtype: int
        """
        temp = n
        rev = 0

        while temp > 0:
            rev = rev * 10 + temp % 10
            temp //= 10

        return abs(n - rev)
