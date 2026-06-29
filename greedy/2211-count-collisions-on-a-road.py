"""
Problem Description:
There are n cars moving on a road.

Each car is:
- 'L' : moving left
- 'R' : moving right
- 'S' : stationary

When cars collide:
- R and L collide -> 2 collisions
- Moving car and stationary car -> 1 collision
- After a collision, the involved cars become stationary.

Return the total number of collisions.

Approach:
- Cars moving left at the very beginning never collide,
  since there is nothing to their left.
- Cars moving right at the very end never collide,
  since there is nothing to their right.
- Every remaining moving car ('L' or 'R') must eventually
  collide exactly once.
- Therefore:
    answer =
        (number of non-stationary cars)
        - (leading L's)
        - (trailing R's)

Time Complexity:
O(n)

Space Complexity:
O(1)
"""

class Solution(object):

    def countCollisions(self, directions):
        """
        :type directions: str
        :rtype: int
        """

        rCount = 0
        lCount = 0
        mixCount = 0

        i = 0

        while i < len(directions) and directions[i] == "L":
            lCount += 1
            i += 1

        j = len(directions) - 1

        while j >= 0 and directions[j] == "R":
            rCount += 1
            j -= 1

        for car in directions:

            if car != "S":
                mixCount += 1

        return mixCount - lCount - rCount
