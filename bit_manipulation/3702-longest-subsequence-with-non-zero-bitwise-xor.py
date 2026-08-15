"""
Problem Description:
Given an integer array nums, return the length of the
longest subsequence whose bitwise XOR is non-zero.

Approach:
- Compute the XOR of all elements.
- If the XOR of the entire array is non-zero, the complete
  array is the longest possible subsequence.
- If the total XOR is zero, removing any one element x
  changes the XOR to:
      total_xor ^ x
  Since total_xor is 0, this becomes x.
- Therefore, if any element is non-zero, removing that
  element produces a subsequence with non-zero XOR and
  length n - 1.
- If every element is zero, every subsequence has XOR 0,
  so return 0.

Time Complexity:
O(n)

Reason:
- The first loop computes the XOR of all elements in O(n).
- If the total XOR is zero, the second loop checks for a
  non-zero element in O(n) in the worst case.
- Therefore, total time is O(n).

Space Complexity:
O(1)

Reason:
- Only a constant number of variables are used.
"""

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        
        # xor of total:
        xor = 0

        for i in nums:
            xor^=i
        if xor:
            return len(nums)
        sub = len(nums)
        idx = 0
        
        while idx<len(nums):

            if xor^nums[idx]!=0:
                return sub-1

            idx+=1
                        
        return 0
