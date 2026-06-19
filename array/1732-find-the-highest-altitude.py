"""
Problem Description:
A biker starts at altitude 0.

gain[i] represents the change in altitude between
point i and point i + 1.

Return the highest altitude reached during the trip.

Approach:
- Maintain the current altitude.
- Start at altitude 0.
- For each gain:
    - Update the current altitude.
    - Update the maximum altitude seen so far.
- Return the maximum altitude.

Time Complexity:
O(n)

Space Complexity:
O(1)
"""

class Solution(object):

    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """

        highest = 0
        height = 0

        for i in gain:

            height += i
            highest = max(highest, height)

        return highest
