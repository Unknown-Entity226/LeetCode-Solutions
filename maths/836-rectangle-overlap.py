"""
Problem Description:
Given two axis-aligned rectangles represented by [x1, y1, x2, y2],
determine whether their intersection has positive area.

Rectangles that only touch at an edge or corner are not considered
overlapping.

Approach:
- Compare the projections of both rectangles on the X-axis and Y-axis.
- If one rectangle is completely to the left or right of the other,
  there is no overlap.
- If one rectangle is completely above or below the other, there is
  no overlap.
- Use strict separation conditions so that rectangles touching only
  at an edge or corner correctly return False.
- If none of the separation conditions hold, the rectangles overlap
  with positive area.

Time Complexity:
O(1)

Reason:
- Only a constant number of coordinate comparisons are performed.

Space Complexity:
O(1)

Reason:
- Only a constant number of variables are used.
"""

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        

        x1, y1, x2, y2 = rec1[0],rec1[1],rec1[2],rec1[3]

        x3, y3, x4, y4 = rec2[0],rec2[1],rec2[2],rec2[3]


        if x1>=x4 or x2<=x3 or y1>=y4 or y2<=y3:
            return False
        return True
