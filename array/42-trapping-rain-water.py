"""
Problem Description:
Given an elevation map where each bar has width 1, calculate the total
amount of rainwater that can be trapped between the bars.

Approach:
- Build a left array where left[i] stores the maximum height encountered
  from the left up to index i.
- Build a right array where right[i] stores the maximum height encountered
  from the right up to index i.
- For every index, the water level is the minimum of the left and right
  maximum heights.
- The trapped water at index i is:
  min(left[i], right[i]) - height[i].
- Sum the trapped water across all indices.

Time Complexity:
O(n)

Reason:
- The left maximum array requires O(n).
- The right maximum array requires O(n).
- The final calculation requires O(n).
- Therefore the total is O(n).

Space Complexity:
O(n)

Reason:
- The left and right arrays each store n values.
"""

class Solution:
    def trap(self, height: list[int]) -> int:
        
        size = len(height)

        left= [0]*size
        right = [0]*size

        left_max = height[0]
        right_max = height[-1]

        for  i in range(size):
            left_max = max(height[i], left_max)

            left[i] = left_max

        for i in range(size-1, -1, -1):
            right_max = max(right_max,  height[i])

            right[i] = right_max

        result = 0

        for i in range(size):

            result += min(left[i], right[i])- height[i]

        return result
