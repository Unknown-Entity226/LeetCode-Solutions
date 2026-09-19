"""
Problem Description:
Given a circle and an axis-aligned rectangle, determine whether they
overlap, meaning that they have at least one point in common.

Approach:
- Find the point on the rectangle that is closest to the circle's
  center.
- Clamp the circle center's x-coordinate to the rectangle's horizontal
  range and its y-coordinate to the rectangle's vertical range.
- This produces the closest point on or inside the rectangle to the
  circle center.
- Calculate the squared Euclidean distance between this point and the
  circle center.
- The circle and rectangle overlap if this distance is less than or
  equal to the squared radius.

Time Complexity:
O(1)

Reason:
- Only a constant number of arithmetic operations are performed.

Space Complexity:
O(1)

Reason:
- Only a constant number of variables are used.
"""

class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        
        def clamp(point, low, high):

            return max(low, min(point, high))
            
        px = clamp(xCenter, x1, x2)
        py = clamp(yCenter, y1, y2)

        d_sqr = (px-xCenter)**2+ (py-yCenter)**2

        return d_sqr<=radius**2
