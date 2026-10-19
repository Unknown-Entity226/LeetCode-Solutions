"""
Problem Description:
Given an integer array nums and a target, return the indices
where target occurs after sorting nums in non-decreasing order.

Approach:
- Sort nums in non-decreasing order.
- Traverse the sorted array from left to right.
- Append each index where nums[i] equals target.
- Return the resulting list of indices.

Time Complexity:
O(n log n)

Reason:
- Sorting nums takes O(n log n).
- Traversing the array takes O(n).
- Sorting dominates the overall time complexity.

Space Complexity:
O(n)

Reason:
- The result list requires O(k) space, where k is the
  number of occurrences of target.
- In the worst case, k = n, so the result requires O(n) space.
- Python's sorting implementation may also use temporary space.
"""
class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        
        nums.sort()

        result = []

        for i in range(len(nums)):
            if nums[i] == target:
                result.append(i)


        return result
