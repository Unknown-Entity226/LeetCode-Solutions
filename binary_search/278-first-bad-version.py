"""
Problem Description:
Given n versions [1, 2, ..., n] and an API:

    isBadVersion(version)

which returns whether a version is bad.

All versions after a bad version are also bad.

Return the first bad version while minimizing API calls.

Approach:
- Use binary search on the version range.
- If mid is bad:
      the first bad version is at mid or to its left.
- If mid is good:
      the first bad version must be to the right.
- Continue until the search space collapses.
- The final value of left will be the first bad version.

Time Complexity:
O(log n)

Space Complexity:
O(1)
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n-1

        while left<=right:
            mid = (left+right)//2

            if isBadVersion(mid) == True:
                right = mid-1
            else:
                left = mid+1
        return left
