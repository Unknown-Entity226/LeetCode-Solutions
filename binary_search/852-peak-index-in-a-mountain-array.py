"""
Problem Description:
Given a mountain array arr, return the index of the peak element.

A mountain array:
- Strictly increases up to a peak.
- Strictly decreases after the peak.

The solution must run in O(log n) time.

Approach:
- Use binary search.
- If arr[mid] < arr[mid + 1], we are on the increasing slope,
  so the peak lies to the right.
- If arr[mid] < arr[mid - 1], we are on the decreasing slope,
  so the peak lies to the left.
- If arr[mid] is greater than or equal to both neighbors,
  it is the peak.

Time Complexity:
O(log n)

Space Complexity:
O(1)
"""

class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        left = 0
        right = len(arr) - 1

        while left <= right:

            mid = (left + right) // 2

            if arr[mid] >= arr[mid - 1] and arr[mid] >= arr[mid + 1]:
                return mid

            if arr[mid] < arr[mid + 1]:
                left = mid + 1

            elif arr[mid] < arr[mid - 1]:
                right = mid - 1
