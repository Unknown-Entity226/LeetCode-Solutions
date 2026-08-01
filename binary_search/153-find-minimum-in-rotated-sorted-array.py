"""
Problem Description:
Given a sorted array that has been rotated, return the
minimum element.

Approach:
- If the array is already sorted, return the first
  element.
- Otherwise, use Binary Search.
- Compare the middle element with the first element:
  - If nums[mid] >= nums[0], the minimum lies in the
    right half.
  - Otherwise, the minimum lies in the left half
    (including mid).
- Continue until the search space reduces to one element.

Time Complexity:
O(log n)

Reason:
- Binary Search halves the search space in every
  iteration.

Space Complexity:
O(1)

Reason:
- Only a few pointer variables are used.
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0]<=nums[-1]:
            return nums[0]

        left =0
        right = len(nums)-1

        while left<right:
            mid = (left+right)//2

            if nums[mid]>=nums[0]:
                left = mid+1

            else:
                right = mid

        return nums[left]
