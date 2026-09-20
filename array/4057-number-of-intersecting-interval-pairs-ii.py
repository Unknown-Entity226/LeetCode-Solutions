"""
Problem Description:
Given n closed intervals, count the number of pairs of intervals that
intersect. Two intervals intersect if they have at least one point in
common, including a shared endpoint.

Approach:
- Separate all start points and end points and sort both arrays.
- For each start point, count how many intervals have already ended
  strictly before that start point.
- Such intervals cannot intersect the current interval.
- Since the intervals are closed, an endpoint touching another interval
  is considered an intersection, so an interval ending exactly at the
  current start is NOT counted as a non-intersecting interval.
- Count all possible pairs using n * (n - 1) / 2.
- Subtract the number of non-intersecting pairs.

Time Complexity:
O(n log n)

Reason:
- Sorting the starts and ends takes O(n log n).
- The two-pointer traversal takes O(n).

Space Complexity:
O(n)

Reason:
- Separate arrays of starts and ends are created.
"""

class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:

        size = len(intervals)
        starts = [i[0] for i in intervals]
        starts.sort()

        ends = [i[1] for i in intervals]
        ends.sort()

        end = 0
        non_intersection = 0
        for start in range(size):
            
            while end<size and ends[end]<starts[start]:
                end+=1
            non_intersection += end

        total = size*(size-1)//2

        return total - non_intersection
        
