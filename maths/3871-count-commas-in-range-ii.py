"""
Problem Description:
Given an integer n, count the total number of commas used when writing
all integers from 1 to n in standard number formatting.

Approach:
- A comma first appears in numbers >= 1000.
- Every number from 1000 onward contributes at least one comma.
- A second comma appears in numbers >= 1,000,000.
- A third comma appears in numbers >= 1,000,000,000, and so on.
- For every power of 1000, count how many numbers from that value
  through n contain a comma at that position.
- Sum these contributions.

Time Complexity:
O(log_1000(n))

Reason:
- The loop runs once for every power of 1000 up to n.

Space Complexity:
O(1)

Reason:
- Only a constant number of variables are used.
"""

class Solution:
    def countCommas(self, n: int) -> int:
        count = 0
        power = 1000

        while power<=n:
            count+= n-power+1
            power*=1000

        return count
