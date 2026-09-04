"""
Problem Description:
Given an integer array nums and an integer k, the instability score
of index i is:

max(nums[0..i]) - min(nums[i..n-1])

Return the smallest index whose instability score is <= k.
Return -1 if no such index exists.

Approach:
- Precompute the minimum value from each index to the end of the array
  using a suffix minimum array.
- Traverse the array from left to right while maintaining the maximum
  value seen so far.
- For each index i, calculate:
      prefix_max - suffix_min[i]
- Return the first index where the instability score is <= k.

Time Complexity:
O(n)

Reason:
- Constructing the suffix minimum array takes O(n).
- The second traversal takes O(n).
- Therefore, total time is O(n).

Space Complexity:
O(n)

Reason:
- The suffix array stores one minimum value for every index.
"""


class Solution:

    def firstStableIndex(self, nums: list[int], k: int) -> int:
        
        m = nums[0]

        suffix = [0]*len(nums)
        n = nums[-1]
        for i in range(len(nums)-1, -1,-1):
            n = min(n, nums[i])
            suffix[i] = n
        
        for i in range(len(nums)):

            m = max(m, nums[i])
            if m- suffix[i]<=k:
                return i
        return -1
