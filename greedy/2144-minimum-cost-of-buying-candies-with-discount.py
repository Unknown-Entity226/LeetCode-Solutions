"""
Problem Description:
A shop offers the following discount:

For every two candies bought,
you may take a third candy for free provided:

    free_candy_cost <= min(bought_candy_1, bought_candy_2)

Return the minimum amount of money needed to buy all candies.

Approach:
- To maximize the discount, we want the most expensive candies
  to be paid for and every third candy to be as expensive as possible.
- Sort the array in descending order.
- Process candies in groups of three:
    - Pay for the first two candies.
    - Get the third candy for free.
- Add the costs of the first two candies from each group.

Example:
cost = [6,5,4,3,2,1]

Sorted descending:
[6,5,4,3,2,1]

Groups:
(6,5,4) -> pay 6+5, get 4 free
(3,2,1) -> pay 3+2, get 1 free

Total = 16

Time Complexity:
O(n log n)

Space Complexity:
O(1)
"""

class Solution(object):

    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        cost.sort(reverse=True)

        total = 0

        for i in range(len(cost)):

            if i % 3 != 2:
                total += cost[i]

        return total
