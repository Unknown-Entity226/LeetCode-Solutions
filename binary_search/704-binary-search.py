"""
Problem Description:
Given a sorted array of distinct integers and a target
value, return the index of the target if it exists.
Otherwise, return -1.

The solution must run in O(log n) time.

Approach:
Use Binary Search.

- Maintain two pointers:
    - start
    - end
- Repeatedly examine the middle element.
- If it matches the target, return its index.
- If the target is smaller, search the left half.
- Otherwise, search the right half.
- If the search space becomes empty, the target does
  not exist.

Time Complexity:
O(log n)

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

        start = 0
        end = len(nums) - 1

        while start <= end:

            mid = (start + end) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                end = mid - 1

            else:
                start = mid + 1

        return -1
