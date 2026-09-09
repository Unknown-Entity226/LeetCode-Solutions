"""
Problem Description:
Given an integer n, count the total number of commas used when writing
all integers from 1 to n in standard number formatting.

Approach:
- Every number from 1000 onward contains at least one comma.
- Therefore, if n >= 1000, the numbers containing a comma are:
  1000, 1001, ..., n.
- The number of such integers is n - 1000 + 1.
- If n < 1000, no number contains a comma.

Time Complexity:
O(1)

Reason:
- Only a single comparison and arithmetic calculation are performed.

Space Complexity:
O(1)

Reason:
- No additional data structures are used.
"""

class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n >= 1000:
            return n-1000+1
        else:
            return 0
