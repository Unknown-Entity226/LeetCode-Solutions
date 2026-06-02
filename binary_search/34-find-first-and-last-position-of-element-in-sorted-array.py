"""
Problem Description:
Given a sorted array nums and a target value,
return the starting and ending position of the target.

If the target does not exist in the array,
return [-1, -1].

The solution must run in O(log n) time.

Approach:
- Use binary search twice.
- First binary search:
    Find the first occurrence of target.
    When target is found, continue searching left.
- Second binary search:
    Find the last occurrence of target.
    When target is found, continue searching right.
- Return [first_occurrence, last_occurrence].

Time Complexity:
O(log n)

Space Complexity:
O(1)
"""

class Solution(object):

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def first(array, target):

            left = 0
            right = len(array) - 1
            ans = -1

            while left <= right:

                mid = (left + right) // 2

                if array[mid] > target:
                    right = mid - 1

                elif array[mid] < target:
                    left = mid + 1

                else:
                    ans = mid
                    right = mid - 1

            return ans

        def last(array, target):

            left = 0
            right = len(array) - 1
            ans = -1

            while left <= right:

                mid = (left + right) // 2

                if array[mid] > target:
                    right = mid - 1

                elif array[mid] < target:
                    left = mid + 1

                else:
                    ans = mid
                    left = mid + 1

            return ans

        return [first(nums, target), last(nums, target)]
