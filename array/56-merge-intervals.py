"""
Problem Description:
Given a collection of intervals, merge all overlapping
intervals and return the resulting non-overlapping
intervals.

Approach:
- Sort the intervals by their starting value.
- Traverse the sorted intervals.
- Maintain the last merged interval in the answer.
- For each interval:
    - If it overlaps with the last merged interval,
      extend the ending point.
    - Otherwise, append it as a new interval.

Time Complexity:
O(n log n)

Space Complexity:
O(n)
- Excluding the space used by the sorting algorithm.
"""

class Solution(object):

    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals.sort()

        ans = []

        for i in intervals:

            s = i[0]
            e = i[1]

            if not ans:
                ans.append([s, e])

            else:

                start = ans[-1][0]
                end = ans[-1][1]

                if start <= s and s <= end:
                    ans[-1][1] = max(end, e)

                else:
                    ans.append([s, e])

        return ans
