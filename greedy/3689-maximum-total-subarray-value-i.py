"""
Problem Description:
You must choose exactly k non-empty subarrays.

The value of a subarray is:

    max(subarray) - min(subarray)

Subarrays may:
- Overlap
- Be chosen multiple times
- Even be the exact same subarray

Return the maximum possible total value.

Approach:
- Since the same subarray can be chosen multiple times,
  we only need to find the maximum possible value of a
  single subarray.
- The maximum value is achieved by a subarray containing:
      global maximum element
      global minimum element
- Such a subarray has value:

      max(nums) - min(nums)

- Since we may choose the same subarray repeatedly,
  choose that optimal subarray k times.

Time Complexity:
O(n)

Space Complexity:
O(1)
"""

class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        m = nums[0]
        n = nums[0]

        for i in range(len(nums)):

            if nums[i] > m:
                m = nums[i]

            if nums[i] < n:
                n = nums[i]

        return k * (m - n)
