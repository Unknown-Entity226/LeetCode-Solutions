"""
Problem Description:
Given a permutation nums of integers from 0 to n - 1, find the
maximum non-negative integer k such that the array can be sorted
using swaps only between elements whose bitwise AND equals k.
Return 0 if nums is already sorted.

Approach:
- Traverse nums and identify elements that are not at their
  correct indices.
- Initialize result with the first misplaced element.
- Compute the bitwise AND of all subsequent misplaced elements.
- Return the accumulated AND, or 0 if the array is already sorted.

Time Complexity:
O(n)

Reason:
- A single traversal checks every element.
- Each bitwise AND operation takes O(1) time for fixed-width integers.
- Therefore, the total time complexity is O(n).

Space Complexity:
O(1)

Reason:
- Only the result variable and loop index are used.
- No additional data structure proportional to n is created.
"""
class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        result = None
        for i in range(len(nums)):
            if i!=nums[i]:
                if result is None:
                    result = nums[i]
                else:
                    result&=nums[i]
        return result if result is not None else 0
