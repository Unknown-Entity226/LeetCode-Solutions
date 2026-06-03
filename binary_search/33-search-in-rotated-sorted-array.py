"""
Problem Description:
Given a sorted array that has been rotated at an unknown pivot,
return the index of target if it exists, otherwise return -1.

The solution must run in O(log n) time.

Approach:
1. Find the pivot (smallest element) using binary search.
2. Determine which sorted half may contain the target.
3. Perform a standard binary search on that half.

Time Complexity:
O(log n)
- Pivot search: O(log n)
- Binary search: O(log n)

Space Complexity:
O(1)
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def findPivot(arr):
            left = 0
            right = len(arr)-1

            while left < right:
                mid = (left + right) // 2

                if arr[mid] >= arr[0]:
                    left = mid + 1
                else:
                    right = mid

            return left

        pivot = 0 if nums[0]<=nums[-1] else findPivot(nums)

        if nums[pivot] == target:
            return pivot

        def binarySearch(arr, target, left=0, right=-1):

            while left <= right:

                mid = (left + right) // 2

                if arr[mid] == target:
                    return mid

                elif arr[mid] > target:
                    right = mid - 1

                else:
                    left = mid + 1

            return -1

        if nums[pivot] < target and target <= nums[len(nums)-1]:
            return binarySearch(nums, target, pivot, len(nums)-1)

        else:
            return binarySearch(nums, target, 0, pivot)
