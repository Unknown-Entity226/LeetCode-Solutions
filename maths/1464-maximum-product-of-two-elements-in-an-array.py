"""
Problem Description:
Given an integer array, return the maximum value of
(nums[i] - 1) * (nums[j] - 1), where i and j are
different indices.

Approach:
- Maintain the largest and second largest elements.
- Traverse the array once to update these values.
- Compute (largest - 1) * (secondLargest - 1).

Time Complexity:
O(n)

Reason:
- The array is traversed once.
- Each element is processed in constant time.

Space Complexity:
O(1)

Reason:
- Only two variables are used to track the largest
  elements.
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        l = 0
        s = 0

        for i in nums:
            if i>=l:
                s = l
                l = i
            elif i>s:
                s=i

        return (l-1)*(s-1)
