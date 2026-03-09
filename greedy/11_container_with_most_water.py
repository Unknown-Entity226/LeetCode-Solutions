'''
Problem Description:
You are given an integer array height where each element represents
the height of a vertical line drawn at that index.

Two lines together with the x-axis form a container that can hold water.
The amount of water a container can hold is determined by:

    width * min(height[left], height[right])

where:
    width = distance between the two lines.

Return the maximum amount of water that can be contained.
The container cannot be slanted.

Approach:
- Use the two-pointer technique.
- Start with one pointer at the beginning (left) and one at the end (right).
- Compute the current container area using:

      (right - left) * min(height[left], height[right])

- Update the maximum area found so far.
- Move the pointer that has the smaller height inward:
    - Because the area is limited by the shorter line.
    - Moving the taller line cannot increase the area.

- Continue until the two pointers meet.

Time Complexity:
O(n), where n is the length of the height array.

Space Complexity:
O(1)
'''
class Solution(object):
    def maxArea(self, height):

        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            current_area = (right - left) * min(height[left], height[right])

            if current_area > max_water:
                max_water = current_area

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return max_water
