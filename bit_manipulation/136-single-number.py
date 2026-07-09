"""
Problem Description:
Given a non-empty array of integers where every element
appears exactly twice except for one element that appears
only once, return that single element.

The solution must run in linear time and use constant
extra space.

Approach:
Use the XOR operation.

Properties of XOR:
- x ^ x = 0
- x ^ 0 = x
- XOR is commutative and associative.

Therefore, XORing all elements together causes every
duplicate pair to cancel out, leaving only the unique
element.

Time Complexity:
O(n)

Space Complexity:
O(1)
"""

class Solution(object):

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ans = nums[0]

        for i in range(1, len(nums)):
            ans = ans ^ nums[i]

        return ans
