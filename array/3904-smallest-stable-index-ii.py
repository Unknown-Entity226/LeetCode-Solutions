"""
Problem Description:
Given an integer array nums and an integer k, the instability score
of index i is:

max(nums[0..i]) - min(nums[i..n-1])

Return the smallest index whose instability score is <= k.
Return -1 if no such index exists.

Approach:
- Build a suffix minimum array where suffix[i] stores the minimum
  element from index i to the end of nums.
- Traverse nums from left to right while maintaining the maximum
  element seen so far.
- For each index i, calculate the instability score using the
  current prefix maximum and suffix[i].
- Return the first index whose score is <= k.

Time Complexity:
O(n)

Reason:
- Constructing the suffix minimum array takes O(n).
- Finding the first stable index takes O(n).
- Therefore, the total time complexity is O(n).

Space Complexity:
O(n)

Reason:
- The suffix array stores one value for every element of nums.
"""

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        
        suffix = [0]*len(nums)

        n = nums[-1]

        for i in range(len(nums)-1, -1, -1):
            n = min(nums[i], n)

            suffix[i] = n 

        m = nums[0]

        for i in range(len(nums)):

            m = max(nums[i], m)

            if m-suffix[i]<=k:
                return i

        return -1
        
