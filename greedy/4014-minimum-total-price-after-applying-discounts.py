"""
Problem Description:
Given arrays of item prices and discount percentages,
assign discounts to items to minimize the total final price.

Approach:
- Sort both prices and discounts in ascending order.
- Pair the largest price with the largest discount.
- Continue pairing while both arrays have elements.
- Add any remaining undiscounted prices to the total.

Time Complexity:
O(n log n + m log m)

Reason:
- Sorting prices takes O(n log n).
- Sorting discounts takes O(m log m).
- The two-pointer traversal takes O(min(n, m)).

Space Complexity:
O(1)

Reason:
- Only a constant number of variables are used,
  excluding the sorting implementation's internal space.
"""

class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort()
        discounts.sort()
        total = 0
        
        p = len(prices)-1
        d = len(discounts)-1

        while p>=0 and d>=0:
            total+= prices[p] - 0.01*discounts[d]*prices[p]

            p-=1
            d-=1
        
        while p>=0:
            total+=prices[p]
            p-=1
        return total
