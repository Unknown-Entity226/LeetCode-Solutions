"""
Problem Description:
Given a list of intervals, remove every interval that is
completely covered by another interval.

An interval [a, b) is covered by [c, d) if:

    c <= a
    b <= d

Return the number of remaining intervals.

Approach:
- Sort the intervals by their starting point (and ending
  point for ties).
- Maintain the last interval that has not been covered.
- For each interval:
    - If it has the same start but a larger end,
      replace the current interval since it covers it.
    - If it is covered by the current interval,
      ignore it.
    - Otherwise, it becomes the new current interval and
      contributes to the answer.

Time Complexity:
O(n log n)

Space Complexity:
O(1)
- Ignoring the space used by the sorting algorithm.
"""

class Solution(object):

    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        intervals.sort()

        start = -1
        end = -1

        count = 0

        for i in intervals:

            if start == -1:
                start = i[0]
                end = i[1]
                count += 1

            else:

                if start == i[0] and end <= i[1]:
                    start = i[0]
                    end = i[1]

                elif start <= i[0] and end >= i[1]:
                    continue

                else:
                    start = i[0]
                    end = i[1]
                    count += 1

        return count
