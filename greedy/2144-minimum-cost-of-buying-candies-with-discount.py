"""
Problem Description:
A shop offers a promotion:
- For every two candies purchased, one additional candy can be taken for free.
- The free candy must have a cost less than or equal to the cheaper
  of the two purchased candies.

Return the minimum cost required to obtain all candies.

Approach:
- Sort the candies by cost.
- Start from the most expensive candies.
- For every group of three candies:
    - Pay for the two most expensive.
    - Take the third most expensive for free.
- Accumulate the cost of only the candies that must be paid for.

Time Complexity:
O(n log n)
- Due to sorting.

Space Complexity:
O(1)
- Ignoring the space used by the sorting algorithm.
"""
class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        size = len(cost)
        cost.sort()

        i = size - 1
        j = size - 2
        total = 0

        while i >= 0 and j >= 0:
            total += cost[i] + cost[j]
            i -= 3
            j -= 3

        if i >= 0:
            total += cost[i]

        if j >= 0:
            total += cost[j]

        return total
