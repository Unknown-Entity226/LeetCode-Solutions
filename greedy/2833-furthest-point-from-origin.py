'''
Problem Description:
Given a string moves consisting of 'L', 'R', and '_':
- 'L' → move left
- 'R' → move right
- '_' → can be chosen as either 'L' or 'R'

Starting from 0, return the maximum possible distance from origin
after performing all moves.

Approach:
- Count:
    L = number of 'L'
    R = number of 'R'
    _ = number of flexible moves

- Current displacement = |L - R|
- To maximize distance, assign ALL '_' in the same direction
  as the dominant side (either left or right).

- So final distance:
      abs(L - R) + _

Time Complexity:
O(n)

Space Complexity:
O(1)
'''
class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        l = 0
        r = 0
        dash = 0
        for i in range(len(moves)):
            if moves[i] == 'L':
                l +=1
            elif moves[i] == 'R':
                r+=1
            else:
                dash +=1
        return abs(l-r)+dash
