"""
Problem Description:
Given an array nums of length n, construct a new array
of length 2n such that:

- The first n elements are the same as nums.
- The next n elements are nums in reverse order.

Return the resulting array.

Approach:
- Store the original size of the array.
- Traverse the original elements from the last index to
  the first.
- Append each element to the end of the array.
- Since the original size is fixed before appending,
  only the original elements are processed.

Time Complexity:
O(n)

Space Complexity:
O(1)
- Ignoring the space required for the output array.
"""

class Solution(object):

    def concatWithReverse(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        size = len(nums)

        for i in range(size - 1, -1, -1):
            nums.append(nums[i])

        return nums
