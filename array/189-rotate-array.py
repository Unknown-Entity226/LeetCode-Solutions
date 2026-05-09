'''
Problem Description:
Given an integer array nums, rotate the array to the right by k steps,
where k is non-negative.

Example:
nums = [1,2,3,4,5,6,7], k = 3
Result → [5,6,7,1,2,3,4]

Approach:
Use the reversal algorithm:

1. Reverse the entire array
2. Reverse the first k elements
3. Reverse the remaining elements

Time Complexity:
O(n)

Space Complexity:
O(1), in-place rotation.
'''
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        def rev(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        rev(0, len(nums) - 1)
        rev(0, k - 1)
        rev(k, len(nums) - 1)
